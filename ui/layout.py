import curses
from ui.details import DetailsDisplay


class LayoutManager:
    def __init__(self, stdscr, menu):
        self.stdscr = stdscr
        self.menu = menu
        self.details_display = DetailsDisplay(stdscr)
        self.window_height, self.window_width = self.stdscr.getmaxyx()

    def render(self, current_option):
        self.stdscr.clear()

        # Draw borders around the layout sections
        self.draw_borders()

        # Render the menu on the left
        self.menu.render()

        # Display details for the selected option on the right
        details = self.get_details_for_option(current_option)
        self.details_display.render(details)

        self.stdscr.refresh()


    def draw_borders(self):
        # Draw a border for the left section (menu)
        self.stdscr.attron(curses.color_pair(1))

        # Top border with title for left section
        self.stdscr.addch(2, 0, curses.ACS_ULCORNER)
        self.stdscr.addstr(2, 1, " Menu ")
        self.stdscr.hline(2, 7, curses.ACS_HLINE, self.window_width // 3 - 7)
        self.stdscr.addch(2, self.window_width // 3, curses.ACS_URCORNER)

        # Top border with title for right section
        self.stdscr.addch(2, self.window_width // 3, curses.ACS_ULCORNER)
        self.stdscr.addstr(2, self.window_width // 3 + 1, " Details ")
        self.stdscr.hline(2, self.window_width // 3 + 9, curses.ACS_HLINE,
                        self.window_width - self.window_width // 3 - 9)
        self.stdscr.addch(2, self.window_width - 1, curses.ACS_URCORNER)

        # Vertical borders
        for y in range(3, self.window_height - 4):  # Leave space for the bottom section
            self.stdscr.addch(y, 0, curses.ACS_VLINE)
            self.stdscr.addch(y, self.window_width // 3, curses.ACS_VLINE)
            self.stdscr.addch(y, self.window_width - 1, curses.ACS_VLINE)

        # Bottom border for the middle sections
        self.stdscr.addch(self.window_height - 4, 0, curses.ACS_LTEE)
        self.stdscr.hline(self.window_height - 4, 1,
                        curses.ACS_HLINE, self.window_width - 2)
        self.stdscr.addch(self.window_height - 4,
                        self.window_width - 1, curses.ACS_RTEE)

        # Separate the bottom section with a new border
        self.stdscr.addch(self.window_height - 3, 0, curses.ACS_ULCORNER)
        self.stdscr.addstr(self.window_height - 3, 1, " Bottom Section ")
        self.stdscr.hline(self.window_height - 3, 15,
                        curses.ACS_HLINE, self.window_width - 16)
        self.stdscr.addch(self.window_height - 3,
                        self.window_width - 1, curses.ACS_URCORNER)

        # Bottom border for the entire layout
        self.stdscr.addch(self.window_height - 2, 0, curses.ACS_LLCORNER)
        self.stdscr.hline(self.window_height - 2, 1,
                        curses.ACS_HLINE, self.window_width - 2)
        self.stdscr.addch(self.window_height - 2,
                        self.window_width - 1, curses.ACS_LRCORNER)

        self.stdscr.attroff(curses.color_pair(1))




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
