import os
from datetime import datetime


def generate_report(cleanup_actions):
    report = f"Cleanup Report - {datetime.now()}\n"
    report += "=" * 30 + "\n\n"

    for action, result in cleanup_actions:
        report += f"Action: {action}\n"
        report += f"Result: {result}\n\n"

    return report


def save_report(report, filename="cleanup_report.txt"):
    with open(filename, "w") as f:
        f.write(report)
    return f"Report saved to {os.path.abspath(filename)}"