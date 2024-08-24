<p align="center">
  <p align="center">
    <img src="https://github.com/user-attachments/assets/e563a3d5-ea1a-46b0-b20f-26c24acbc6cd" alt="OtterClean" width="100" height="100" />
  </p>
  <p align="center">
    Clean your system with the precision of an otter and the power of Python.
  </p>
</p>

# What's OtterClean?

OtterClean is an open-source, terminal-based system cleanup and optimization tool designed for command-line enthusiasts. It provides a user-friendly Terminal User Interface (TUI) for various system maintenance tasks, including Docker management, cache cleaning, and disk usage analysis.

<p align="center">
  <img src="https://github.com/user-attachments/assets/8f635f88-c3f0-423c-9386-ff9c42bc5951" width="270" />
  <img src="https://github.com/user-attachments/assets/8f635f88-c3f0-423c-9386-ff9c42bc5951" width="270" />
  <img src="https://github.com/user-attachments/assets/8f635f88-c3f0-423c-9386-ff9c42bc5951" width="270" />
  <img src="https://github.com/user-attachments/assets/8f635f88-c3f0-423c-9386-ff9c42bc5951" width="270" />
</p>

## Features

- Comprehensive system cleanup
- Docker management and cleanup
- Application and system cache cleaning
- Log file management
- Disk usage analysis
- User-friendly Terminal User Interface (TUI)
- Verbose mode for detailed operation information
- Logging system for tracking operations and errors

## Project Structure

```
otterclean/
├── requirements.txt           # List of project dependencies
├── setup.py                   # Script for installing the project
└── otterclean/
├── init.py            # Package initialization
├── main.py                # Main entry point of the application
├── version.py             # Version information
├── config/
│   ├── init.py        # Config package initialization
│   ├── colors.py          # Color definitions for UI
│   └── settings.py        # Application settings and constants
├── features/
│   ├── init.py        # Features package initialization
│   ├── analysis.py        # Disk usage analysis functions
│   ├── browser_cleanup.py # Browser cache cleaning functions
│   ├── cleanup.py         # General cleanup functions
│   ├── command_line_support.py  # CLI support functions
│   ├── docker_management.py     # Docker-related cleanup functions
│   ├── privacy_protection.py    # Privacy protection features
│   ├── reporting.py       # Report generation functions
│   ├── secure_delete.py   # Secure file deletion functions
│   └── system.py          # System-related cleanup functions
├── logs/                  # Directory for storing log files
├── tests/                 # Directory for unit tests
├── ui/
│   ├── init.py        # UI package initialization
│   ├── components.py      # Reusable UI components
│   ├── details.py         # Details display functionality
│   ├── file_browser.py    # File browser implementation
│   ├── layout.py          # Overall UI layout management
│   ├── menu.py            # Menu implementation
│   ├── ui_components.py   # Additional UI components
│   └── sections/
│       ├── details_section.py   # Details section of the UI
│       ├── footer_section.py    # Footer section of the UI
│       └── menu_section.py      # Menu section of the UI
└── utils/
├── init.py        # Utils package initialization
├── command_runner.py  # Utility for running system commands
├── file_system.py     # File system utility functions
└── progress.py        # Progress bar implementations
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/otterclean.git
   cd otterclean
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the package:
   ```bash
   pip install .
   ```

## Usage

Run the program with:

```bash
otterclean
```

Use the arrow keys to navigate the menu and press Enter to select an option.

### Command-line Options

- `-v` or `--verbose`: Enable verbose mode for detailed operation information
- `-h` or `--help`: Display help information and available command-line options

Example:
```bash
otterclean --verbose
```

## Available Options

1. Comprehensive Docker Cleanup
2. Remove Unused Docker Images
3. Remove Stopped Containers
4. Remove Unused Docker Volumes
5. Clean Docker Build Cache
6. Clean Application Cache
7. Clean User Logs
8. Clean System Logs
9. Clean System Cache
10. Clean All System Caches
11. Disk Usage Analysis
12. Clean Selected Application Caches
13. Privacy Protection
14. Exit

## Logging

OtterClean now includes a logging system that records important events and errors during operation. Log files are stored in the `logs` directory within the project folder. The default log file is named `otter_clean.log`.

To view the logs:
```bash
cat logs/otter_clean.log
```

## Contributing

We welcome contributions to OtterClean! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python and curses
- Thanks to all contributors who participate in this project

## Disclaimer

This software is provided as-is, and users are advised to use it at their own risk. Always ensure you have backups before performing system cleanup operations.

---
