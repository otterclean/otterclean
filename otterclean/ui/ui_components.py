import curses
import textwrap
import os
from otterclean.ui.file_browser import FileBrowser

class UIComponents:
    @staticmethod
    def display_message(window, message):
        height, width = window.getmaxyx()
        window.clear()
        wrapped_message = textwrap.wrap(message, width - 4)
        for idx, line in enumerate(wrapped_message):
            if idx < height - 2:
                window.addstr(idx + 1, 2, line)
        window.box()
        window.refresh()
        window.getch()

    @staticmethod
    def get_confirmation(window, message):
        height, width = window.getmaxyx()
        window.clear()
        wrapped_message = textwrap.wrap(message, width - 4)
        for idx, line in enumerate(wrapped_message):
            if idx < height - 4:
                window.addstr(idx + 1, 2, line)
        window.addstr(height - 2, 2, "Press 'y' to confirm or any other key to cancel")
        window.box()
        window.refresh()
        key = window.getch()
        return key in [ord('y'), ord('Y')]

    @staticmethod
    def display_error(window, error_message):
        height, width = window.getmaxyx()
        window.clear()
        window.attron(curses.color_pair(4))  # Assuming color pair 4 is for errors
        wrapped_message = textwrap.wrap(f"ERROR: {error_message}", width - 4)
        for idx, line in enumerate(wrapped_message):
            if idx < height - 2:
                window.addstr(idx + 1, 2, line)
        window.attroff(curses.color_pair(4))
        window.box()
        window.refresh()
        window.getch()

    @staticmethod
    def select_from_options(window, options, prompt):
        height, width = window.getmaxyx()
        current_selection = 0
        scroll_offset = 0

        while True:
            window.clear()
            window.addstr(1, 2, prompt)
            max_display = height - 6
            display_range = range(scroll_offset, min(scroll_offset + max_display, len(options)))

            for idx, option in enumerate(options[scroll_offset:scroll_offset + max_display]):
                y = idx + 3
                if idx + scroll_offset == current_selection:
                    window.attron(curses.A_REVERSE)
                window.addstr(y, 2, f"{option[:width-4]}")
                if idx + scroll_offset == current_selection:
                    window.attroff(curses.A_REVERSE)

            window.addstr(height - 2, 2, "Use arrow keys to move, ENTER to select")
            window.box()
            window.refresh()

            key = window.getch()
            if key == curses.KEY_UP and current_selection > 0:
                current_selection -= 1
                if current_selection < scroll_offset:
                    scroll_offset -= 1
            elif key == curses.KEY_DOWN and current_selection < len(options) - 1:
                current_selection += 1
                if current_selection >= scroll_offset + max_display:
                    scroll_offset += 1
            elif key == ord('\n'):
                return options[current_selection]

    @staticmethod
    def get_password(window, prompt):
        curses.echo()
        window.addstr(window.getmaxyx()[0] - 1, 0, prompt)
        password = window.getstr().decode('utf-8')
        curses.noecho()
        window.addstr(window.getmaxyx()[0] - 1, 0, " " * len(prompt))
        return password

    @staticmethod
    def get_password_in_details(window, prompt):
        height, width = window.getmaxyx()
        window.clear()
        window.addstr(1, 2, prompt)
        window.refresh()
        curses.echo()
        password = window.getstr(2, 2, 30).decode('utf-8')
        curses.noecho()
        window.clear()
        window.refresh()
        return password

    @staticmethod
    def select_multiple_options(window, options, prompt):
        height, width = window.getmaxyx()
        selected_options = []
        current_selection = 0
        scroll_offset = 0
        max_display = height - 7  # Başlık, prompt ve footer için yer bırakıyoruz

        while True:
            window.clear()
            window.addstr(1, 2, prompt)

            for idx, option in enumerate(options[scroll_offset:scroll_offset + max_display]):
                y = idx + 3
                if y >= height - 4:
                    break

                if idx + scroll_offset == current_selection:
                    window.attron(curses.A_REVERSE)

                marker = 'X' if idx + scroll_offset in selected_options else ' '
                display_text = f"[{marker}] {option[:width - 6]}"
                window.addstr(y, 2, display_text)

                if idx + scroll_offset == current_selection:
                    window.attroff(curses.A_REVERSE)

            # Scroll bar
            if len(options) > max_display:
                scroll_height = int(max_display * (max_display / len(options)))
                scroll_pos = int((scroll_offset / len(options)) * max_display)
                for i in range(max_display):
                    if scroll_pos <= i < scroll_pos + scroll_height:
                        window.addstr(i + 3, width - 2, "█")
                    else:
                        window.addstr(i + 3, width - 2, "│")

            window.addstr(height - 3, 2, "↑↓: Navigate | SPACE: Select/Deselect | ENTER: Confirm | Q: Quit")
            window.box()
            window.refresh()

            try:
                key = window.getch()
            except curses.error:
                continue

            if key == ord('q'):
                return None
            elif key == curses.KEY_UP:
                if current_selection > 0:
                    current_selection -= 1
                    if current_selection < scroll_offset:
                        scroll_offset = max(0, scroll_offset - 1)
            elif key == curses.KEY_DOWN:
                if current_selection < len(options) - 1:
                    current_selection += 1
                    if current_selection >= scroll_offset + max_display:
                        scroll_offset = min(len(options) - max_display, scroll_offset + 1)
            elif key == ord(' '):
                if current_selection in selected_options:
                    selected_options.remove(current_selection)
                else:
                    selected_options.append(current_selection)
            elif key == ord('\n'):
                return [options[i] for i in selected_options]

        return None

    @staticmethod
    def display_privacy_options(window, options):
        return UIComponents.select_multiple_options(window, options, "Select privacy items to clean:")

    @staticmethod
    def update_privacy_selection(window, options, selected_options, current_selection):
        height, width = window.getmaxyx()
        for i, option in enumerate(options):
            y = 5 + i
            if i == current_selection:
                window.attron(curses.A_REVERSE)
            marker = 'X' if i in selected_options else ' '
            window.addstr(y, 2, f"[{marker}] {option[:width-6]}")
            if i == current_selection:
                window.attroff(curses.A_REVERSE)
        window.refresh()

    @staticmethod
    def get_file_or_folder(window, prompt):
        height, width = window.getmaxyx()
        window.clear()
        window.addstr(1, 2, prompt)
        window.refresh()
        browser = FileBrowser(window.subwin(height - 4, width - 4, 2, 2))
        return browser.run()

    @staticmethod
    def select_deletion_method(window):
        methods = ["simple", "dod", "gutmann"]
        descriptions = [
            "Simple: Overwrite once with random data",
            "DoD: 3 passes of overwriting",
            "Gutmann: 35 passes of overwriting (most secure, but very slow)"
        ]
        options = [f"{method}: {desc}" for method, desc in zip(methods, descriptions)]
        selected = UIComponents.select_from_options(window, options, "Select secure deletion method:")
        return methods[options.index(selected)]

