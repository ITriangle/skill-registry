from __future__ import annotations

import importlib.machinery
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


REGCTL_PATH = Path(__file__).resolve().parents[1] / "bin" / "regctl"
regctl = importlib.machinery.SourceFileLoader("regctl_test_module", str(REGCTL_PATH)).load_module()


class AssetManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        regctl.ROOT = root
        regctl.PROJECTS_DIR = root / "projects"
        regctl.SOURCES_DIR = root / "sources"
        regctl.SKILLS_DIR = root / "skills"
        regctl.RULES_DIR = root / "rules"
        regctl.ANALYSIS_DIR = root / "analysis"
        regctl.GROUPS_FILE = root / "skill-groups.yaml"
        regctl.GLOBALS_FILE = root / "globals.yaml"
        regctl.LOCALES_DIR = root / "locales"
        self.home = root / "home"
        self.home.mkdir()
        self.codex_home = self.home / ".codex"
        self.codex_home.mkdir()
        self.cursor_rules = self.home / ".cursor" / "rules"
        self.claude_home = self.home / ".claude"
        (self.codex_home / "AGENTS.md").write_text("", encoding="utf-8")

        self.skill_id = "vendor/acme/demo"
        skill_dir = root / "skills" / "vendor" / "acme" / "demo"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: demo\ndescription: Demo skill.\n---\n\nDo the demo.\n",
            encoding="utf-8",
        )
        translated = root / "locales" / "zh-CN" / "vendor" / "acme" / "demo"
        translated.mkdir(parents=True)
        (translated / "SKILL.md").write_text(
            "---\nname: demo\ndescription: 示例技能。\n---\n\n做示例。\n",
            encoding="utf-8",
        )
        (translated / ".translation.yaml").write_text(
            regctl.dump_translation_manifest(self.skill_id, "zh-CN"),
            encoding="utf-8",
        )

        self.apply_id = "vendor/acme/always-on"
        self.skip_id = "vendor/acme/file-names"
        self._write_rule(
            self.apply_id,
            "always-on",
            True,
            "每次任务先确认问题可验收。",
        )
        self._write_rule(
            self.skip_id,
            "file-names",
            False,
            "文件名只用能力短名。",
        )

        (root / "publish" / "codex").mkdir(parents=True)
        self.codex_source = root / "publish" / "codex" / "AGENTS.md"
        self.codex_source.write_text("", encoding="utf-8")
        (root / "globals.yaml").write_text(
            "globals:\n"
            "  - id: codex-agents\n"
            "    kind: agents-md\n"
            "    agent: codex\n"
            "    path: publish/codex/AGENTS.md\n",
            encoding="utf-8",
        )
        (root / "sources").mkdir()
        (root / "sources" / "acme.yaml").write_text(
            "source: acme\n"
            "skills:\n"
            "  - id: vendor/acme/demo\n"
            "    status: candidate\n"
            "rules:\n"
            "  - id: vendor/acme/always-on\n"
            "    status: candidate\n"
            "  - id: vendor/acme/file-names\n"
            "    status: candidate\n",
            encoding="utf-8",
        )
        (root / "projects").mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _write_rule(self, rule_id: str, name: str, always: bool, body: str) -> None:
        rule_dir = regctl.ROOT / "rules" / rule_id
        rule_dir.mkdir(parents=True)
        text = (
            "---\n"
            f"description: {body}\n"
            f"alwaysApply: {'true' if always else 'false'}\n"
            "---\n\n"
            f"# {name}\n\n{body}\n"
        )
        (rule_dir / "RULE.mdc").write_text(text, encoding="utf-8")
        translated = regctl.ROOT / "locales" / "zh-CN" / rule_id
        translated.mkdir(parents=True)
        (translated / "RULE.mdc").write_text(text, encoding="utf-8")
        (translated / ".translation.yaml").write_text(
            regctl.dump_translation_manifest(rule_id, "zh-CN"),
            encoding="utf-8",
        )

    def _write_user_home(self, skills: list[str], rules: list[str] | None = None) -> None:
        (regctl.PROJECTS_DIR / "user-home.yaml").write_text(
            regctl.dump_project_manifest(
                "user-home",
                str(self.home),
                skills,
                rules,
                {
                    "skills": str(self.home / ".agents" / "skills"),
                    "cursor_rules": str(self.cursor_rules),
                    "codex_agents": str(self.codex_home / "AGENTS.md"),
                    "claude_agents": str(self.claude_home / "CLAUDE.md"),
                },
            ),
            encoding="utf-8",
        )

    def _write_git_project(self) -> Path:
        repo = Path(self.tmp.name) / "repo"
        repo.mkdir()
        (regctl.PROJECTS_DIR / "repo.yaml").write_text(
            regctl.dump_project_manifest("repo", str(repo), [self.skill_id]),
            encoding="utf-8",
        )
        return repo

    def test_dump_keeps_skills_rules_and_adapters(self) -> None:
        text = regctl.dump_project_manifest(
            "user-home",
            str(self.home),
            [self.skill_id],
            [self.apply_id],
            {"codex_agents": "~/.codex/AGENTS.md", "cursor_rules": "~/.cursor/rules"},
        )
        self.assertIn("adapters:", text)
        self.assertIn("codex_agents: ~/.codex/AGENTS.md", text)
        self.assertIn(f"- id: {self.skill_id}", text)
        self.assertIn(f"- id: {self.apply_id}", text)
        path = Path(self.tmp.name) / "manifest.yaml"
        path.write_text(text, encoding="utf-8")
        parsed = regctl.parse_simple_yaml(path)
        self.assertEqual(parsed["adapters"]["codex_agents"], "~/.codex/AGENTS.md")

    def test_enable_skill_does_not_drop_rules(self) -> None:
        self._write_user_home([], [self.apply_id])
        args = SimpleNamespace(project="user-home", asset=self.skill_id, source=None, kind="skill")
        regctl.command_enable(args)
        data = regctl.load_project("user-home")
        self.assertEqual(regctl.project_skill_ids(data), [self.skill_id])
        self.assertEqual(regctl.project_rule_ids(data), [self.apply_id])
        self.assertIn("codex_agents", regctl.project_adapters(data))

    def test_enable_rule_on_git_project_fails(self) -> None:
        self._write_git_project()
        with self.assertRaises(regctl.RegistryError):
            regctl.command_enable(
                SimpleNamespace(project="repo", asset=self.apply_id, source=None, kind="rule")
            )
        repo = Path(self.tmp.name) / "repo"
        self.assertFalse((repo / "AGENTS.md").exists())

    def test_sync_git_project_does_not_write_agents_md(self) -> None:
        repo = self._write_git_project()
        regctl.command_sync(SimpleNamespace(project="repo", allow_candidate=True, dry_run=False))
        self.assertFalse((repo / "AGENTS.md").exists())
        self.assertFalse((repo / ".cursor").exists())
        self.assertFalse((repo / "CLAUDE.md").exists())

    def test_sync_global_adapters(self) -> None:
        self._write_user_home([self.skill_id], [self.apply_id, self.skip_id])
        regctl.command_sync(SimpleNamespace(project="user-home", allow_candidate=True, dry_run=False))
        agents = self.codex_home / "AGENTS.md"
        self.assertTrue(agents.is_symlink())
        self.assertEqual(agents.resolve(), self.codex_source.resolve())
        self.assertEqual(agents.read_text(encoding="utf-8"), "")
        cursor = self.cursor_rules / "always-on.mdc"
        self.assertTrue(cursor.is_symlink())
        claude = (self.claude_home / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertIn("每次任务先确认问题可验收", claude)
        self.assertNotIn("文件名只用能力短名", claude)
        self.assertFalse((Path(self.tmp.name) / "repo" / "AGENTS.md").exists())

    def test_refuse_nonempty_unmanaged_codex_file(self) -> None:
        (self.codex_home / "AGENTS.md").write_text("keep me\n", encoding="utf-8")
        self._write_user_home([], [self.apply_id])
        with self.assertRaises(SystemExit):
            regctl.command_sync(SimpleNamespace(project="user-home", allow_candidate=True, dry_run=False))

    def test_override_warns(self) -> None:
        import io
        from contextlib import redirect_stderr

        (self.codex_home / "AGENTS.override.md").write_text("override\n", encoding="utf-8")
        self._write_user_home([], [self.apply_id])
        buf = io.StringIO()
        with redirect_stderr(buf):
            regctl.command_audit(SimpleNamespace(project="user-home", allow_candidate=True))
        self.assertIn("override", buf.getvalue())
