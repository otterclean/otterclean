
# System Cleanup Project

This project provides a terminal-based user interface (TUI) for performing various system cleanup tasks, including Docker cleanup and system cache/log file cleanup. The program is written in Python and utilizes `curses` for the TUI and `tqdm` for progress bars.

## Prerequisites

- Python 3.7 or higher
- `pip` package manager (comes with Python)

## Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine:

\`\`\`bash
git clone <repository-url>
cd system_cleanup_project
\`\`\`

### 2. Run the Setup Script

This project includes a `setup.sh` script that automates the setup process, including creating a virtual environment, installing dependencies, and running the program.

To run the setup script:

\`\`\`bash
chmod +x setup.sh
./setup.sh
\`\`\`

### 3. Manual Setup (Optional)

If you prefer to manually set up the environment, follow these steps:

#### 3.1 Create and Activate a Virtual Environment

Create a virtual environment in the project directory:

\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

#### 3.2 Install Dependencies

Install the required Python packages:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

#### 3.3 Run the Program

After setting up the environment and installing dependencies, you can run the program with:

\`\`\`bash
python3 system_cleanup.py
\`\`\`

## Usage

Once the program is running, you'll see a list of cleanup options in a terminal-based user interface. Use the arrow keys to navigate and press `Enter` to select an option. The available options include:

1. Comprehensive Docker Cleanup (system prune)
2. Remove Unused Docker Images (image prune)
3. Remove Stopped Containers (container prune)
4. Remove Unused Docker Volumes (volume prune)
5. Clean Docker Build Cache (builder prune --all)
6. Clean Application Cache (~/Library/Caches/* and /Library/Caches/*)
7. Clean User Logs (~/Library/Logs/*)
8. Clean System Logs (/var/log/*)
9. Clean System Cache (/Library/Caches/* and ~/Library/Caches/*)
10. Clean All System Caches (/System/Library/Caches/* and ~/Library/Caches/*)
11. Disk Usage Analysis (Human-Readable)
   - Analyzes specific directories like Application Cache, User Logs, System Logs, and System Cache.
   - Displays the disk usage for each section in a human-readable format.
   - If a directory does not exist or an error occurs during calculation, a corresponding message is displayed.
12. Exit

Select the cleanup operation you wish to perform. The program will execute the corresponding commands and show a progress bar while the cleanup is in progress.

## Exiting the Program

To exit the program, simply select the "Exit" option from the menu.

## Troubleshooting

If you encounter any issues with missing packages or if the program fails to run:

1. Ensure that the virtual environment is activated:
   \`\`\`bash
   source venv/bin/activate
   \`\`\`

2. Reinstall the dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. If you see an error related to `tqdm`, make sure it is installed and correctly configured in the virtual environment.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
