#!/bin/bash
# Dependency Audit Script
# Usage: ./audit-deps.sh [package-manager]

set -e

detect_package_manager() {
    if [ -f "package-lock.json" ] || [ -f "yarn.lock" ] || [ -f "pnpm-lock.yaml" ]; then
        echo "node"
    elif [ -f "requirements.txt" ] || [ -f "Pipfile.lock" ] || [ -f "poetry.lock" ]; then
        echo "python"
    elif [ -f "go.mod" ]; then
        echo "go"
    else
        echo "unknown"
    fi
}

audit_node() {
    echo "=== Node.js Dependency Audit ==="

    if [ -f "package-lock.json" ]; then
        echo "Using npm..."
        npm audit 2>/dev/null || true
        echo ""
        echo "=== Outdated Packages ==="
        npm outdated 2>/dev/null || true
    elif [ -f "yarn.lock" ]; then
        echo "Using yarn..."
        yarn audit 2>/dev/null || true
        echo ""
        echo "=== Outdated Packages ==="
        yarn outdated 2>/dev/null || true
    elif [ -f "pnpm-lock.yaml" ]; then
        echo "Using pnpm..."
        pnpm audit 2>/dev/null || true
        echo ""
        echo "=== Outdated Packages ==="
        pnpm outdated 2>/dev/null || true
    fi
}

audit_python() {
    echo "=== Python Dependency Audit ==="

    if command -v pip-audit &> /dev/null; then
        pip-audit 2>/dev/null || true
    else
        echo "pip-audit not installed. Install with: pip install pip-audit"
    fi

    echo ""
    echo "=== Outdated Packages ==="
    pip list --outdated 2>/dev/null || true
}

audit_go() {
    echo "=== Go Dependency Audit ==="

    if command -v govulncheck &> /dev/null; then
        govulncheck ./... 2>/dev/null || true
    else
        echo "govulncheck not installed. Install with: go install golang.org/x/vuln/cmd/govulncheck@latest"
    fi

    echo ""
    echo "=== Module Updates Available ==="
    go list -u -m all 2>/dev/null | grep '\[' || echo "All modules up to date"
}

# Main execution
PM=${1:-$(detect_package_manager)}

echo "Detected package manager: $PM"
echo "================================"
echo ""

case $PM in
    node)
        audit_node
        ;;
    python)
        audit_python
        ;;
    go)
        audit_go
        ;;
    *)
        echo "Unknown or unsupported package manager"
        echo "Supported: node, python, go"
        exit 1
        ;;
esac

echo ""
echo "=== Audit Complete ==="
