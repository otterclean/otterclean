# OtterClean

OtterClean is an open-source, terminal-based system cleanup and optimization tool designed for command-line enthusiasts. It provides a user-friendly Terminal User Interface (TUI) for various system maintenance tasks, including Docker management, cache cleaning, and disk usage analysis.

## Features

- Comprehensive system cleanup
- Docker management and cleanup
- Application and system cache cleaning
- Log file management
- Disk usage analysis
- User-friendly Terminal User Interface (TUI)

## Project Structure

```
otterclean/
├── main.py                    # Main entry point
├── config/
│   ├── colors.py              # Color palettes and themes
│   └── settings.py            # Application settings and constants
├── ui/
│   ├── __init__.py
│   ├── menu.py                # Menu rendering and management
│   ├── details.py             # Displaying details of selected items
│   ├── components.py          # Custom UI components (e.g., progress bar, dialogs)
│   └── layout.py              # Layout management
├── features/
│   ├── __init__.py
│   ├── cleanup.py             # System cleanup functions
│   ├── analysis.py            # Disk analysis and other analytical functions
│   ├── docker_management.py   # Docker-related cleanup and management
│   └── system.py              # General system-related functions
├── utils/
│   ├── __init__.py
│   ├── file_system.py         # File and directory operations
│   ├── command_runner.py      # Helper functions for running shell commands
│   └── progress.py            # Progress bars and loading animations
└── assets/
    ├── icons/                 # Icons or ASCII art for UI
    └── fonts/                 # Custom font files (if terminal supports)
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
