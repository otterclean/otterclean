import os
import curses


class FileBrowser:
    def __init__(self, window):
        self.window = window
        self.current_path = os.path.expanduser("~")
        self.cursor_position = 0
        self.offset = 0
        self.items = []
        self.selected_item = None
        self.update_items()

    def update_items(self):
        self.items = [".."] + sorted([f for f in os.listdir(self.current_path) if not f.startswith('.')])

    def display(self):
        self.window.clear()
        height, width = self.window.getmaxyx()

        # Display current path
        self.window.addstr(0, 0, f"Current path: {self.current_path[:width - 1]}", curses.A_BOLD)
        self.window.addstr(1, 0, "Press 'q' to quit, 'space' to select, 'enter' to confirm", curses.A_BOLD)

        # Display items
        for idx, item in enumerate(self.items[self.offset:self.offset + height - 3]):
            y = idx + 2
            if y >= height - 1:
                break

            prefix = "[ ]"
            if item == self.selected_item:
                prefix = "[x]"

            if idx + self.offset == self.cursor_position:
                self.window.attron(curses.A_REVERSE)

            item_path = os.path.join(self.current_path, item)
            if os.path.isdir(item_path):
                self.window.addstr(y, 0, f"{prefix} [DIR] {item[:width - 10]}")
            else:
                self.window.addstr(y, 0, f"{prefix} [FILE] {item[:width - 10]}")

            if idx + self.offset == self.cursor_position:
                self.window.attroff(curses.A_REVERSE)

        self.window.refresh()

    def run(self):
        while True:
            self.display()
            key = self.window.getch()

            if key == ord('q'):
                return None
            elif key == curses.KEY_UP:
                self.cursor_position = max(0, self.cursor_position - 1)
            elif key == curses.KEY_DOWN:
                self.cursor_position = min(len(self.items) - 1, self.cursor_position + 1)
            elif key == ord(' '):  # Space to select/deselect
                selected = self.items[self.cursor_position]
                if self.selected_item == selected:
                    self.selected_item = None
                else:
                    self.selected_item = selected
            elif key == ord('\n'):  # Enter key
                selected = self.items[self.cursor_position]
                if selected == "..":
                    self.current_path = os.path.dirname(self.current_path)
                    self.cursor_position = 0
                    self.selected_item = None
                else:
                    new_path = os.path.join(self.current_path, selected)
                    if os.path.isdir(new_path):
                        self.current_path = new_path
                        self.cursor_position = 0
                        self.selected_item = None
                    elif self.selected_item:
                        return os.path.join(self.current_path, self.selected_item)
                self.update_items()

            # Adjust offset for scrolling
            height, _ = self.window.getmaxyx()
            if self.cursor_position >= self.offset + height - 3:
                self.offset = min(len(self.items) - height + 3, self.cursor_position - height + 4)
            elif self.cursor_position < self.offset:
                self.offset = max(0, self.cursor_position)