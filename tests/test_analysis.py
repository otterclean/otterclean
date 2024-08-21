import os
import pytest
from features.analysis import analyze_disk_usage, analyze_file_types, analyze_large_files
from utils.file_system import human_readable_size

@pytest.fixture
def create_test_environment(tmpdir):
    test_dir = tmpdir.mkdir("test_dir")
    sub_dir = test_dir.mkdir("sub_dir")
    small_file = test_dir.join("small_file.txt")
    large_file = sub_dir.join("large_file.txt")

    small_file.write("small content")
    large_file.write("large content" * 1024 * 1024)  # Yaklaşık 12 MB

    return test_dir

def test_analyze_disk_usage(create_test_environment):
    test_dir = str(create_test_environment)
    result = analyze_disk_usage([test_dir])

    assert test_dir in result
    assert "MB" in result[test_dir] or "KB" in result[test_dir]

def test_analyze_file_types(create_test_environment):
    test_dir = str(create_test_environment)
    result = analyze_file_types(test_dir)

    assert ".txt" in result
    assert "MB" in result[".txt"] or "KB" in result[".txt"]

def test_analyze_large_files(create_test_environment):
    test_dir = str(create_test_environment)
    size_threshold = 10 * 1024 * 1024  # 10 MB
    result = analyze_large_files(test_dir, size_threshold)

    assert len(result) == 1
    assert "large_file.txt" in result[0][0]
    assert "MB" in result[0][1]

def test_analyze_large_files_no_large_files(create_test_environment):
    test_dir = str(create_test_environment)
    size_threshold = 50 * 1024 * 1024  # 50 MB
    result = analyze_large_files(test_dir, size_threshold)

    assert len(result) == 0
