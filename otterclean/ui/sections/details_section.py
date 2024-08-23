import curses
import textwrap

class DetailsSection:
    def __init__(self, window):
        self.window = window
        self.height, self.width = window.getmaxyx()

    def render(self, content):
        self.window.clear()
        wrapped_content = textwrap.wrap(content, self.width - 4)
        for idx, line in enumerate(wrapped_content):
            if idx < self.height - 2:
                self.window.addstr(idx + 1, 2, line)
        self.window.box()
        self.window.refresh()

    def update(self, content):
        self.render(content)

    def handle_resize(self, new_height, new_width):
        self.height, self.width = new_height, new_width
        self.window.resize(new_height, new_width)

    def display_operation_result(self, message):
        self.window.clear()
        wrapped_message = textwrap.wrap(message, self.width - 4)
        for idx, line in enumerate(wrapped_message):
            if idx < self.height - 2:
                self.window.addstr(idx + 1, 2, line)
        self.window.box()
        self.window.refresh()


    def clear(self):
        self.window.clear()
        self.window.box()
        self.window.refresh()