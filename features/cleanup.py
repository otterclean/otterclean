import os
import shutil
from utils.file_system import get_directory_size, human_readable_size


def perform_cleanup(option):
    if option == 1:
        print("Clearing caches...")
        clear_cache(['/path/to/cache'])
    elif option == 2:
        print("Clearing logs...")
        clear_logs(['/path/to/logs'])
    elif option == 3:
        print("Clearing temporary files...")
        clear_temp_files(['/path/to/temp'])
    else:
        print("Invalid option selected.")


def clear_cache(cache_dirs):
    """
    Clears the specified cache directories.
    
    Args:
        cache_dirs (list): A list of directories to clear.
        
    Returns:
        dict: A dictionary with the size of cleared cache for each directory.
    """
    cleared_sizes = {}

    for dir_path in cache_dirs:
        if os.path.exists(dir_path):
            size_before = get_directory_size(dir_path)
            shutil.rmtree(dir_path)
            os.makedirs(dir_path)  # Recreate the directory
            cleared_sizes[dir_path] = human_readable_size(size_before)

    return cleared_sizes


def clear_logs(log_dirs):
    """
    Clears the specified log directories.
    
    Args:
        log_dirs (list): A list of log directories to clear.
        
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


def clear_temp_files(temp_dirs):
    """
    Clears temporary files from the specified directories.
    
    Args:
        temp_dirs (list): A list of temporary directories to clear.
        
    Returns:
        dict: A dictionary with the size of cleared temporary files for each directory.
    """
    cleared_sizes = {}

    for dir_path in temp_dirs:
        if os.path.exists(dir_path):
            size_before = get_directory_size(dir_path)
            shutil.rmtree(dir_path)
            os.makedirs(dir_path)  # Recreate the directory
            cleared_sizes[dir_path] = human_readable_size(size_before)

    return cleared_sizes
