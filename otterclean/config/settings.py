import os

# Application Title
APP_TITLE = "Otter Clean"

# Version Information
APP_VERSION = "0.1.0"

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

# Determine log file path
LOGS_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
LOG_FILE_PATH = os.path.join(LOGS_DIR, 'otter_clean.log')

# Ensure the logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

# Other directories
TEMP_DIR = "/tmp/clean_my_system_tui"
CACHE_DIR = "/var/cache/clean_my_system_tui"
