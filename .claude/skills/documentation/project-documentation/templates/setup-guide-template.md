# Setup Guide Template

Use this template to create installation and configuration guides.

---

```markdown
# {Project Name} Setup Guide

## Prerequisites

### Required Software

| Software | Version | Check Command | Install Link |
|----------|---------|---------------|--------------|
| {Software 1} | {X.X+} | `{cmd} --version` | [{link}]({url}) |
| {Software 2} | {X.X+} | `{cmd} --version` | [{link}]({url}) |
| {Software 3} | {X.X+} | `{cmd} --version` | [{link}]({url}) |

### System Requirements

- **OS:** {Supported operating systems}
- **RAM:** {Minimum} recommended
- **Disk:** {Minimum} free space
- **Network:** {Requirements}

### Accounts/Access

- [ ] {Account/Access 1}
- [ ] {Account/Access 2}
- [ ] {Account/Access 3}

## Installation

### Step 1: Clone Repository

```bash
git clone {repository-url}
cd {project-name}
```

### Step 2: Install Dependencies

```bash
# Using {package-manager}
{install-command}

# Verify installation
{verify-command}
```

**Troubleshooting:**
- If `{error}`: Run `{fix-command}`
- If `{error}`: Check {what to check}

### Step 3: Configure Environment

```bash
# Copy example configuration
cp .env.example .env

# Edit with your settings
{editor} .env
```

**Required Configuration:**

| Variable | Description | Example |
|----------|-------------|---------|
| `{VAR_1}` | {Description} | `{example}` |
| `{VAR_2}` | {Description} | `{example}` |

**Optional Configuration:**

| Variable | Default | Description |
|----------|---------|-------------|
| `{VAR_3}` | `{default}` | {Description} |
| `{VAR_4}` | `{default}` | {Description} |

### Step 4: Database Setup

{If applicable}

```bash
# Create database
{create-db-command}

# Run migrations
{migration-command}

# Seed with test data (optional)
{seed-command}
```

### Step 5: Start Application

```bash
# Development mode
{dev-command}

# Application should be running at:
# {url}
```

### Step 6: Verify Installation

```bash
# Run health check
curl http://localhost:{port}/health

# Expected response:
# {"status": "ok"}

# Run tests
{test-command}
```

## IDE Setup

### VS Code

**Recommended Extensions:**
- {Extension 1} - {Purpose}
- {Extension 2} - {Purpose}
- {Extension 3} - {Purpose}

**Settings:**
```json
{
  "{setting1}": "{value}",
  "{setting2}": "{value}"
}
```

### {Other IDE}

{IDE-specific setup instructions}

## Development Workflow

### Running Locally

```bash
# Start all services
{start-command}

# Watch mode (auto-reload)
{watch-command}
```

### Running Tests

```bash
# All tests
{test-all-command}

# Unit tests only
{test-unit-command}

# With coverage
{test-coverage-command}
```

### Code Quality

```bash
# Linting
{lint-command}

# Formatting
{format-command}

# Type checking
{type-check-command}
```

## Common Issues

### Issue: {Problem Description}

**Symptoms:**
- {What you see}
- {Error message}

**Cause:** {Why this happens}

**Solution:**
```bash
{fix-commands}
```

---

### Issue: {Problem Description}

**Symptoms:**
- {What you see}

**Cause:** {Why this happens}

**Solution:**
{Step-by-step fix}

## Platform-Specific Notes

### macOS

{macOS-specific instructions or issues}

### Windows

{Windows-specific instructions or issues}

```powershell
# Windows-specific commands
{command}
```

### Linux

{Linux-specific instructions or issues}

## Docker Setup (Optional)

```bash
# Build image
docker build -t {image-name} .

# Run container
docker run -p {port}:{port} {image-name}

# Using docker-compose
docker-compose up -d
```

## Production Deployment

{Brief overview of production deployment}

See [{Deployment Guide}]({link}) for full production setup.

## Getting Help

- **Documentation:** {link}
- **Issues:** {link}
- **Discussions:** {link}
- **Team Contact:** {contact}

## Next Steps

After setup is complete:

1. [ ] Read the [Architecture Overview](architecture/overview.md)
2. [ ] Complete the [Quickstart Tutorial](onboarding/quickstart.md)
3. [ ] Review [Contributing Guidelines](CONTRIBUTING.md)
```

---

## Template Usage Notes

- Test all commands before documenting
- Include version numbers where relevant
- Provide both copy-paste commands and explanations
- Document platform-specific differences
- Include troubleshooting for common issues
- Link to deeper documentation
