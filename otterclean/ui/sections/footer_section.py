import curses
from otterclean.ui.components import ProgressBar


class FooterSection:
    def __init__(self, window):
        self.window = window
        self.height, self.width = window.getmaxyx()
        self.progress_bar = ProgressBar(window, 100, 0, 0, self.width)
        self.show_progress = False
        self.default_help_text = "^Q:Quit | ^↑↓:Navigate | ^Enter:Select | ^H:Help"
        self.current_help_text = self.default_help_text

    def render(self):
        self.window.clear()
        self.window.box()  # Draw the border around the footer section
        if self.show_progress:
            self.progress_bar.render()
        else:
            self.render_help_text()
        self.window.refresh()

    def render_help_text(self):
        self.window.addstr(0, 1, self.current_help_text[:self.width - 2])

    def update_progress(self, progress, operation_name, elapsed_time):
        if self.show_progress:
            self.progress_bar.update(progress, operation_name, elapsed_time)
            self.window.refresh()

    def start_progress(self):
        self.show_progress = True
        self.render()

    def stop_progress(self):
        self.show_progress = False
        self.render()

    def handle_resize(self, new_height, new_width):
        self.height, self.width = new_height, new_width
        self.window.resize(new_height, new_width)
        self.progress_bar.width = new_width

    def display_message(self, message, duration=3):
        original_show_progress = self.show_progress
        self.show_progress = False
        self.window.clear()
        self.window.box()  # Draw the border around the footer section
        self.window.addstr(0, 1, message[:self.width - 2])
        self.window.refresh()
        curses.napms(duration * 1000)  # Display message for specified duration
        self.show_progress = original_show_progress
        self.render()

    def set_help_text(self, text):
        self.current_help_text = text
        self.render()

    def reset_help_text(self):
        self.current_help_text = self.default_help_text
        self.render()
