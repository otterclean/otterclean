import curses
from config.settings import COLOR_SCHEME


class DetailsDisplay:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def render(self, details):
        # Get screen dimensions
        max_y, max_x = self.stdscr.getmaxyx()
        split_point = max_x // 3

        # Clear previous details
        self.stdscr.attron(curses.color_pair(COLOR_SCHEME['default']))
        self.stdscr.addstr(3, split_point + 2, " " * (max_x - split_point - 4))
        self.stdscr.attroff(curses.color_pair(COLOR_SCHEME['default']))

        # Render details
        for idx, line in enumerate(details.split('\n')):
            self.stdscr.attron(curses.color_pair(COLOR_SCHEME['info']))
            self.stdscr.addstr(3 + idx, split_point + 2, line)
            self.stdscr.attroff(curses.color_pair(COLOR_SCHEME['info']))
