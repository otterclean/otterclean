import curses
from otterclean.config.settings import COLOR_SCHEME


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
        self.menu_width = self.window_width // 4

    def render(self):
        max_y = self.window_height - 6
        display_range = range(self.scroll_offset, min(
            self.scroll_offset + max_y, len(self.options)))

        for idx, option in enumerate(self.options[self.scroll_offset:self.scroll_offset + max_y]):
            y = 3 + idx  # Başlık için yer bırakıyoruz
            if idx + self.scroll_offset == self.current_option:
                self.stdscr.attron(curses.color_pair(COLOR_SCHEME['highlight']))
                self.stdscr.addstr(y, 2, f"> {option[:self.menu_width - 4]}")
                self.stdscr.attroff(curses.color_pair(COLOR_SCHEME['highlight']))
            else:
                self.stdscr.attron(curses.color_pair(COLOR_SCHEME['default']))
                self.stdscr.addstr(y, 2, f"  {option[:self.menu_width - 4]}")
                self.stdscr.attroff(curses.color_pair(COLOR_SCHEME['default']))

    def navigate(self, direction):
        """
        Handles navigation within the menu.

        Args:
            direction (str): "UP" or "DOWN", indicating the navigation direction.
        """
        if direction == "UP" and self.current_option > 0:
            self.current_option -= 1
            if self.current_option < self.scroll_offset:
                self.scroll_offset -= 1
        elif direction == "DOWN" and self.current_option < len(self.options) - 1:
            self.current_option += 1
            if self.current_option >= self.scroll_offset + (self.window_height - 6):
                self.scroll_offset += 1

    def get_selected_option(self):
        """
        Returns the currently selected menu option.

        Returns:
            int: The index of the currently selected option.
        """
        return self.current_option

    def update_dimensions(self, height, width):
        """
        Updates the menu dimensions when the terminal is resized.

        Args:
            height (int): New height of the terminal window.
            width (int): New width of the terminal window.
        """
        self.window_height = height
        self.window_width = width
        self.scroll_offset = max(0, min(self.scroll_offset, len(
            self.options) - (self.window_height - 6)))
