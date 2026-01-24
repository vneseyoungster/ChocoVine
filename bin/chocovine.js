#!/usr/bin/env node

import { fileURLToPath } from 'url';
import { dirname, join, resolve } from 'path';
import { existsSync, cpSync, mkdirSync, writeFileSync, readFileSync } from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const packageRoot = resolve(__dirname, '..');

const COLORS = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m',
  red: '\x1b[31m',
};

function log(message, color = '') {
  console.log(`${color}${message}${COLORS.reset}`);
}

function printBanner() {
  log(`
   _____ _                     __     ___
  / ____| |                    \\ \\   / (_)
 | |    | |__   ___   ___ ___   \\ \\ / / _ _ __   ___
 | |    | '_ \\ / _ \\ / __/ _ \\   \\ V / | | '_ \\ / _ \\
 | |____| | | | (_) | (_| (_) |   | |  | | | | |  __/
  \\_____|_| |_|\\___/ \\___\\___/    |_|  |_|_| |_|\\___|

  Stop prompting. Start building.
`, COLORS.magenta);
}

function printHelp() {
  printBanner();
  log('Usage:', COLORS.bright);
  log('  npx chocovine init     Install ChocoVine into current directory');
  log('  npx chocovine help     Show this help message');
  log('');
  log('What it does:', COLORS.bright);
  log('  - Copies .claude/ folder with all agents, commands, and skills');
  log('  - Creates a starter CLAUDE.md if one doesn\'t exist');
  log('  - Sets up your project for the TDD workflow');
  log('');
  log('After installation:', COLORS.bright);
  log('  1. Edit CLAUDE.md with your project details');
  log('  2. Run /project-scan to analyze your codebase');
  log('  3. Use /start [task] to begin building!');
  log('');
}

function init() {
  printBanner();

  const targetDir = process.cwd();
  const claudeDir = join(targetDir, '.claude');
  const sourceClaudeDir = join(packageRoot, '.claude');

  log('Installing ChocoVine...', COLORS.cyan);
  log(`Target: ${targetDir}`, COLORS.blue);
  log('');

  // Check if .claude already exists
  if (existsSync(claudeDir)) {
    log('Warning: .claude directory already exists!', COLORS.yellow);
    log('Backing up to .claude.backup and replacing...', COLORS.yellow);

    const backupDir = join(targetDir, '.claude.backup');
    if (existsSync(backupDir)) {
      cpSync(backupDir, `${backupDir}.${Date.now()}`, { recursive: true });
    }
    cpSync(claudeDir, backupDir, { recursive: true });
  }

  // Copy .claude directory
  log('Copying .claude/ directory...', COLORS.cyan);

  try {
    // Create .claude directory
    mkdirSync(claudeDir, { recursive: true });

    // Copy subdirectories
    const subdirs = ['agents', 'commands', 'hooks', 'rules', 'skills', 'templates'];
    for (const subdir of subdirs) {
      const source = join(sourceClaudeDir, subdir);
      const target = join(claudeDir, subdir);
      if (existsSync(source)) {
        cpSync(source, target, { recursive: true });
        log(`  Copied ${subdir}/`, COLORS.green);
      }
    }

    // Copy individual files
    const files = ['settings.json', 'settings.local.json', 'CLAUDE.md'];
    for (const file of files) {
      const source = join(sourceClaudeDir, file);
      if (existsSync(source)) {
        cpSync(source, join(claudeDir, file));
        log(`  Copied ${file}`, COLORS.green);
      }
    }

  } catch (err) {
    log(`Error copying .claude directory: ${err.message}`, COLORS.red);
    process.exit(1);
  }

  // Create CLAUDE.md if it doesn't exist
  const claudeMdPath = join(targetDir, 'CLAUDE.md');
  if (!existsSync(claudeMdPath)) {
    log('Creating CLAUDE.md template...', COLORS.cyan);

    const claudeMdTemplate = `# Project Context

## Project Overview
- **Name:** ${targetDir.split('/').pop()}
- **Type:** <!-- frontend/backend/fullstack/library/cli -->
- **Description:** <!-- one-line description -->

## Tech Stack
- **Language:** <!-- TypeScript, Python, Go, etc. -->
- **Framework:** <!-- Next.js, FastAPI, etc. -->
- **Runtime:** <!-- Node.js 20, Python 3.11, etc. -->

## Key Paths
| Path | Purpose |
|------|---------|
| \`src/\` | Source code |
| \`tests/\` | Test files |
| \`config/\` | Configuration |

## Commands
\`\`\`bash
# Development
npm run dev

# Build
npm run build

# Test
npm test

# Lint
npm run lint
\`\`\`

## Conventions
- <!-- Add your coding conventions here -->
- <!-- e.g., "Use camelCase for variables" -->
- <!-- e.g., "All API responses use { data, error } format" -->

## Important Notes
- <!-- Any gotchas or important context for AI -->
`;

    writeFileSync(claudeMdPath, claudeMdTemplate);
    log('  Created CLAUDE.md', COLORS.green);
  } else {
    log('CLAUDE.md already exists, skipping...', COLORS.yellow);
  }

  log('');
  log('Installation complete!', COLORS.green + COLORS.bright);
  log('');
  log('Next steps:', COLORS.bright);
  log('  1. Edit CLAUDE.md with your project details', COLORS.cyan);
  log('  2. Run /project-scan to analyze your codebase', COLORS.cyan);
  log('  3. Use /start [task] to begin building!', COLORS.cyan);
  log('');
  log('Quick commands:', COLORS.bright);
  log('  /start [task]        - Full TDD workflow', COLORS.blue);
  log('  /quick-fix [error]   - Fix bugs quickly', COLORS.blue);
  log('  /research:codebase   - Understand existing code', COLORS.blue);
  log('');
}

// Parse arguments
const args = process.argv.slice(2);
const command = args[0];

switch (command) {
  case 'init':
  case 'install':
  case 'i':
    init();
    break;
  case 'help':
  case '--help':
  case '-h':
  case undefined:
    printHelp();
    break;
  default:
    log(`Unknown command: ${command}`, COLORS.red);
    log('Run "npx chocovine help" for usage information.');
    process.exit(1);
}
