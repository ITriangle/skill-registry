from __future__ import annotations

import importlib.machinery
import shutil
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


SKILLCTL_PATH = Path(__file__).resolve().parents[1] / "bin" / "skillctl"
skillctl = importlib.machinery.SourceFileLoader("skillctl_test_module", str(SKILLCTL_PATH)).load_module()


class TranslationMirrorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        skillctl.ROOT = root
        skillctl.PROJECTS_DIR = root / "projects"
        skillctl.SOURCES_DIR = root / "sources"
        skillctl.SKILLS_DIR = root / "skills"
        skillctl.ANALYSIS_DIR = root / "analysis"
        skillctl.GROUPS_FILE = root / "skill-groups.yaml"
        skillctl.LOCALES_DIR = root / "locales"

        self.skill_id = "vendor/acme/demo"
        self.source = root / "skills" / "vendor" / "acme" / "demo"
        self.translated = root / "locales" / "zh-CN" / "vendor" / "acme" / "demo"
        self.source.mkdir(parents=True)
        self.translated.mkdir(parents=True)
        (self.source / "SKILL.md").write_text(
            "---\nname: demo\ndescription: Demo skill.\n---\n\nRead [guide](guide.md).\n",
            encoding="utf-8",
        )
        (self.source / "guide.md").write_text("# Guide\n", encoding="utf-8")
        (self.source / "LICENSE.txt").write_text("license", encoding="utf-8")
        (self.source / "scripts").mkdir()
        (self.source / "scripts" / "tool.py").write_text("print('ok')\n", encoding="utf-8")
        self.write_valid_translation()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write_valid_translation(self) -> None:
        (self.translated / "SKILL.md").write_text(
            "---\nname: demo\ndescription: 示例技能。\n---\n\n阅读[指南](guide.md)。\n",
            encoding="utf-8",
        )
        (self.translated / "guide.md").write_text("# 指南\n", encoding="utf-8")

    def stamp(self) -> None:
        (self.translated / ".translation.yaml").write_text(
            skillctl.dump_translation_manifest(self.skill_id, "zh-CN"),
            encoding="utf-8",
        )

    def test_complete_mirror_passes_and_excludes_license_and_code(self) -> None:
        self.assertEqual(
            [path.as_posix() for path in skillctl.translatable_files(self.skill_id)],
            ["SKILL.md", "guide.md"],
        )
        self.stamp()
        self.assertEqual(skillctl.translation_problems(self.skill_id, "zh-CN"), [])

    def test_missing_translation_is_reported(self) -> None:
        (self.translated / "guide.md").unlink()
        problems = skillctl.translation_content_problems(self.skill_id, "zh-CN")
        self.assertTrue(any("missing translation" in item for item in problems))

    def test_changed_source_hash_is_stale(self) -> None:
        self.stamp()
        (self.source / "guide.md").write_text("# Updated\n", encoding="utf-8")
        problems = skillctl.translation_problems(self.skill_id, "zh-CN")
        self.assertTrue(any("stale translation source hash" in item for item in problems))

    def test_changed_translation_must_be_stamped(self) -> None:
        self.stamp()
        (self.translated / "guide.md").write_text("# 已修改\n", encoding="utf-8")
        problems = skillctl.translation_problems(self.skill_id, "zh-CN")
        self.assertTrue(any("unstamped translation change" in item for item in problems))

    def test_added_and_deleted_source_documents_are_reported(self) -> None:
        self.stamp()
        (self.source / "new.md").write_text("new\n", encoding="utf-8")
        problems = skillctl.translation_problems(self.skill_id, "zh-CN")
        self.assertTrue(any("missing translation" in item and "new.md" in item for item in problems))
        (self.source / "new.md").unlink()
        (self.source / "guide.md").unlink()
        problems = skillctl.translation_content_problems(self.skill_id, "zh-CN")
        self.assertTrue(any("orphan translation" in item and "guide.md" in item for item in problems))

    def test_invalid_front_matter_and_non_chinese_description_are_reported(self) -> None:
        (self.translated / "SKILL.md").write_text(
            "---\nname: changed\ndescription: English only.\n---\n",
            encoding="utf-8",
        )
        problems = skillctl.translation_content_problems(self.skill_id, "zh-CN")
        self.assertTrue(any("name changed" in item for item in problems))
        self.assertTrue(any("not Chinese" in item for item in problems))

    def test_changed_relative_document_link_is_reported(self) -> None:
        (self.translated / "SKILL.md").write_text(
            "---\nname: demo\ndescription: 示例技能。\n---\n\n阅读[指南](missing.md)。\n",
            encoding="utf-8",
        )
        problems = skillctl.translation_content_problems(self.skill_id, "zh-CN")
        self.assertTrue(any("translated link changed or missing" in item for item in problems))

    def test_orphan_translation_file_is_reported(self) -> None:
        (self.translated / "extra.txt").write_text("多余\n", encoding="utf-8")
        problems = skillctl.translation_content_problems(self.skill_id, "zh-CN")
        self.assertTrue(any("orphan translation" in item and "extra.txt" in item for item in problems))

    def test_locale_mirror_is_not_a_discoverable_skill(self) -> None:
        records = skillctl.skill_records()
        self.assertEqual([record["id"] for record in records], [self.skill_id])
        self.assertEqual(skillctl.skill_path(self.skill_id), self.source.resolve())

    def test_orphan_translated_skill_directory_is_reported(self) -> None:
        self.stamp()
        orphan = skillctl.LOCALES_DIR / "zh-CN" / "vendor" / "acme" / "orphan"
        orphan.mkdir(parents=True)
        (orphan / "SKILL.md").write_text("孤立镜像\n", encoding="utf-8")
        problems = skillctl.all_translation_problems("zh-CN")
        self.assertTrue(any("orphan translated skill directory" in item for item in problems))

    def test_placeholder_and_english_copy_are_rejected(self) -> None:
        (self.translated / "SKILL.md").write_text(
            "---\nname: demo\ndescription: 示例技能。\n---\n\n"
            "# 中文导读\n\n# 上游说明原文\n\nRead [guide](guide.md).\n",
            encoding="utf-8",
        )
        (self.translated / "guide.md").write_text(
            "# 中文提示\n\n" + "This English paragraph is still copied and has not been translated. " * 8,
            encoding="utf-8",
        )
        (self.source / "guide.md").write_text(
            "This English paragraph is still copied and has not been translated. " * 8,
            encoding="utf-8",
        )
        problems = skillctl.translation_content_problems(self.skill_id, "zh-CN")
        self.assertTrue(any("placeholder translation content" in item for item in problems))
        self.assertTrue(any("insufficient Chinese translation" in item for item in problems))
        self.assertTrue(any("translation too similar" in item for item in problems))

    def test_folded_front_matter_description_is_parsed(self) -> None:
        meta = skillctl.parse_front_matter(
            "---\nname: demo\ndescription: >\n  中文第一行，\n  中文第二行。\n---\n"
        )
        self.assertEqual(meta["name"], "demo")
        self.assertEqual(meta["description"], "中文第一行， 中文第二行。")

    def test_explicit_dependency_is_included_in_install_order(self) -> None:
        parent_id = "vendor/acme/parent"
        dependency_id = "vendor/acme/child"
        parent = skillctl.skill_path(parent_id)
        dependency = skillctl.skill_path(dependency_id)
        parent.mkdir(parents=True)
        dependency.mkdir(parents=True)
        (parent / "SKILL.md").write_text(
            "---\nname: parent\ndescription: Parent skill.\n---\n",
            encoding="utf-8",
        )
        (dependency / "SKILL.md").write_text(
            "---\nname: child\ndescription: Child skill.\n---\n",
            encoding="utf-8",
        )
        previous = skillctl.EXPLICIT_DEPENDENCIES.get("parent")
        skillctl.EXPLICIT_DEPENDENCIES["parent"] = ("child",)
        self.addCleanup(
            lambda: skillctl.EXPLICIT_DEPENDENCIES.pop("parent", None)
            if previous is None
            else skillctl.EXPLICIT_DEPENDENCIES.__setitem__("parent", previous)
        )

        self.assertEqual(
            skillctl.skill_with_dependencies(parent_id),
            [parent_id, dependency_id],
        )

    def test_root_skill_import_excludes_upstream_git_metadata(self) -> None:
        upstream = skillctl.ROOT / "fixture-repo"
        upstream.mkdir()
        (upstream / "SKILL.md").write_text(
            "---\nname: root-demo\ndescription: Root demo skill.\n---\n",
            encoding="utf-8",
        )
        (upstream / ".git").mkdir()
        (upstream / ".git" / "config").write_text("[core]\n", encoding="utf-8")

        def fake_run(command: list[str]) -> None:
            if command[:2] == ["git", "clone"]:
                shutil.copytree(upstream, Path(command[3]))

        args = SimpleNamespace(
            source="acme-root",
            repo="fixture",
            ref="abc123",
            skill_path=".",
            skill_id="vendor/acme-root/root-demo",
            force=False,
        )
        with patch.object(skillctl, "run", side_effect=fake_run):
            with self.assertRaises(SystemExit):
                skillctl.command_import(args)

        imported = skillctl.skill_path(args.skill_id)
        self.assertTrue((imported / "SKILL.md").exists())
        self.assertFalse((imported / ".git").exists())


if __name__ == "__main__":
    unittest.main()
