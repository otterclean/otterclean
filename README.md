<p align="center">
  <p align="center">
    <img src="https://github.com/user-attachments/assets/6ef56744-8e53-42c8-b59d-4f44f6b19878" alt="OtterClean" width="500" height="100" />
  </p>
  <p align="center">
    Clean your system with the precision of an otter and the power of Python.
  </p>
</p>
<p align="center">
  <a href="https://sonarcloud.io/api/project_badges/measure?project=otterclean_otterclean&metric=security_rating">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=otterclean_otterclean&metric=security_rating" alt="GitHub Release" />
  </a>

</p>

# What's OtterClean?

---
OtterClean is an open-source, terminal-based system cleanup and optimization tool designed for command-line enthusiasts. It provides a user-friendly Terminal User Interface (TUI) for various system maintenance tasks, including Docker management, cache cleaning, and disk usage analysis.

<p align="center">
  <img src="https://github.com/user-attachments/assets/8f635f88-c3f0-423c-9386-ff9c42bc5951" width="270" />
  <img src="https://github.com/user-attachments/assets/8f635f88-c3f0-423c-9386-ff9c42bc5951" width="270" />
  <img src="https://github.com/user-attachments/assets/8f635f88-c3f0-423c-9386-ff9c42bc5951" width="270" />
  <img src="https://github.com/user-attachments/assets/8f635f88-c3f0-423c-9386-ff9c42bc5951" width="270" />
</p>

## Features

---
- Comprehensive system cleanup
- Docker management and cleanup
- Application and system cache cleaning
- Log file management
- Disk usage analysis
- User-friendly Terminal User Interface (TUI)
- Verbose mode for detailed operation information
- Logging system for tracking operations and errors

## Project Structure

---
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

---


- Python 3.7 or higher
- pip (Python package manager)

## Installation

---

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

---
Run the program with:

```bash
otterclean
```

Use the arrow keys to navigate the menu and press Enter to select an option.

### Command-line Options

---

- `-v` or `--verbose`: Enable verbose mode for detailed operation information
- `-h` or `--help`: Display help information and available command-line options

Example:
```bash
otterclean --verbose
```

## Available Options

---
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

---

OtterClean now includes a logging system that records important events and errors during operation. Log files are stored in the `logs` directory within the project folder. The default log file is named `otter_clean.log`.

To view the logs:
```bash
cat logs/otter_clean.log
```

## Contributing

---

We welcome contributions to OtterClean! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

# Frequently Asked Questions (FAQ)

## General Questions

### What is OtterClean?
OtterClean is an open-source, terminal-based system cleanup and optimization tool designed for command-line enthusiasts. It provides a user-friendly Terminal User Interface (TUI) for various system maintenance tasks.

### What operating systems does OtterClean support?
OtterClean is primarily designed for Unix-based systems, including Linux and macOS. Windows support is currently not available.

### Is OtterClean free to use?
Yes, OtterClean is completely free and open-source, licensed under the MIT License.

## Installation and Setup

### What are the system requirements for OtterClean?
OtterClean requires Python 3.7 or higher and pip (Python package manager).

### How do I install OtterClean?
You can install OtterClean by cloning the repository, setting up a virtual environment, and using pip to install the package. Detailed instructions are available in the README.md file.

### I'm having trouble installing OtterClean. What should I do?
Ensure you have the correct Python version installed and that you're following the installation steps correctly. If you're still having issues, please open an issue on our GitHub repository.

## Usage

### How do I start OtterClean?
After installation, you can start OtterClean by simply typing `otterclean` in your terminal.

### What does the verbose mode do?
Verbose mode (`otterclean --verbose`) provides more detailed information about the operations being performed, which can be helpful for troubleshooting or understanding the cleanup process.

### Can OtterClean damage my system?
While OtterClean is designed to be safe, it's always recommended to have backups before performing system cleanup operations. Use caution, especially when cleaning system caches or logs.

## Features

### What kind of cleanup operations does OtterClean perform?
OtterClean can perform various cleanup tasks, including Docker cleanup, application and system cache cleaning, log file management, and disk usage analysis.

### Does OtterClean clean browser caches?
Yes, OtterClean includes functionality to clean browser caches for popular browsers.

