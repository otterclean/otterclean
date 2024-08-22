import os
from datetime import datetime
from unittest.mock import patch, mock_open
from otterclean.features import generate_report, save_report

def test_generate_report():
    cleanup_actions = [
        ("Cleared Chrome history", "Success"),
        ("Cleared clipboard", "Success"),
        ("Emptied trash", "Failed")
    ]

    result = generate_report(cleanup_actions)

    lines = result.split('\n')
    report_date_time = lines[0].replace("Cleanup Report - ", "").strip()
    report_date_time = report_date_time.split(' ')[0]  # Extract date part only
    
    expected_report_fixed_part = (
        "Cleanup Report - YYYY-MM-DD HH:MM:SS\n"
        + "=" * 30 + "\n\n"
        + "Action: Cleared Chrome history\n"
        + "Result: Success\n\n"
        + "Action: Cleared clipboard\n"
        + "Result: Success\n\n"
        + "Action: Emptied trash\n"
        + "Result: Failed\n\n"
    )

    expected_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expected_report = expected_report_fixed_part.replace('YYYY-MM-DD HH:MM:SS', expected_date_time)

    assert result.strip().startswith(f"Cleanup Report - {expected_date_time}")
    assert '\n'.join(result.split('\n')[1:]).strip() == '\n'.join(expected_report.split('\n')[1:]).strip()

@patch("builtins.open", new_callable=mock_open)
def test_save_report(mock_open):
    report = "Sample Report"
    filename = "test_report.txt"
    
    result = save_report(report, filename)
    
    expected_message = f"Report saved to {os.path.abspath(filename)}"
    assert result == expected_message
    
    mock_open.assert_called_once_with(filename, "w")
    mock_open().write.assert_called_once_with(report)
