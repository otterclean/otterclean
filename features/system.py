import os
import shutil
from utils.file_system import get_directory_size, human_readable_size


def clean_system_logs(log_dirs):
    """
    Cleans the system log directories specified.
    
    Args:
        log_dirs (list): A list of system log directories to clean.
        
    Returns:
        dict: A dictionary with the size of cleared logs for each directory.
    """
    cleared_sizes = {}

    for dir_path in log_dirs:
        if os.path.exists(dir_path):
            size_before = get_directory_size(dir_path)
            for log_file in os.listdir(dir_path):
                file_path = os.path.join(dir_path, log_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
            cleared_sizes[dir_path] = human_readable_size(size_before)

    return cleared_sizes


def clean_system_cache(cache_dirs):
    """
    Cleans the system cache directories specified.
    
    Args:
        cache_dirs (list): A list of system cache directories to clean.
        
    Returns:
        dict: A dictionary with the size of cleared caches for each directory.
    """
    cleared_sizes = {}

    for dir_path in cache_dirs:
        if os.path.exists(dir_path):
            size_before = get_directory_size(dir_path)
            shutil.rmtree(dir_path)
            os.makedirs(dir_path)  # Recreate the directory
            cleared_sizes[dir_path] = human_readable_size(size_before)

    return cleared_sizes
