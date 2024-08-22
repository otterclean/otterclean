from unittest.mock import mock_open, patch
from otterclean.features.secure_delete import secure_delete_file

def test_secure_delete_file_success():
    file_path = "/path/to/test/file.txt"

    with patch("os.path.exists", return_value=True), \
         patch("os.remove") as mock_remove, \
         patch("builtins.open", mock_open(read_data=b"test data")) as mock_file:

        mock_file.return_value.tell.return_value = 9  # Assuming file size of 9 bytes

        result = secure_delete_file(file_path)

        mock_file.assert_called_once_with(file_path, "ba+")
        mock_file.return_value.write.assert_called_once()
        assert mock_remove.called
        assert result == f"File securely deleted: {file_path}"

def test_secure_delete_file_not_found():
    file_path = "/path/to/test/file.txt"

    with patch("os.path.exists", return_value=False):
        result = secure_delete_file(file_path)

        assert result == f"File not found: {file_path}"

def test_secure_delete_file_error():
    file_path = "/path/to/test/file.txt"

    with patch("os.path.exists", return_value=True), \
         patch("os.remove") as mock_remove, \
         patch("builtins.open", mock_open(read_data=b"test data")) as mock_file:

        mock_remove.side_effect = OSError("Remove error")

        result = secure_delete_file(file_path)

        assert mock_remove.called
        assert result == f"Error deleting file {file_path}: Remove error"

