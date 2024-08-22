import pytest
from unittest.mock import patch
from otterclean.features import clear_cache


@pytest.fixture
def test_clear_cache():
    with patch('os.path.exists', return_value=True), \
         patch('shutil.rmtree') as mock_rmtree, \
         patch('os.makedirs') as mock_makedirs, \
         patch('utils.file_system.get_directory_size', return_value=1024), \
         patch('utils.file_system.human_readable_size', return_value='1 KB') as mock_human_readable_size:
        
        cache_dirs = ['/path/to/cache']
        result = clear_cache(cache_dirs)
        
        expected_path = '/path/to/cache'
        expected_result = {expected_path: '1 KB'}
        
        assert result == expected_result
        
        mock_rmtree.assert_called_once_with(expected_path)
        mock_makedirs.assert_called_once_with(expected_path)
        
        mock_get_directory_size = patch('utils.file_system.get_directory_size').start()
        mock_get_directory_size.assert_called_once_with(expected_path)
        
        mock_human_readable_size.assert_called_once_with(1024)
