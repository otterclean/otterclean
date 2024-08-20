import os
from utils.command_runner import run_command


def prune_docker_system():
    """
    Runs the Docker system prune command to remove all unused containers, networks, images, and optionally, volumes.

    Returns:
        str: The output from the prune command.
    """
    command = "docker system prune -a --volumes -f"
    output = run_command(command)
    return output


def prune_docker_images():
    """
    Runs the Docker image prune command to remove unused Docker images.

    Returns:
        str: The output from the prune command.
    """
    command = "docker image prune -a -f"
    output = run_command(command)
    return output


def prune_docker_containers():
    """
    Runs the Docker container prune command to remove stopped Docker containers.

    Returns:
        str: The output from the prune command.
    """
    command = "docker container prune -f"
    output = run_command(command)
    return output


def prune_docker_volumes():
    """
    Runs the Docker volume prune command to remove unused Docker volumes.

    Returns:
        str: The output from the prune command.
    """
    command = "docker volume prune -f"
    output = run_command(command)
    return output


def prune_docker_builder_cache():
    """
    Runs the Docker builder prune command to clean up the Docker build cache.

    Returns:
        str: The output from the prune command.
    """
    command = "docker builder prune --all -f"
    output = run_command(command)
    return output
