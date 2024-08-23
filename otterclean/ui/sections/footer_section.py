import curses
from otterclean.ui.components import ProgressBar

class FooterSection:
    def __init__(self, window):
        self.window = window
        self.height, self.width = window.getmaxyx()
        self.progress_bar = ProgressBar(window, 100, 1, 0, self.width)

    def render(self, message):
        self.window.clear()
        self.window.addstr(0, 1, message[:self.width - 2])
        self.window.box()
        self.progress_bar.render()
        self.window.refresh()

    def update_progress(self, progress, operation_name, elapsed_time):
        self.progress_bar.update(progress, operation_name, elapsed_time)
        self.window.refresh()

    def handle_resize(self, new_height, new_width):
        self.height, self.width = new_height, new_width
        self.window.resize(new_height, new_width)
        self.progress_bar.width = new_width