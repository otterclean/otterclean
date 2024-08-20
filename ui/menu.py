import curses
from config.settings import COLOR_SCHEME


class MainMenu:
    def __init__(self, stdscr, options):
        self.stdscr = stdscr
        self.options = options
        self.current_option = 0

    def render(self):
        # Get screen dimensions
        max_y, max_x = self.stdscr.getmaxyx()

        # Render each option
        for idx, option in enumerate(self.options):
            if idx == self.current_option:
                # Highlight the selected option
                self.stdscr.attron(curses.color_pair(
                    COLOR_SCHEME['highlight']))
                self.stdscr.addstr(3 + idx, 2, option)
                self.stdscr.attroff(curses.color_pair(
                    COLOR_SCHEME['highlight']))
            else:
                # Render other options normally
                self.stdscr.attron(curses.color_pair(COLOR_SCHEME['default']))
                self.stdscr.addstr(3 + idx, 2, option)
                self.stdscr.attroff(curses.color_pair(COLOR_SCHEME['default']))

    def navigate(self, direction):
        if direction == "UP" and self.current_option > 0:
            self.current_option -= 1
        elif direction == "DOWN" and self.current_option < len(self.options) - 1:
            self.current_option += 1

    def get_selected_option(self):
        return self.current_option
