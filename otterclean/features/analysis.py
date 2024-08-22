import os
from otterclean.utils.file_system import get_directory_size, human_readable_size


def analyze_disk_usage(directories):
    """
    Analyzes the disk usage of specified directories.

    Args:
        directories (list): A list of directories to analyze.

    Returns:
        dict: A dictionary with the size of each directory.
    """
    usage_report = {}

    for dir_path in directories:
        if os.path.exists(dir_path) and os.access(dir_path, os.R_OK):
            size = get_directory_size(dir_path)
            usage_report[dir_path] = human_readable_size(size)
        else:
            usage_report[dir_path] = "Permission denied or directory doesn't exist"

    return usage_report


def analyze_file_types(directory):
    """
    Analyzes the types of files within a directory and their sizes.

    Args:
        directory (str): The directory to analyze.

    Returns:
        dict: A dictionary with file extensions as keys and their total sizes as values.
    """
    file_types = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            size = os.path.getsize(file_path)

            if ext in file_types:
                file_types[ext] += size
            else:
                file_types[ext] = size

    # Convert sizes to human-readable format
    for ext in file_types:
        file_types[ext] = human_readable_size(file_types[ext])

    return file_types


def analyze_large_files(directory, size_threshold):
    """
    Finds large files in the specified directory that exceed the size threshold.

    Args:
        directory (str): The directory to search for large files.
        size_threshold (int): The size threshold in bytes.

    Returns:
        list: A list of tuples containing the file path and size of large files.
    """
    large_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)

            if size > size_threshold:
                large_files.append((file_path, human_readable_size(size)))

    return large_files
