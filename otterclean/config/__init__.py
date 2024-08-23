# config/__init__.py

from .colors import init_colors
from .settings import (
    APP_TITLE, APP_VERSION, MENU_ITEM_COUNT, MIN_TERMINAL_WIDTH, MIN_TERMINAL_HEIGHT,
    DISK_ANALYSIS_FORMAT, PROCESS_TIMEOUTS, COLOR_SCHEME, LOG_FILE_PATH, TEMP_DIR, CACHE_DIR
)

import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,  # Default log level
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)

# Initialize the logger
logger = logging.getLogger(__name__)
