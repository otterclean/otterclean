import os


def secure_delete_file(file_path):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"

    try:
        # Dosyayı rastgele verilerle üzerine yazma
        with open(file_path, "ba+") as f:
            length = f.tell()
            f.seek(0)
            f.write(os.urandom(length))

        # Dosyayı silme
        os.remove(file_path)
        return f"File securely deleted: {file_path}"
    except Exception as e:
        return f"Error deleting file {file_path}: {str(e)}"