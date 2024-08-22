import unittest
from unittest.mock import patch
from otterclean.features.docker_management import prune_docker_system, prune_docker_images, prune_docker_containers, prune_docker_volumes, prune_docker_builder_cache

class TestDockerPruneCommands(unittest.TestCase):

    @patch('features.docker_management.run_command')
    def test_prune_docker_system(self, mock_run_command):
        mock_run_command.return_value = 'Docker system prune successful'
        
        result = prune_docker_system()
        
        expected_command = "docker system prune -a --volumes -f"
        mock_run_command.assert_called_once_with(expected_command)
        self.assertEqual(result, 'Docker system prune successful')

    @patch('features.docker_management.run_command')
    def test_prune_docker_images(self, mock_run_command):
        mock_run_command.return_value = 'Docker image prune successful'
        
        result = prune_docker_images()
        
        expected_command = "docker image prune -a -f"
        mock_run_command.assert_called_once_with(expected_command)
        self.assertEqual(result, 'Docker image prune successful')

    @patch('features.docker_management.run_command')
    def test_prune_docker_containers(self, mock_run_command):
        mock_run_command.return_value = 'Docker container prune successful'
        
        result = prune_docker_containers()
        
        expected_command = "docker container prune -f"
        mock_run_command.assert_called_once_with(expected_command)
        self.assertEqual(result, 'Docker container prune successful')

    @patch('features.docker_management.run_command')
    def test_prune_docker_volumes(self, mock_run_command):
        mock_run_command.return_value = 'Docker volume prune successful'
        
        result = prune_docker_volumes()
        
        expected_command = "docker volume prune -f"
        mock_run_command.assert_called_once_with(expected_command)
        self.assertEqual(result, 'Docker volume prune successful')

    @patch('features.docker_management.run_command')
    def test_prune_docker_builder_cache(self, mock_run_command):
        mock_run_command.return_value = 'Docker builder prune successful'
        
        result = prune_docker_builder_cache()
        
        expected_command = "docker builder prune --all -f"
        mock_run_command.assert_called_once_with(expected_command)
        self.assertEqual(result, 'Docker builder prune successful')

if __name__ == '__main__':
    unittest.main()
