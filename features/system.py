import os
import shutil
import subprocess
from getpass import getpass
from utils.file_system import get_directory_size, human_readable_size


def clean_system_logs(log_dirs):
    """
    Cleans the system log directories specified.

    Args:
        log_dirs (list): A list of system log directories to clean.

    Returns:
        dict: A dictionary with the results of the cleaning operation.
    """
    results = {
        'cleared_sizes': {},
        'errors': [],
        'total_dirs': len(log_dirs),
        'cleaned_dirs': 0
    }

    for dir_path in log_dirs:
        if os.path.exists(dir_path):
            size_before = get_directory_size(dir_path)
            try:
                for log_file in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, log_file)
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                results['cleared_sizes'][dir_path] = human_readable_size(size_before)
                results['cleaned_dirs'] += 1
            except Exception as e:
                results['errors'].append(f"Failed to clean {dir_path}: {str(e)}")

    return results


def clean_system_cache(directories, layout):
    results = {
        'cleared_sizes': {},
        'errors': [],
        'total_dirs': len(directories),
        'cleaned_dirs': 0
    }

    for dir_path in directories:
        try:
            if dir_path.startswith('/System/') or dir_path.startswith('/Library/'):
                layout.display_operation_message(f"Cleaning {dir_path}. Sudo password may be required.")
                sudo_password = layout.get_password_in_details("Enter sudo password: ")

                command = f"sudo rm -rf {dir_path}/*"
                process = subprocess.Popen(['sudo', '-S'] + command.split(),
                                           stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           universal_newlines=True)
                sudo_prompt = process.communicate(input=sudo_password + '\n')[1]

                if 'try again' in sudo_prompt.lower():
                    layout.display_operation_message("Incorrect sudo password. Please try again.")
                    results['errors'].append(f"Failed to clean {dir_path}: Incorrect sudo password")
                    continue
            else:
                shutil.rmtree(dir_path)

            results['cleared_sizes'][dir_path] = "Unknown"  # Size calculation could be added here
            results['cleaned_dirs'] += 1
            layout.display_operation_message(f"Successfully cleaned: {dir_path}")

        except PermissionError:
            results['errors'].append(f"Permission denied: {dir_path}")
            layout.display_operation_message(f"Permission denied: {dir_path}")
        except Exception as e:
            results['errors'].append(f"Failed to clean {dir_path}: {str(e)}")
            layout.display_operation_message(f"Failed to clean {dir_path}: {str(e)}")

    return results