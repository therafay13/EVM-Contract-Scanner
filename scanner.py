import sys
import re
import os

def scan_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    vulnerabilities = [
        {"name": "Use of tx.origin", "pattern": r"\btx\.origin\b", "severity": "High"},
        {"name": "Use of block.timestamp", "pattern": r"\bblock\.timestamp\b", "severity": "Medium"},
        {"name": "Use of selfdestruct", "pattern": r"\bselfdestruct\s*\(", "severity": "High"},
        {"name": "Unchecked Call", "pattern": r"\.call\s*\{value:", "severity": "Low (Requires manual review)"},
    ]

    print(f"--- Scanning {filepath} ---")
    found_issues = False

    for i, line in enumerate(lines):
        for vuln in vulnerabilities:
            if re.search(vuln["pattern"], line):
                print(f"[!] {vuln['severity']} | {vuln['name']} found on line {i + 1}:")
                print(f"    {line.strip()}")
                found_issues = True

    if not found_issues:
        print("No basic vulnerabilities found. Manual review still required.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <file.sol>")
    else:
        scan_file(sys.argv[1])