### Can OtterClean remove Docker images and containers?
Yes, OtterClean provides options to remove unused Docker images, stopped containers, and unused volumes.

## Troubleshooting

### Where can I find the log files?
Log files are stored in the `logs` directory within the project folder. The default log file is named `otter_clean.log`.

### OtterClean is not recognizing Docker on my system. What should I do?
Ensure that Docker is properly installed and running on your system. OtterClean requires Docker to be accessible to perform Docker-related cleanup tasks.

### I encountered an error while using OtterClean. How can I report it?
Please open an issue on our GitHub repository with details about the error, including any relevant log entries and the steps to reproduce the issue.

## Contributing

### How can I contribute to OtterClean?
We welcome contributions! Please read our CONTRIBUTING.md file for details on how to submit pull requests, report issues, or suggest improvements.

### I have an idea for a new feature. How can I suggest it?
You can suggest new features by opening an issue on our GitHub repository. Please provide as much detail as possible about the feature you're proposing.
## License

---

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

---

- Built with Python and curses
- Thanks to all contributors who participate in this project

Stats
-----
![Alt](https://repobeats.axiom.co/api/embed/d4a496d2f84389172c275f1fde99f08fbadfa61e.svg "Repobeats analytics image")

# Frequently Asked Questions (FAQ)

## General Questions

### What is OtterClean?
OtterClean is an open-source, terminal-based system cleanup and optimization tool designed for command-line enthusiasts. It provides a user-friendly Terminal User Interface (TUI) for various system maintenance tasks.

### What operating systems does OtterClean support?
OtterClean is primarily designed for Unix-based systems, including Linux and macOS. Windows support is currently not available.

### Is OtterClean free to use?
Yes, OtterClean is completely free and open-source, licensed under the MIT License.

## Installation and Setup

### What are the system requirements for OtterClean?
OtterClean requires Python 3.7 or higher and pip (Python package manager).

### How do I install OtterClean?
You can install OtterClean by cloning the repository, setting up a virtual environment, and using pip to install the package. Detailed instructions are available in the README.md file.

### I'm having trouble installing OtterClean. What should I do?
Ensure you have the correct Python version installed and that you're following the installation steps correctly. If you're still having issues, please open an issue on our GitHub repository.

## Usage

### How do I start OtterClean?
After installation, you can start OtterClean by simply typing `otterclean` in your terminal.

### What does the verbose mode do?
Verbose mode (`otterclean --verbose`) provides more detailed information about the operations being performed, which can be helpful for troubleshooting or understanding the cleanup process.

### Can OtterClean damage my system?
While OtterClean is designed to be safe, it's always recommended to have backups before performing system cleanup operations. Use caution, especially when cleaning system caches or logs.

## Features

### What kind of cleanup operations does OtterClean perform?
OtterClean can perform various cleanup tasks, including Docker cleanup, application and system cache cleaning, log file management, and disk usage analysis.

### Does OtterClean clean browser caches?
Yes, OtterClean includes functionality to clean browser caches for popular browsers.

### Can OtterClean remove Docker images and containers?
Yes, OtterClean provides options to remove unused Docker images, stopped containers, and unused volumes.

## Troubleshooting

### Where can I find the log files?
Log files are stored in the `logs` directory within the project folder. The default log file is named `otter_clean.log`.

### OtterClean is not recognizing Docker on my system. What should I do?
Ensure that Docker is properly installed and running on your system. OtterClean requires Docker to be accessible to perform Docker-related cleanup tasks.

### I encountered an error while using OtterClean. How can I report it?
Please open an issue on our GitHub repository with details about the error, including any relevant log entries and the steps to reproduce the issue.

## Contributing

### How can I contribute to OtterClean?
We welcome contributions! Please read our CONTRIBUTING.md file for details on how to submit pull requests, report issues, or suggest improvements.

### I have an idea for a new feature. How can I suggest it?
You can suggest new features by opening an issue on our GitHub repository. Please provide as much detail as possible about the feature you're proposing.
## Disclaimer

---

This software is provided as-is, and users are advised to use it at their own risk. Always ensure you have backups before performing system cleanup operations.

---
