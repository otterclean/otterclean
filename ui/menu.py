import curses
from config.settings import COLOR_SCHEME


class MainMenu:
    def __init__(self, stdscr, options):
        """
        Initializes the MainMenu class.

        Args:
            stdscr: The curses screen object.
            options (list): A list of menu options to display.
        """
        self.stdscr = stdscr
        self.options = options
        self.current_option = 0
        self.scroll_offset = 0
        self.window_height, self.window_width = self.stdscr.getmaxyx()

    def render(self):
        """
        Renders the menu on the screen. It highlights the currently selected option.
        """
        # Calculate the displayable area, accounting for borders, padding, etc.
        max_y = self.window_height - 6

        # Determine the range of options to display based on the current scroll position
        display_range = range(self.scroll_offset, self.scroll_offset + max_y)
        if self.current_option >= display_range.stop:
            self.scroll_offset += 1
        elif self.current_option < display_range.start:
            self.scroll_offset -= 1
        display_range = range(self.scroll_offset, self.scroll_offset + max_y)

        # Render each menu option
        for idx, option in enumerate(self.options[display_range.start:display_range.stop]):
            y = 3 + idx
            if idx + display_range.start == self.current_option:
                # Highlight the selected option
                self.stdscr.attron(curses.color_pair(
                    COLOR_SCHEME['highlight']))
                self.stdscr.addstr(y, 2, option)
                self.stdscr.attroff(curses.color_pair(
                    COLOR_SCHEME['highlight']))
            else:
                # Render other options with normal text color
                self.stdscr.attron(curses.color_pair(COLOR_SCHEME['default']))
                self.stdscr.addstr(y, 2, option)
                self.stdscr.attroff(curses.color_pair(COLOR_SCHEME['default']))

    def navigate(self, direction):
        """
        Handles navigation within the menu.

        Args:
            direction (str): "UP" or "DOWN", indicating the navigation direction.
        """
        max_y = self.window_height - 6

        if direction == "UP" and self.current_option > 0:
            self.current_option -= 1
        elif direction == "DOWN" and self.current_option < len(self.options) - 1:
            self.current_option += 1

    def get_selected_option(self):
        """
        Returns the currently selected menu option.

        Returns:
            int: The index of the currently selected option.
        """
        return self.current_option
