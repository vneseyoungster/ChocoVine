#!/usr/bin/env python3
"""
Requirements Validation Script

Validates that requirements documents meet quality criteria before
proceeding to the planning phase.

Usage:
    python validate-requirements.py <session-id>
    python validate-requirements.py <session-id> --verbose
    python validate-requirements.py <session-id> --json

Exit Codes:
    0 - All validations passed
    1 - Validation errors found
    2 - File not found or parse error
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class ValidationResult:
    """Holds validation results for reporting."""

    def __init__(self):
        self.errors: list[dict[str, Any]] = []
        self.warnings: list[dict[str, Any]] = []
        self.info: list[dict[str, Any]] = []
        self.stats: dict[str, Any] = {}

    def add_error(self, category: str, message: str, details: str = ""):
        self.errors.append({
            "category": category,
            "message": message,
            "details": details,
            "severity": "error"
        })

    def add_warning(self, category: str, message: str, details: str = ""):
        self.warnings.append({
            "category": category,
            "message": message,
            "details": details,
            "severity": "warning"
        })

    def add_info(self, category: str, message: str, details: str = ""):
        self.info.append({
            "category": category,
            "message": message,
            "details": details,
            "severity": "info"
        })

    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.is_valid(),
            "timestamp": datetime.now().isoformat(),
            "stats": self.stats,
            "errors": self.errors,
            "warnings": self.warnings,
            "info": self.info
        }


def find_docs_root() -> Path:
    """Find the docs directory relative to script location."""
    script_dir = Path(__file__).resolve().parent
    # Navigate up to project root: scripts -> requirement-clarification -> questioning -> skills -> .claude -> project
    project_root = script_dir.parent.parent.parent.parent.parent
    docs_dir = project_root / "docs"

    if not docs_dir.exists():
        # Try current working directory
        cwd_docs = Path.cwd() / "docs"
        if cwd_docs.exists():
            return cwd_docs

    return docs_dir


def read_file_content(filepath: Path) -> str | None:
    """Read file content, return None if not found."""
    try:
        return filepath.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
        return None


def parse_questions_document(content: str) -> dict[str, Any]:
    """Parse questions document and extract question data."""
    result = {
        "blocking_questions": [],
        "important_questions": [],
        "optional_questions": [],
        "total_questions": 0
    }

    current_section = None
    current_question = None

    for line in content.split("\n"):
        line = line.strip()

        # Detect section headers
        if "Must Answer" in line or "Blocking" in line:
            current_section = "blocking"
        elif "Should Answer" in line or "Important" in line:
            current_section = "important"
        elif "Could Answer" in line or "Nice to Have" in line:
            current_section = "optional"

        # Detect question (lines starting with Q or ### Q)
        question_match = re.match(r'^(?:###\s*)?Q\d*[:\s]*(.+)', line)
        if question_match:
            question_text = question_match.group(1).strip()
            current_question = {
                "text": question_text,
                "has_impact": False,
                "has_default": False,
                "has_answer": False
            }
            if current_section == "blocking":
                result["blocking_questions"].append(current_question)
            elif current_section == "important":
                result["important_questions"].append(current_question)
            else:
                result["optional_questions"].append(current_question)
            result["total_questions"] += 1

        # Check for impact, default, answer markers
        if current_question:
            if line.lower().startswith("- **impact"):
                current_question["has_impact"] = True
            elif line.lower().startswith("- **default"):
                current_question["has_default"] = True
            elif line.lower().startswith("- **answer") or line.lower().startswith("**answer"):
                current_question["has_answer"] = True

    return result


def parse_requirements_document(content: str) -> dict[str, Any]:
    """Parse requirements document and extract requirement data."""
    result = {
        "functional_requirements": [],
        "non_functional_requirements": [],
        "acceptance_criteria": [],
        "assumptions": [],
        "out_of_scope": [],
        "has_status": False,
        "status": None
    }

    current_section = None

    # Check for status
    status_match = re.search(r'\*\*Status:\*\*\s*(\w+)', content)
    if status_match:
        result["has_status"] = True
        result["status"] = status_match.group(1)

    for line in content.split("\n"):
        line = line.strip()

        # Detect section headers
        if "Functional Requirements" in line and "Non" not in line:
            current_section = "functional"
        elif "Non-Functional Requirements" in line:
            current_section = "non_functional"
        elif "Acceptance Criteria" in line:
            current_section = "acceptance"
        elif "Assumptions" in line:
            current_section = "assumptions"
        elif "Out of Scope" in line:
            current_section = "out_of_scope"

        # Detect requirements (table rows with FR- or NFR- IDs)
        req_match = re.match(r'\|\s*(FR-\d+|NFR-\d+)\s*\|(.+)\|', line)
        if req_match:
            req_id = req_match.group(1)
            req_data = req_match.group(2).strip()
            if req_id.startswith("FR-"):
                result["functional_requirements"].append({
                    "id": req_id,
                    "data": req_data
                })
            else:
                result["non_functional_requirements"].append({
                    "id": req_id,
                    "data": req_data
                })

        # Detect acceptance criteria (checkbox items)
        criteria_match = re.match(r'^-\s*\[[ x]\]\s*(.+)', line)
        if criteria_match and current_section == "acceptance":
            result["acceptance_criteria"].append(criteria_match.group(1))

        # Detect assumptions (numbered or bulleted lists)
        assumption_match = re.match(r'^(?:\d+\.|-)\s*(.+)', line)
        if assumption_match and current_section == "assumptions":
            result["assumptions"].append(assumption_match.group(1))

        # Detect out of scope items
        oos_match = re.match(r'^-\s*(.+)', line)
        if oos_match and current_section == "out_of_scope":
            result["out_of_scope"].append(oos_match.group(1))

    return result


def validate_blocking_questions_answered(
    questions_data: dict[str, Any],
    result: ValidationResult
) -> None:
    """Check that all blocking questions have answers."""
    blocking = questions_data.get("blocking_questions", [])
    unanswered = [q for q in blocking if not q.get("has_answer")]

    result.stats["blocking_questions_total"] = len(blocking)
    result.stats["blocking_questions_answered"] = len(blocking) - len(unanswered)

    if unanswered:
        result.add_error(
            "blocking_questions",
            f"{len(unanswered)} blocking questions remain unanswered",
            "; ".join(q["text"][:50] + "..." for q in unanswered[:3])
        )
    else:
        result.add_info(
            "blocking_questions",
            f"All {len(blocking)} blocking questions answered"
        )


def validate_questions_have_defaults(
    questions_data: dict[str, Any],
    result: ValidationResult
) -> None:
    """Check that all blocking questions have default assumptions."""
    blocking = questions_data.get("blocking_questions", [])
    no_default = [q for q in blocking if not q.get("has_default")]

    if no_default:
        result.add_warning(
            "defaults",
            f"{len(no_default)} blocking questions lack default assumptions",
            "; ".join(q["text"][:50] + "..." for q in no_default[:3])
        )


def validate_no_contradictions(
    requirements_data: dict[str, Any],
    result: ValidationResult
) -> None:
    """Check for potentially contradictory requirements."""
    all_reqs = (
        requirements_data.get("functional_requirements", []) +
        requirements_data.get("non_functional_requirements", [])
    )

    # Simple contradiction detection: look for opposing keywords
    contradiction_pairs = [
        ("sync", "async"),
        ("real-time", "batch"),
        ("public", "private"),
        ("required", "optional"),
        ("encrypted", "plain"),
        ("cached", "fresh"),
    ]

    found_contradictions = []
    for i, req1 in enumerate(all_reqs):
        for req2 in all_reqs[i + 1:]:
            text1 = req1.get("data", "").lower()
            text2 = req2.get("data", "").lower()

            for word1, word2 in contradiction_pairs:
                if (word1 in text1 and word2 in text2) or \
                   (word2 in text1 and word1 in text2):
                    found_contradictions.append(
                        f"{req1['id']} vs {req2['id']}: {word1}/{word2}"
                    )

    if found_contradictions:
        result.add_warning(
            "contradictions",
            f"Potential contradictions found: {len(found_contradictions)}",
            "; ".join(found_contradictions[:3])
        )
    else:
        result.add_info("contradictions", "No obvious contradictions detected")


def validate_technical_feasibility(
    requirements_data: dict[str, Any],
    result: ValidationResult
) -> None:
    """Check for technical feasibility markers."""
    # Check if there's a technical constraints section with content
    has_constraints = bool(requirements_data.get("assumptions"))

    if not has_constraints:
        result.add_warning(
            "feasibility",
            "No technical constraints or assumptions documented",
            "Consider documenting technical limitations discovered during research"
        )
    else:
        result.add_info(
            "feasibility",
            f"Found {len(requirements_data['assumptions'])} documented assumptions/constraints"
        )


def validate_confidence_levels(
    requirements_data: dict[str, Any],
    result: ValidationResult
) -> None:
    """Check that requirements have confidence/priority indicators."""
    all_reqs = (
        requirements_data.get("functional_requirements", []) +
        requirements_data.get("non_functional_requirements", [])
    )

    priority_keywords = ["must have", "should have", "could have", "won't have",
                         "high", "medium", "low", "critical"]

    reqs_without_priority = []
    for req in all_reqs:
        data = req.get("data", "").lower()
        has_priority = any(kw in data for kw in priority_keywords)
        if not has_priority:
            reqs_without_priority.append(req["id"])

    result.stats["requirements_total"] = len(all_reqs)
    result.stats["requirements_with_priority"] = len(all_reqs) - len(reqs_without_priority)

    if reqs_without_priority and len(reqs_without_priority) > len(all_reqs) / 2:
        result.add_warning(
            "priority",
            f"{len(reqs_without_priority)} requirements lack priority indicators",
            f"IDs: {', '.join(reqs_without_priority[:5])}"
        )


def validate_acceptance_criteria(
    requirements_data: dict[str, Any],
    result: ValidationResult
) -> None:
    """Check for acceptance criteria coverage."""
    functional_reqs = requirements_data.get("functional_requirements", [])
    criteria = requirements_data.get("acceptance_criteria", [])

    result.stats["acceptance_criteria_count"] = len(criteria)

    if not criteria and functional_reqs:
        result.add_error(
            "acceptance_criteria",
            "No acceptance criteria defined",
            "Each functional requirement should have testable acceptance criteria"
        )
    elif len(criteria) < len(functional_reqs):
        result.add_warning(
            "acceptance_criteria",
            f"Only {len(criteria)} criteria for {len(functional_reqs)} functional requirements",
            "Consider adding more acceptance criteria"
        )
    else:
        result.add_info(
            "acceptance_criteria",
            f"Found {len(criteria)} acceptance criteria"
        )


def validate_status_confirmed(
    requirements_data: dict[str, Any],
    result: ValidationResult
) -> None:
    """Check that requirements have been confirmed."""
    if not requirements_data.get("has_status"):
        result.add_error(
            "status",
            "Requirements document lacks status field",
            "Add '**Status:** Confirmed' after user approval"
        )
    elif requirements_data.get("status", "").lower() != "confirmed":
        result.add_error(
            "status",
            f"Requirements status is '{requirements_data['status']}', not 'Confirmed'",
            "User must confirm requirements before planning"
        )
    else:
        result.add_info("status", "Requirements confirmed by user")


def run_validation(session_id: str, verbose: bool = False) -> ValidationResult:
    """Run all validations for a session."""
    result = ValidationResult()
    docs_root = find_docs_root()

    # Find files
    questions_file = docs_root / "specs" / f"questions-{session_id}.md"
    requirements_file = docs_root / "specs" / f"requirements-{session_id}.md"

    # Read questions document
    questions_content = read_file_content(questions_file)
    if questions_content is None:
        result.add_warning(
            "files",
            f"Questions file not found: {questions_file}",
            "This may be expected if questions were answered inline"
        )
        questions_data = {}
    else:
        questions_data = parse_questions_document(questions_content)
        if verbose:
            result.add_info("files", f"Parsed questions from {questions_file}")

    # Read requirements document
    requirements_content = read_file_content(requirements_file)
    if requirements_content is None:
        result.add_error(
            "files",
            f"Requirements file not found: {requirements_file}",
            "Requirements document must exist before planning phase"
        )
        return result
    else:
        requirements_data = parse_requirements_document(requirements_content)
        if verbose:
            result.add_info("files", f"Parsed requirements from {requirements_file}")

    # Run validations
    if questions_data:
        validate_blocking_questions_answered(questions_data, result)
        validate_questions_have_defaults(questions_data, result)

    validate_no_contradictions(requirements_data, result)
    validate_technical_feasibility(requirements_data, result)
    validate_confidence_levels(requirements_data, result)
    validate_acceptance_criteria(requirements_data, result)
    validate_status_confirmed(requirements_data, result)

    return result


def print_result(result: ValidationResult, json_output: bool = False) -> None:
    """Print validation result to console."""
    if json_output:
        print(json.dumps(result.to_dict(), indent=2))
        return

    # Header
    status = "PASSED" if result.is_valid() else "FAILED"
    status_color = "\033[92m" if result.is_valid() else "\033[91m"
    reset_color = "\033[0m"

    print(f"\n{'=' * 60}")
    print(f"Requirements Validation: {status_color}{status}{reset_color}")
    print(f"{'=' * 60}\n")

    # Stats
    if result.stats:
        print("Statistics:")
        for key, value in result.stats.items():
            print(f"  - {key.replace('_', ' ').title()}: {value}")
        print()

    # Errors
    if result.errors:
        print(f"\033[91mErrors ({len(result.errors)}):\033[0m")
        for error in result.errors:
            print(f"  [{error['category']}] {error['message']}")
            if error['details']:
                print(f"    Details: {error['details']}")
        print()

    # Warnings
    if result.warnings:
        print(f"\033[93mWarnings ({len(result.warnings)}):\033[0m")
        for warning in result.warnings:
            print(f"  [{warning['category']}] {warning['message']}")
            if warning['details']:
                print(f"    Details: {warning['details']}")
        print()

    # Info (only if verbose or few items)
    if result.info and len(result.info) <= 5:
        print(f"\033[94mInfo:\033[0m")
        for info in result.info:
            print(f"  [{info['category']}] {info['message']}")
        print()

    # Summary
    print(f"{'=' * 60}")
    if result.is_valid():
        print("\033[92mValidation PASSED - Ready for planning phase\033[0m")
    else:
        print("\033[91mValidation FAILED - Address errors before proceeding\033[0m")
    print(f"{'=' * 60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Validate requirements documents for RQPIV workflow"
    )
    parser.add_argument(
        "session_id",
        help="Session ID to validate (e.g., '2024-01-15-feature-x')"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output results as JSON"
    )

    args = parser.parse_args()

    try:
        result = run_validation(args.session_id, args.verbose)
        print_result(result, args.json)
        sys.exit(0 if result.is_valid() else 1)
    except Exception as e:
        if args.json:
            print(json.dumps({"error": str(e), "valid": False}))
        else:
            print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
