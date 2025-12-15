#!/usr/bin/env python3
"""
Task Validation Utility

Validates implementation plan documents for completeness and consistency.
Used to ensure task breakdown meets quality standards before implementation.

Usage:
    python generate-tasks.py <implementation-plan.md>
    python generate-tasks.py docs/plans/implementation-auth.md
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class TaskSize(Enum):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"  # Should be flagged for breakdown


class Priority(Enum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"


@dataclass
class Task:
    """Represents a single task from the implementation plan."""
    id: str
    name: str
    priority: Optional[Priority]
    size: Optional[TaskSize]
    dependencies: List[str]
    has_file_operations: bool
    has_verification: bool
    has_commit_message: bool
    line_number: int


@dataclass
class ValidationResult:
    """Result of validating an implementation plan."""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    tasks: List[Task]
    stats: dict


def parse_task(content: str, start_line: int) -> Optional[Task]:
    """Parse a task block from markdown content."""

    # Extract task ID and name
    task_match = re.search(r'###\s+Task\s+(\d+\.\d+):\s+(.+)', content)
    if not task_match:
        return None

    task_id = task_match.group(1)
    task_name = task_match.group(2).strip()

    # Extract priority
    priority = None
    priority_match = re.search(r'\*\*Priority:\*\*\s*(P[1-4])', content)
    if priority_match:
        priority = Priority(priority_match.group(1))

    # Extract size
    size = None
    size_match = re.search(r'\*\*Size:\*\*\s*(XS|S|M|L|XL)', content)
    if size_match:
        size = TaskSize(size_match.group(1))

    # Extract dependencies
    dependencies = []
    dep_match = re.search(r'\*\*Dependencies:\*\*\s*(.+)', content)
    if dep_match:
        dep_text = dep_match.group(1)
        if dep_text.lower() != 'none':
            dep_refs = re.findall(r'Task\s+(\d+\.\d+)', dep_text)
            dependencies = dep_refs

    # Check for file operations table
    has_file_operations = '| Action |' in content or '| CREATE |' in content or '| MODIFY |' in content

    # Check for verification section
    has_verification = '### Verification' in content or '```bash' in content

    # Check for commit message
    has_commit_message = '### Commit' in content or 'feat(' in content or 'fix(' in content

    return Task(
        id=task_id,
        name=task_name,
        priority=priority,
        size=size,
        dependencies=dependencies,
        has_file_operations=has_file_operations,
        has_verification=has_verification,
        has_commit_message=has_commit_message,
        line_number=start_line
    )


def parse_implementation_plan(filepath: Path) -> List[Task]:
    """Parse all tasks from an implementation plan document."""
    content = filepath.read_text()
    tasks = []

    # Split by task headers
    task_pattern = r'(###\s+Task\s+\d+\.\d+:.+?)(?=###\s+Task\s+\d+\.\d+:|---\s*$|##\s+Phase|##\s+Validation|$)'
    matches = re.finditer(task_pattern, content, re.DOTALL)

    for match in matches:
        task_content = match.group(1)
        # Estimate line number
        line_number = content[:match.start()].count('\n') + 1
        task = parse_task(task_content, line_number)
        if task:
            tasks.append(task)

    return tasks


def validate_tasks(tasks: List[Task]) -> ValidationResult:
    """Validate a list of tasks for completeness and consistency."""
    errors = []
    warnings = []
    task_ids = {t.id for t in tasks}

    for task in tasks:
        # Check for XL tasks (should be broken down)
        if task.size == TaskSize.XL:
            errors.append(f"Task {task.id}: Size XL - must be broken down into smaller tasks")

        # Check for missing priority
        if task.priority is None:
            warnings.append(f"Task {task.id}: Missing priority")

        # Check for missing size
        if task.size is None:
            warnings.append(f"Task {task.id}: Missing size estimate")

        # Check for file operations
        if not task.has_file_operations:
            warnings.append(f"Task {task.id}: No file operations specified")

        # Check for verification
        if not task.has_verification:
            errors.append(f"Task {task.id}: Missing verification commands")

        # Check for commit message
        if not task.has_commit_message:
            warnings.append(f"Task {task.id}: No commit message template")

        # Check dependencies exist
        for dep_id in task.dependencies:
            if dep_id not in task_ids:
                errors.append(f"Task {task.id}: Dependency {dep_id} not found")

    # Check for circular dependencies (simple check)
    # A more thorough check would use graph algorithms
    for task in tasks:
        if task.id in task.dependencies:
            errors.append(f"Task {task.id}: Self-referencing dependency")

    # Calculate stats
    stats = {
        'total_tasks': len(tasks),
        'p1_tasks': sum(1 for t in tasks if t.priority == Priority.P1),
        'p2_tasks': sum(1 for t in tasks if t.priority == Priority.P2),
        'p3_tasks': sum(1 for t in tasks if t.priority == Priority.P3),
        'p4_tasks': sum(1 for t in tasks if t.priority == Priority.P4),
        'xs_tasks': sum(1 for t in tasks if t.size == TaskSize.XS),
        's_tasks': sum(1 for t in tasks if t.size == TaskSize.S),
        'm_tasks': sum(1 for t in tasks if t.size == TaskSize.M),
        'l_tasks': sum(1 for t in tasks if t.size == TaskSize.L),
        'xl_tasks': sum(1 for t in tasks if t.size == TaskSize.XL),
    }

    is_valid = len(errors) == 0

    return ValidationResult(
        is_valid=is_valid,
        errors=errors,
        warnings=warnings,
        tasks=tasks,
        stats=stats
    )


def print_report(result: ValidationResult, filepath: Path):
    """Print validation report to console."""
    print(f"\n{'='*60}")
    print(f"Task Validation Report: {filepath.name}")
    print(f"{'='*60}\n")

    # Stats
    print("📊 Statistics:")
    print(f"   Total Tasks: {result.stats['total_tasks']}")
    print(f"   By Priority: P1={result.stats['p1_tasks']}, P2={result.stats['p2_tasks']}, "
          f"P3={result.stats['p3_tasks']}, P4={result.stats['p4_tasks']}")
    print(f"   By Size: XS={result.stats['xs_tasks']}, S={result.stats['s_tasks']}, "
          f"M={result.stats['m_tasks']}, L={result.stats['l_tasks']}, XL={result.stats['xl_tasks']}")

    # Errors
    if result.errors:
        print(f"\n❌ Errors ({len(result.errors)}):")
        for error in result.errors:
            print(f"   • {error}")

    # Warnings
    if result.warnings:
        print(f"\n⚠️  Warnings ({len(result.warnings)}):")
        for warning in result.warnings:
            print(f"   • {warning}")

    # Result
    print(f"\n{'='*60}")
    if result.is_valid:
        print("✅ Validation PASSED - Plan is ready for implementation")
    else:
        print("❌ Validation FAILED - Please fix errors before implementing")
    print(f"{'='*60}\n")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python generate-tasks.py <implementation-plan.md>")
        print("Example: python generate-tasks.py docs/plans/implementation-auth.md")
        sys.exit(1)

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    if not filepath.suffix == '.md':
        print(f"Warning: Expected markdown file, got: {filepath.suffix}")

    # Parse and validate
    tasks = parse_implementation_plan(filepath)

    if not tasks:
        print(f"No tasks found in {filepath}")
        print("Make sure tasks follow the format: ### Task X.Y: Task Name")
        sys.exit(1)

    result = validate_tasks(tasks)
    print_report(result, filepath)

    # Exit with appropriate code
    sys.exit(0 if result.is_valid else 1)


if __name__ == '__main__':
    main()