class ProgressBar:
    def __init__(self, window, total, y, x, width):
        self.window = window
        self.total = total
        self.current_progress = 0
        self.y = y
        self.x = x
        self.width = width
        self.operation_name = ""
        self.elapsed_time = 0

    def update(self, progress, operation_name, elapsed_time):
        self.current_progress = progress
        self.operation_name = operation_name
        self.elapsed_time = elapsed_time
        self.render()

    def render(self):
        bar_width = self.width - 2
        filled = int(self.current_progress / self.total * bar_width)

        self.window.addstr(self.y, self.x, "[" + "=" * filled + " " * (bar_width - filled) + "]")
        progress_text = f"{self.operation_name} - {self.current_progress}% Complete"
        self.window.addstr(self.y, self.x + 1, progress_text[:bar_width])
        time_text = f"Time: {self.elapsed_time:.1f}s"
        self.window.addstr(self.y, self.width - len(time_text) - 1, time_text)
        self.window.refresh()

    @staticmethod
    def get_file_or_folder(window, prompt):
        height, width = window.getmaxyx()
        window.clear()
        window.box()
        window.addstr(1, 2, prompt)
        window.refresh()

        # Alt pencere için güvenli boyutlar hesaplayalım
        sub_height = max(3, height - 6)  # En az 3 satır
        sub_width = max(20, width - 4)  # En az 20 sütun
        sub_begin_y = min(3, height - sub_height)
        sub_begin_x = 2

        try:
            sub_win = window.derwin(sub_height, sub_width, sub_begin_y, sub_begin_x)
            browser = FileBrowser(sub_win)
            return browser.run()
        except curses.error:
            window.addstr(height - 2, 2, "Error: Window too small for file browser")
            window.refresh()
            window.getch()
            return None