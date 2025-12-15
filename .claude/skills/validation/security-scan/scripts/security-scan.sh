#!/bin/bash

# Security Scan Script
# Run this script to perform automated security checks

set -e

echo "========================================="
echo "Starting Security Scan"
echo "========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track overall status
ISSUES_FOUND=0

# Function to print status
print_status() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}[PASS]${NC} $2"
    else
        echo -e "${RED}[FAIL]${NC} $2"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

# =========================================
# 1. Dependency Audit
# =========================================
echo "1. Checking Dependencies for Vulnerabilities..."
echo "-------------------------------------------"

# Node.js (npm)
if [ -f "package.json" ]; then
    echo "Running npm audit..."
    npm audit --json > /tmp/npm-audit.json 2>/dev/null || true

    VULN_COUNT=$(cat /tmp/npm-audit.json | grep -o '"vulnerabilities":' | wc -l || echo "0")

    if npm audit 2>/dev/null; then
        print_status 0 "npm audit - No vulnerabilities found"
    else
        print_status 1 "npm audit - Vulnerabilities detected"
        echo "   Run 'npm audit' for details"
    fi
fi

# Python (pip)
if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
    if command -v pip-audit &> /dev/null; then
        echo "Running pip-audit..."
        if pip-audit 2>/dev/null; then
            print_status 0 "pip-audit - No vulnerabilities found"
        else
            print_status 1 "pip-audit - Vulnerabilities detected"
        fi
    else
        print_warning "pip-audit not installed. Run: pip install pip-audit"
    fi
fi

# Go
if [ -f "go.mod" ]; then
    if command -v govulncheck &> /dev/null; then
        echo "Running govulncheck..."
        if govulncheck ./... 2>/dev/null; then
            print_status 0 "govulncheck - No vulnerabilities found"
        else
            print_status 1 "govulncheck - Vulnerabilities detected"
        fi
    else
        print_warning "govulncheck not installed. Run: go install golang.org/x/vuln/cmd/govulncheck@latest"
    fi
fi

echo ""

# =========================================
# 2. Secret Detection
# =========================================
echo "2. Scanning for Hardcoded Secrets..."
echo "-------------------------------------------"

# Check for common secret patterns
SECRET_PATTERNS=(
    "password\s*=\s*['\"][^'\"]+['\"]"
    "api_key\s*=\s*['\"][^'\"]+['\"]"
    "secret\s*=\s*['\"][^'\"]+['\"]"
    "token\s*=\s*['\"][^'\"]+['\"]"
    "AWS_ACCESS_KEY_ID"
    "AWS_SECRET_ACCESS_KEY"
    "PRIVATE_KEY"
)

SECRETS_FOUND=0
for pattern in "${SECRET_PATTERNS[@]}"; do
    MATCHES=$(grep -rni "$pattern" --include="*.js" --include="*.ts" --include="*.py" --include="*.go" --include="*.java" --include="*.json" --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=vendor . 2>/dev/null | grep -v ".env.example" | grep -v "test" | head -5)
    if [ -n "$MATCHES" ]; then
        echo -e "${RED}Potential secrets found:${NC}"
        echo "$MATCHES"
        SECRETS_FOUND=1
    fi
done

if [ $SECRETS_FOUND -eq 0 ]; then
    print_status 0 "No obvious hardcoded secrets found"
else
    print_status 1 "Potential hardcoded secrets detected"
fi

# Use secretlint if available
if command -v npx &> /dev/null && [ -f "package.json" ]; then
    if npm list secretlint 2>/dev/null | grep -q secretlint; then
        echo "Running secretlint..."
        if npx secretlint "**/*" 2>/dev/null; then
            print_status 0 "secretlint - No secrets found"
        else
            print_status 1 "secretlint - Secrets detected"
        fi
    fi
fi

echo ""

# =========================================
# 3. Security Linting
# =========================================
echo "3. Running Security Linters..."
echo "-------------------------------------------"

# ESLint with security plugin (Node.js)
if [ -f "package.json" ]; then
    if npm list eslint-plugin-security 2>/dev/null | grep -q eslint-plugin-security; then
        echo "Running ESLint with security plugin..."
        if npx eslint --plugin security --rule 'security/detect-eval-with-expression: error' . 2>/dev/null; then
            print_status 0 "ESLint security - No issues"
        else
            print_status 1 "ESLint security - Issues detected"
        fi
    else
        print_warning "eslint-plugin-security not installed"
    fi
fi

# Bandit (Python)
if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
    if command -v bandit &> /dev/null; then
        echo "Running Bandit..."
        if bandit -r . -x ./venv,./tests 2>/dev/null; then
            print_status 0 "Bandit - No issues"
        else
            print_status 1 "Bandit - Issues detected"
        fi
    else
        print_warning "Bandit not installed. Run: pip install bandit"
    fi
fi

echo ""

# =========================================
# 4. File Permission Check
# =========================================
echo "4. Checking File Permissions..."
echo "-------------------------------------------"

# Check for world-writable files
WORLD_WRITABLE=$(find . -type f -perm -002 -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null)
if [ -n "$WORLD_WRITABLE" ]; then
    print_status 1 "World-writable files found"
    echo "$WORLD_WRITABLE"
else
    print_status 0 "No world-writable files"
fi

# Check for files with sensitive names
SENSITIVE_FILES=$(find . -name ".env" -o -name "*.pem" -o -name "*.key" -o -name "*credentials*" -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null | grep -v ".example")
if [ -n "$SENSITIVE_FILES" ]; then
    print_warning "Potentially sensitive files found:"
    echo "$SENSITIVE_FILES"
fi

echo ""

# =========================================
# 5. Git Security Check
# =========================================
echo "5. Checking Git Security..."
echo "-------------------------------------------"

# Check if .gitignore exists
if [ -f ".gitignore" ]; then
    print_status 0 ".gitignore exists"

    # Check if common sensitive patterns are ignored
    PATTERNS_TO_CHECK=(".env" "*.pem" "*.key" "node_modules" "*.log")
    for pattern in "${PATTERNS_TO_CHECK[@]}"; do
        if grep -q "$pattern" .gitignore 2>/dev/null; then
            print_status 0 "$pattern is in .gitignore"
        else
            print_warning "$pattern should be in .gitignore"
        fi
    done
else
    print_status 1 ".gitignore missing"
fi

echo ""

# =========================================
# Summary
# =========================================
echo "========================================="
echo "Security Scan Complete"
echo "========================================="
if [ $ISSUES_FOUND -eq 0 ]; then
    echo -e "${GREEN}No critical issues found${NC}"
    exit 0
else
    echo -e "${RED}$ISSUES_FOUND issue(s) require attention${NC}"
    exit 1
fi
