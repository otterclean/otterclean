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
                    for chunk in range(0, file_size, 512):
                        f.write(pattern)
                        progress = (chunk + 512) / file_size * 100
                        yield f"Iteration {i + 1}/{iterations} completed", int(progress)

                f.flush()
                os.fsync(f.fileno())

        os.remove(file_path)
        return f"File securely deleted: {file_path}"
    except Exception as e:
        return f"Error deleting file {file_path}: {str(e)}"


def secure_delete_folder(folder_path, method='simple'):
    if not os.path.exists(folder_path):
        yield f"Folder not found: {folder_path}", 100
        return

    try:
        # Klasördeki toplam dosya sayısını hesapla
        total_files = sum([len(files) for r, d, files in os.walk(folder_path)])
        files_deleted = 0

        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                for progress, _ in secure_delete_file(file_path, method):
                    yield progress, int((files_deleted / total_files) * 100)
                files_deleted += 1

            # Alt klasörleri sil
            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    os.rmdir(dir_path)
                    yield f"Deleted empty directory: {dir_path}", int((files_deleted / total_files) * 100)
                except OSError:
                    yield f"Could not delete directory: {dir_path}", int((files_deleted / total_files) * 100)

        # Ana klasörü sil
        try:
            os.rmdir(folder_path)
            yield f"Folder securely deleted: {folder_path}", 100
        except OSError:
            yield f"Could not delete the main folder: {folder_path}", 100

    except Exception as e:
        yield f"Error deleting folder {folder_path}: {str(e)}", 100