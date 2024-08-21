import sys
import time


def progress_bar(iterable, total=None, prefix='', suffix='', length=50, fill='█', print_end="\r"):
    """
    Creates a progress bar for iterating over a collection.

    Args:
        iterable (iterable): The iterable to iterate over.
        total (int): The total number of iterations (if known).
        prefix (str): A prefix string to display before the progress bar.
        suffix (str): A suffix string to display after the progress bar.
        length (int): The length of the progress bar (in characters).
        fill (str): The character used to fill the progress bar.
        print_end (str): The end character for the print function.

    Yields:
        item: The next item from the iterable.
    """
    if total is None:
        total = len(iterable)

    def print_progress_bar(iteration):
        percent = f"{100 * (iteration / float(total)):.1f}"
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)

    print_progress_bar(0)
    for i, item in enumerate(iterable):
        yield item
        print_progress_bar(i + 1)
    print()


def loading_animation(message, duration):
    """
    Displays a loading animation for a specified duration.

    Args:
        message (str): The message to display alongside the loading animation.
        duration (int): The duration of the animation in seconds.
    """
    animation = "|/-\\"
    idx = 0

    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{message} {animation[idx % len(animation)]}")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    sys.stdout.write("\r")
