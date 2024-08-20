import curses
import os
from ui.details import DetailsDisplay
from ui.components import ProgressBar
from config.settings import MIN_TERMINAL_WIDTH, MIN_TERMINAL_HEIGHT, COLOR_SCHEME

class LayoutManager:
    def __init__(self, stdscr, menu):
        self.stdscr = stdscr
        self.menu = menu
        self.details_display = DetailsDisplay(stdscr)
        self.progress_bar = ProgressBar(stdscr, 100)
        self.check_terminal_size()
        self.window_height, self.window_width = self.stdscr.getmaxyx()
        self.menu_width = self.window_width // 3

    def check_terminal_size(self):
        height, width = self.stdscr.getmaxyx()
        if height < MIN_TERMINAL_HEIGHT or width < MIN_TERMINAL_WIDTH:
            raise curses.error(f"Terminal window too small. Please resize to at least {
                               MIN_TERMINAL_WIDTH}x{MIN_TERMINAL_HEIGHT}.")

    def handle_resize(self):
        curses.update_lines_cols()
        new_height, new_width = self.stdscr.getmaxyx()
        if new_height < MIN_TERMINAL_HEIGHT or new_width < MIN_TERMINAL_WIDTH:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"Window too small. Minimum size: {
                               MIN_TERMINAL_WIDTH}x{MIN_TERMINAL_HEIGHT}")
            self.stdscr.refresh()
            return

        curses.resizeterm(new_height, new_width)
        self.window_height, self.window_width = new_height, new_width
        self.render(self.menu.get_selected_option())
        self.stdscr.refresh()

    def render(self, current_option):
        self.stdscr.clear()
        self.draw_borders()
        self.menu.render()
        details = self.get_details_for_option(current_option)
        self.details_display.render(details)
        self.progress_bar.render()
        self.stdscr.refresh()

    def draw_borders(self):
        self.stdscr.attron(curses.color_pair(COLOR_SCHEME['default']))
        
        # Top border for left section (Menu)
        self.stdscr.addch(0, 0, curses.ACS_ULCORNER)
        self.stdscr.addstr(0, 2, "Menu")
        self.stdscr.hline(0, 7, curses.ACS_HLINE, self.window_width // 3 - 7)
        self.stdscr.addch(0, self.window_width // 3, curses.ACS_URCORNER)

        # Top border for right section (Details)
        self.stdscr.addch(0, self.window_width // 3, curses.ACS_ULCORNER)
        self.stdscr.addstr(0, self.window_width // 3 + 2, "Details")
        self.stdscr.hline(0, self.window_width // 3 + 10, curses.ACS_HLINE, 
                          self.window_width - self.window_width // 3 - 11)
        self.stdscr.addch(0, self.window_width - 1, curses.ACS_URCORNER)

        # Vertical borders
        for y in range(1, self.window_height - 3):
            self.stdscr.addch(y, 0, curses.ACS_VLINE)
            self.stdscr.addch(y, self.window_width // 3, curses.ACS_VLINE)
            self.stdscr.addch(y, self.window_width - 1, curses.ACS_VLINE)

        # Bottom border for main sections
        self.stdscr.addch(self.window_height - 3, 0, curses.ACS_LTEE)
        self.stdscr.hline(self.window_height - 3, 1, curses.ACS_HLINE, self.window_width - 2)
        self.stdscr.addch(self.window_height - 3, self.window_width - 1, curses.ACS_RTEE)

        self.stdscr.attroff(curses.color_pair(COLOR_SCHEME['default']))


    def display_result(self, result):
        """
        Displays the result of an operation in the details area.

        Args:
            result (str): The result to display.
        """
        # Clear the details area
        max_y, max_x = self.stdscr.getmaxyx()
        split_point = max_x // 3
        for y in range(3, max_y - 4):
            self.stdscr.addstr(y, split_point + 2, " " * (max_x - split_point - 4))

        # Display the result
        lines = result.split('\n')
        for idx, line in enumerate(lines):
            if 3 + idx < max_y - 4:  # Ensure we don't write beyond the bottom of the screen
                self.stdscr.addstr(3 + idx, split_point + 2,
                                line[:max_x - split_point - 4])

        self.stdscr.refresh()


    def get_details_for_option(self, option):
        details_map = {
            0: "Details for option 1: Comprehensive Docker Cleanup...",
            1: "Details for option 2: Remove Unused Docker Images...",
            2: "Details for option 3: Remove Stopped Containers...",
            3: "Details for option 4: Remove Unused Docker Volumes...",
            4: "Details for option 5: Clean Docker Build Cache...",
            5: "Details for option 6: Clean Application Cache...",
            6: "Details for option 7: Clean User Logs...",
            7: "Details for option 8: Clean System Logs...",
            8: "Details for option 9: Clean System Cache...",
            9: "Details for option 10: Clean All System Caches...",
            10: "Details for option 11: Disk Usage Analysis...",
            11: "Details for option 12: Clean Selected Application Caches...",
            12: "Details for option 13: Exit..."
        }

        return details_map.get(option, "No details available for this option.")


    def update_details(self, content):
        max_y, max_x = self.stdscr.getmaxyx()
        detail_width = max_x - self.menu_width - 1
        detail_win = self.stdscr.subwin(
            max_y - 2, detail_width, 1, self.menu_width + 1)
        detail_win.clear()
        detail_win.box()

        lines = content.split('\n')
        for i, line in enumerate(lines):
            if i >= max_y - 4:  # Leave space for borders
                break
            detail_win.addstr(i + 1, 1, line[:detail_width - 2])

        detail_win.refresh()

    def display_app_caches(self, app_caches, current_selection, selected_caches):
        max_y, max_x = self.stdscr.getmaxyx()
        detail_height = max_y - 9  # Leave space for borders, title, and legend
        detail_width = max_x - self.menu_width - 3

        # Calculate the visible range based on current_selection
        start_index = max(0, current_selection - detail_height // 2)
        end_index = min(len(app_caches), start_index + detail_height)

        content = "Select Application Caches to Clean:\n\n"
        for i in range(start_index, end_index):
            path, size = app_caches[i]
            marker = "X" if i in selected_caches else " "
            line = f"[{marker}] {os.path.basename(path)}: {size}"
            if i == current_selection:
                line = "> " + line
            else:
                line = "  " + line
            content += line + "\n"

        self.update_details(content)

        # Display scroll indicators if necessary
        if start_index > 0:
            self.stdscr.addch(3, max_x - 2, '^')
        if end_index < len(app_caches):
            self.stdscr.addch(max_y - 7, max_x - 2, 'v')

        # Add legend
        legend = [
            "↑↓: Move selection",
            "Space: Toggle selection",
            "Enter: Start cleanup",
            "Q: Return to main menu"
        ]
        for i, line in enumerate(legend):
            self.stdscr.addstr(max_y - 5 + i, self.menu_width + 2, line)

    def display_message(self, message):
        """
        Displays a message at the bottom of the screen.

        Args:
            message (str): The message to display.
        """
        max_y, max_x = self.stdscr.getmaxyx()
        self.stdscr.addstr(max_y - 1, 0, message[:max_x-1])
        self.stdscr.clrtoeol()  # Clear the rest of the line
        self.stdscr.refresh()
