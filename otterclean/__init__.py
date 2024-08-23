# otterclean/__init__.py

# Import version information
from .version import __version__

# Import necessary modules
from .config import logger  # Use the logger from config
from . import features, ui, utils

# Initialize the logger (already configured in config)
logger.info(f"OtterClean version {__version__} initialized")

# Optionally, expose important modules or functionality at the package level
# This allows for easier access to core features:
from .features import analysis, cleanup, secure_delete
