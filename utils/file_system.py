import os


def get_directory_size(directory):
    """
    Calculates the total size of the specified directory.
    
    Args:
        directory (str): The path to the directory.
        
    Returns:
        int: The total size of the directory in bytes.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Skip if it is symbolic link
            if not os.path.islink(fp):
                try:
                    total_size += os.path.getsize(fp)
                except (PermissionError, OSError):
                    # Skip files that can't be accessed
                    continue

    return total_size


def human_readable_size(size, decimal_places=2):
    """
    Converts a size in bytes to a human-readable format.
    
    Args:
        size (int): The size in bytes.
        decimal_places (int): The number of decimal places to include in the result.
        
    Returns:
        str: The size in a human-readable format (e.g., KB, MB, GB).
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024
    return f"{size:.{decimal_places}f} PB"


def scan_directory(directory):
    """
    Scans the specified directory and returns a list of files and their sizes.
    
    Args:
        directory (str): The path to the directory.
        
    Returns:
        list: A list of tuples where each tuple contains the file path and its size.
    """
    file_list = []
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                file_list.append((fp, os.path.getsize(fp)))
    return file_list
