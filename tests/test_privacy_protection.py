import unittest
from unittest.mock import patch, MagicMock
import os  # Import the os module
from features.privacy_protection import clean_privacy_traces, empty_trash

class TestCleanPrivacyTraces(unittest.TestCase):

    @patch('features.privacy_protection.os.path.exists')
    @patch('features.privacy_protection.os.remove')
    @patch('features.privacy_protection.os.listdir')
    @patch('features.privacy_protection.os.system')
    @patch('features.privacy_protection.empty_trash')
    def test_clean_privacy_traces(self, mock_empty_trash, mock_system, mock_listdir, mock_remove, mock_exists):
        # Mocking
        mock_exists.side_effect = lambda path: path in [
            os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/History"),
            os.path.expanduser("~/Library/Application Support/com.apple.sharedfilelist/")
        ]
        mock_listdir.return_value = ['recent1.sfl2', 'recent2.sfl2']
        mock_system.return_value = None
        mock_empty_trash.return_value = "Trash emptied successfully"
        
        # Test for all options selected
        selected_options = [
            "Chrome browsing history",
            "System clipboard",
            "Recent items",
            "Trash"
        ]
        result = clean_privacy_traces(selected_options)
        expected_result = (
            "Chrome browsing history cleared\n"
            "System clipboard cleared\n"
            "Recent items cleared\n"
            "Trash emptied successfully"
        )
        self.assertEqual(result, expected_result)

        # Verify that the correct functions are called with expected arguments
        mock_exists.assert_any_call(os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/History"))
        mock_remove.assert_any_call(os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/History"))
        mock_exists.assert_any_call(os.path.expanduser("~/Library/Application Support/com.apple.sharedfilelist/"))
        mock_remove.assert_any_call(os.path.join(os.path.expanduser("~/Library/Application Support/com.apple.sharedfilelist/"), 'recent1.sfl2'))
        mock_remove.assert_any_call(os.path.join(os.path.expanduser("~/Library/Application Support/com.apple.sharedfilelist/"), 'recent2.sfl2'))
        mock_system.assert_called_with("pbcopy < /dev/null")
        mock_empty_trash.assert_called_once()

    @patch('features.privacy_protection.empty_trash')
    def test_empty_trash_only(self, mock_empty_trash):
        mock_empty_trash.return_value = "Trash emptied successfully"

        selected_options = ["Trash"]
        result = clean_privacy_traces(selected_options)
        expected_result = "Trash emptied successfully"
        self.assertEqual(result, expected_result)
        
        mock_empty_trash.assert_called_once()

    @patch('features.privacy_protection.os.path.exists')
    @patch('features.privacy_protection.os.remove')
    @patch('features.privacy_protection.os.listdir')
    def test_no_options_selected(self, mock_listdir, mock_remove, mock_exists):
        mock_exists.side_effect = lambda path: False
        mock_listdir.return_value = []
        
        selected_options = []
        result = clean_privacy_traces(selected_options)
        expected_result = ""
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
