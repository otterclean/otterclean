import os
import shutil
import curses
from utils.file_system import get_directory_size, human_readable_size
from ui.components import ProgressBar, DialogBox


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


def clean_selected_app_caches(layout):
    cache_dir = os.path.expanduser("~/Library/Caches")
    app_caches = []

    for item in os.listdir(cache_dir):
        full_path = os.path.join(cache_dir, item)
        if os.path.isdir(full_path):
            size = get_directory_size(full_path)
            app_caches.append((full_path, human_readable_size(size)))

    selected_caches = []
    current_selection = 0

    while True:
        layout.display_app_caches(
            app_caches, current_selection, selected_caches)

        key = layout.stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(app_caches) - 1:
            current_selection += 1
        elif key == ord(' '):
            if current_selection in selected_caches:
                selected_caches.remove(current_selection)
            else:
                selected_caches.append(current_selection)
        elif key == ord('\n'):
            break
        elif key == ord('q'):
            return
        elif key == curses.KEY_LEFT:
            return  # Sol menüye dön

    # Perform cleanup
    for index in selected_caches:
        path, _ = app_caches[index]
        try:
            shutil.rmtree(path)
        except Exception as e:
            layout.display_error(f"Error cleaning {path}: {str(e)}")

    layout.display_message("Selected caches have been cleaned.")
