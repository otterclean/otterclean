# Application Title
APP_TITLE = "Clean My System TUI"

# Version Information
APP_VERSION = "1.0.0"

# Number of items in the menu
MENU_ITEM_COUNT = 13

# Minimum terminal width and height requirements
MIN_TERMINAL_WIDTH = 80
MIN_TERMINAL_HEIGHT = 24

# Disk analysis report format settings
DISK_ANALYSIS_FORMAT = {
    "size_unit": "GB",  # Display sizes in GB
    "precision": 2      # Show 2 decimal places after the point
}

# Timeouts for different processes (in seconds)
PROCESS_TIMEOUTS = {
    "cleanup": 300,     # Maximum duration for cleanup processes: 5 minutes
    "analysis": 120     # Maximum duration for disk analysis: 2 minutes
}

# Application color scheme (matches with the color pairs defined in colors.py)
COLOR_SCHEME = {
    "default": 1,
    "highlight": 2,
    "header": 3,
    "error": 4,
    "info": 5,
    "warning": 6,
    "menu": 8
}

# Other constants used throughout the application
LOG_FILE_PATH = "/var/log/clean_my_system_tui.log"
TEMP_DIR = "/tmp/clean_my_system_tui"
CACHE_DIR = "/var/cache/clean_my_system_tui"

MIN_TERMINAL_WIDTH = 80
MIN_TERMINAL_HEIGHT = 24
