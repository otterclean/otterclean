from ui.menu import MainMenu
from ui.details import DetailsDisplay


class LayoutManager:
    def __init__(self, stdscr, menu):
        self.stdscr = stdscr
        self.menu = menu
        self.details_display = DetailsDisplay(stdscr)

    def render(self, current_option):
        self.stdscr.clear()

        # Render the menu
        self.menu.render()

        # Display details for the selected option
        details = self.get_details_for_option(current_option)
        self.details_display.render(details)

        self.stdscr.refresh()

    def get_details_for_option(self, option):
        # Placeholder for actual details based on the selected option
        details_map = {
            0: "Details for option 1: Comprehensive Docker Cleanup...",
            1: "Details for option 2: Remove Unused Docker Images...",
            # Add other options here
        }

        return details_map.get(option, "No details available for this option.")
