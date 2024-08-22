import subprocess


def run_command(command):
    """
    Runs a shell command and returns the output.

    Args:
        command (str): The command to run.

    Returns:
        str: The output from the command.

    Raises:
        RuntimeError: If the command returns a non-zero exit code.
    """
    try:
        result = subprocess.run(command, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Command '{command}' failed with error: {e.stderr}")


def run_command_with_timeout(command, timeout):
    """
    Runs a shell command with a timeout.

    Args:
        command (str): The command to run.
        timeout (int): The timeout in seconds.

    Returns:
        str: The output from the command.

    Raises:
        RuntimeError: If the command returns a non-zero exit code or times out.
    """
    try:
        result = subprocess.run(command, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, timeout=timeout)
        return result.stdout
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"Command '{command}' timed out after {timeout} seconds")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Command '{command}' failed with error: {e.stderr}")
