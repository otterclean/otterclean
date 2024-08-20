import curses
from config.settings import COLOR_SCHEME


class ProgressBar:
    def __init__(self, stdscr, total):
        self.stdscr = stdscr
        self.total = total
        self.current_progress = 0

    def update(self, progress):
        self.current_progress = progress
        self.render()

    def render(self):
        # Get screen dimensions
        max_y, max_x = self.stdscr.getmaxyx()
        bar_width = max_x - 10

        # Calculate the number of "filled" segments
        filled = int(self.current_progress / self.total * bar_width)

        # Draw the progress bar
        self.stdscr.attron(curses.color_pair(COLOR_SCHEME['info']))
        self.stdscr.addstr(
            max_y - 3, 5, "[" + "=" * filled + " " * (bar_width - filled) + "]")
        self.stdscr.attroff(curses.color_pair(COLOR_SCHEME['info']))


class DialogBox:
    def __init__(self, stdscr, message):
        self.stdscr = stdscr
        self.message = message

    def render(self):
        # Get screen dimensions
        max_y, max_x = self.stdscr.getmaxyx()

        # Calculate the position
        box_width = max_x // 2
        box_height = max_y // 4
        start_y = (max_y // 2) - (box_height // 2)
        start_x = (max_x // 2) - (box_width // 2)

        # Draw the box
        self.stdscr.attron(curses.color_pair(COLOR_SCHEME['highlight']))
        self.stdscr.addstr(start_y, start_x, "+" + "-" * (box_width - 2) + "+")
        for y in range(1, box_height - 1):
            self.stdscr.addstr(start_y + y, start_x, "|" +
                               " " * (box_width - 2) + "|")
        self.stdscr.addstr(start_y + box_height - 1, start_x,
                           "+" + "-" * (box_width - 2) + "+")
        self.stdscr.attroff(curses.color_pair(COLOR_SCHEME['highlight']))

        # Add the message in the center
        message_x = start_x + (box_width // 2) - (len(self.message) // 2)
        self.stdscr.addstr(start_y + (box_height // 2),
                           message_x, self.message)
