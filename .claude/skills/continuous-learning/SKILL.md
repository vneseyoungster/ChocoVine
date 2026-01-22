# Continuous Learning Skill

Automatically extracts reusable patterns from Claude Code sessions.

## Purpose

- Learn from error resolutions and debugging techniques
- Capture project-specific workarounds
- Build a knowledge base of learned skills over time

## Components

- `evaluate-session.sh` - Runs on session end to evaluate for extractable patterns
- `config.json` - Configuration for pattern detection

## How It Works

1. Runs automatically via Stop hook when sessions end
2. Analyzes session transcript for valuable patterns
3. Saves learned skills to `~/.claude/skills/learned/`

## Configuration

Edit `config.json` to customize:

- `min_session_length` - Minimum messages before evaluation (default: 10)
- `patterns_to_detect` - What to look for
- `ignore_patterns` - What to skip
