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
        self.window.box()  # Draw the border around the section
        self.window.refresh()

    def update(self, content):
        self.render(content)

    def handle_resize(self, new_height, new_width):
        self.height, self.width = new_height, new_width
        self.window.resize(new_height, new_width)
        self.window.box()  # Redraw the border after resize
        self.window.refresh()

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

    def display_scrollable_text(self, text):
        self.window.clear()
        height, width = self.window.getmaxyx()
        lines = text.split('\n')
        current_line = 0
        while True:
            self.window.clear()
            for i in range(height - 2):
                if current_line + i < len(lines):
                    self.window.addstr(i + 1, 1, lines[current_line + i][:width - 2])
            self.window.box()  # Ensure the border is always drawn
            self.window.refresh()

            key = self.window.getch()
            if key == curses.KEY_UP and current_line > 0:
                current_line -= 1
            elif key == curses.KEY_DOWN and current_line < len(lines) - height + 2:
                current_line += 1
            elif key in [ord('q'), ord('Q'), 27]:  # Exit on 'q', 'Q', or ESC
                break
