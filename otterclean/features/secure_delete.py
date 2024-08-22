import os
import random


def secure_delete_file(file_path, method='simple'):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"

    try:
        file_size = os.path.getsize(file_path)

        with open(file_path, "ba+") as f:
            if method == 'simple':
                iterations = 1
            elif method == 'dod':
                iterations = 3
            elif method == 'gutmann':
                iterations = 35
            else:
                return "Invalid method selected"

            for i in range(iterations):
                f.seek(0)
                if method == 'gutmann' and i >= 4:
                    f.write(os.urandom(file_size))
                else:
                    pattern = bytes([random.randint(0, 255) for _ in range(512)])
                    for _ in range(0, file_size, 512):
                        f.write(pattern)
                f.flush()
                os.fsync(f.fileno())
                yield f"Iteration {i + 1}/{iterations} completed"

        os.remove(file_path)
        return f"File securely deleted: {file_path}"
    except Exception as e:
        return f"Error deleting file {file_path}: {str(e)}"


def secure_delete_folder(folder_path, method='simple'):
    if not os.path.exists(folder_path):
        return f"Folder not found: {folder_path}"

    try:
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                yield from secure_delete_file(file_path, method)
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(folder_path)
        return f"Folder securely deleted: {folder_path}"
    except Exception as e:
        return f"Error deleting folder {folder_path}: {str(e)}"