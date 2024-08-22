import curses


def init_colors():
    """
    Initializes curses color pairs. Each color pair consists of a foreground and background color.
    This function enhances the user interface by using the terminal's supported colors.
    """
    # White text on black background for normal text
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Black text on white background for the selected item
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Cyan text on black background for headers
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # Red text on black background for warnings or errors
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    # Green text on black background for informational messages
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Yellow text on black background for highlighted text
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Magenta text on black background for certain application areas
    curses.init_pair(7, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    # White text on blue background for menus
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLUE)


def get_color_pair(index):
    """
    Helper function to get a curses color pair.
    Can be used to highlight text, set background colors, etc.
    
    Args:
        index (int): The color pair index to retrieve.
    
    Returns:
        curses.color_pair: The corresponding curses color pair.
    """
    return curses.color_pair(index)
