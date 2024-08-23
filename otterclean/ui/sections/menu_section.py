import curses
from otterclean.config.settings import COLOR_SCHEME

class MenuSection:
    def __init__(self, window, options):
        self.window = window
        self.options = options
        self.current_option = 0
        self.scroll_offset = 0
        self.height, self.width = window.getmaxyx()

    def render(self):
        self.window.clear()
        max_display = self.height - 2
        display_range = range(self.scroll_offset, min(self.scroll_offset + max_display, len(self.options)))

        for idx, option in enumerate(self.options[self.scroll_offset:self.scroll_offset + max_display]):
            y = idx + 1
            if idx + self.scroll_offset == self.current_option:
                self.window.attron(curses.color_pair(COLOR_SCHEME['highlight']))
                self.window.addstr(y, 1, f"> {option[:self.width - 4]}")
                self.window.attroff(curses.color_pair(COLOR_SCHEME['highlight']))
            else:
                self.window.addstr(y, 1, f"  {option[:self.width - 4]}")

        self.window.box()
        self.window.refresh()

    def navigate(self, direction):
        if direction == "UP" and self.current_option > 0:
            self.current_option -= 1
            if self.current_option < self.scroll_offset:
                self.scroll_offset -= 1
        elif direction == "DOWN" and self.current_option < len(self.options) - 1:
            self.current_option += 1
            if self.current_option >= self.scroll_offset + (self.height - 2):
                self.scroll_offset += 1

    def get_selected_option(self):
        return self.current_option

    def handle_resize(self, new_height, new_width):
        self.height, self.width = new_height, new_width
        self.window.resize(new_height, new_width)
        self.scroll_offset = max(0, min(self.scroll_offset, len(self.options) - (self.height - 2)))