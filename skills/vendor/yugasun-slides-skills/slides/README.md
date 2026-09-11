# Interactive HTML Slide Generator

Generate high-quality, single-file HTML interactive slide decks. Use this skill when you need to create a presentation, slide deck, or PPT.

## Overview

This skill acts as an expert Frontend Developer and Presentation Designer to generate "Keynote-quality" HTML presentations. It supports **two workflows**:

1. **Beautiful HTML Templates** (recommended): 32 professionally-designed templates from [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates). The agent asks about your occasion and mood, presents 3 candidates, then builds from real template HTML/CSS.
2. **Built-in CSS Themes**: 4 self-contained themes (Cyberpunk, Corporate, Minimal, Nature) for fast, lightweight output.

## Features

- **Single-file Output**: All CSS, JS, and HTML bundled into one file
- **Interactive**: Keyboard/click navigation with progress bar
- **Responsive**: Vertical scroll on mobile, single slide on desktop
- **32 Beautiful Templates**: Professionally designed, visually distinctive
- **4 Built-in Themes**: Cyberpunk, Corporate, Minimal, Nature

## Usage

When asking the agent to create slides, specify your **occasion** and **mood/vibe**. The agent will:

1. **Clarify taste**: Ask about occasion and preferred mood
2. **Present candidates**: Show 3 matching templates with live previews
3. **Build**: Create a polished HTML deck from the chosen template
4. **Deliver**: Open the deck in your browser

Or simply specify a theme (Cyberpunk/Corporate/Minimal/Nature) for a faster, self-contained output.

## Template Library

The `beautiful-html-templates/` directory contains 32 curated HTML slide templates. See `beautiful-html-templates/index.json` for full metadata (mood, tone, formality, density, best_for).

Key templates:
- **Soft Editorial**: Cormorant Garamond serif on warm paper
- **8-Bit Orbit**: Pixel-art neon arcade aesthetic
- **Studio**: Black canvas with electric yellow type
- **Grove**: Forest-green with classical Playfair serifs
- **Signal**: Deep navy with muted-gold accent
- **Daisy Days**: Cheerful pastel with hand-drawn elements

## Directory Structure

- `SKILL.md`: Main skill definition and instructions
- `examples/`: Example outputs
- `templates/`: Base template + scripts + layouts (for Workflow B)
- `themes/`: CSS theme files (for Workflow B)
- `beautiful-html-templates/`: 32 HTML slide template library
  - `index.json`: Template metadata and matching guide
  - `AGENTS.md`: Full agent operating manual
  - `templates/<slug>/template.html`: Template HTML file
