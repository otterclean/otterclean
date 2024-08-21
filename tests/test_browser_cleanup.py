import os
import shutil
import pytest
from unittest.mock import patch, call
from features.browser_cleanup import clean_chrome_cache, clean_firefox_cache, clean_browser_caches

def test_clean_chrome_cache_exists():
    with patch('os.path.exists', return_value=True), \
         patch('shutil.rmtree') as mock_rmtree:
        result = clean_chrome_cache()
        expected_path = os.path.expanduser("~/Library/Caches/Google/Chrome/Default/Cache")
        assert result == f"Chrome cache cleaned: {expected_path}"
        mock_rmtree.assert_called_once_with(expected_path)

def test_clean_chrome_cache_not_exists():
    with patch('os.path.exists', return_value=False):
        result = clean_chrome_cache()
        assert result == "Chrome cache not found"

def test_clean_firefox_cache_exists():
    with patch('os.path.exists', return_value=True), \
         patch('shutil.rmtree') as mock_rmtree:
        result = clean_firefox_cache()
        expected_path = os.path.expanduser("~/Library/Caches/Firefox")
        assert result == f"Firefox cache cleaned: {expected_path}"
        mock_rmtree.assert_called_once_with(expected_path)

def test_clean_firefox_cache_not_exists():
    with patch('os.path.exists', return_value=False):
        result = clean_firefox_cache()
        assert result == "Firefox cache not found"

def test_clean_browser_caches():
    with patch('os.path.exists') as mock_exists, \
         patch('shutil.rmtree') as mock_rmtree:
        mock_exists.side_effect = [True, True]
        result = clean_browser_caches()
        expected_chrome_path = os.path.expanduser("~/Library/Caches/Google/Chrome/Default/Cache")
        expected_firefox_path = os.path.expanduser("~/Library/Caches/Firefox")
        expected_result = (
            f"Chrome cache cleaned: {expected_chrome_path}\n"
            f"Firefox cache cleaned: {expected_firefox_path}"
        )
        assert result == expected_result

        calls = [call(expected_chrome_path), call(expected_firefox_path)]
        mock_rmtree.assert_has_calls(calls, any_order=False)

    with patch('os.path.exists') as mock_exists:
        mock_exists.side_effect = [False, False]
        result = clean_browser_caches()
        assert result == "Chrome cache not found\nFirefox cache not found"
