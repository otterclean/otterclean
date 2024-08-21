import curses
import os
import time
from tqdm import tqdm
from disk_usage_analyzer import analyze_disk_usage


def display_analysis(stdscr, analysis_results):
    stdscr.clear()
    stdscr.addstr(0, 0, "Disk Usage Analysis:\n", curses.A_BOLD)

    content = []
    for section, results in analysis_results.items():
        content.append(f"{section}:")
        for path, size in results:
            content.append(f"  {path}: {size}")
        content.append("")

    current_line = 0
    max_y, max_x = stdscr.getmaxyx()

    while True:
        stdscr.clear()
        for i, line in enumerate(content[current_line:current_line+max_y-3]):
            try:
                stdscr.addstr(i+1, 0, line[:max_x-1])
            except curses.error:
                pass

        stdscr.addstr(
            max_y-2, 0, "Press UP/DOWN to scroll, Q to return to main menu", curses.A_REVERSE)
        stdscr.refresh()
        key = stdscr.getch()

        if key == ord('q') or key == ord('Q'):
            break
        elif key == curses.KEY_DOWN and current_line < len(content) - max_y + 3:
            current_line += 1
        elif key == curses.KEY_UP and current_line > 0:
            current_line -= 1


def perform_cleanup(option, stdscr):
    curses.endwin()

    if option == 1:
        command = "docker system prune -a --volumes -f"
    elif option == 2:
        command = "docker image prune -a -f"
    elif option == 3:
        command = "docker container prune -f"
    elif option == 4:
        command = "docker volume prune -f"
    elif option == 5:
        command = "docker builder prune --all -f"
    elif option == 6:
        command = "sudo rm -rf ~/Library/Caches/* && sudo rm -rf /Library/Caches/*"
    elif option == 7:
        command = "sudo rm -rf ~/Library/Logs/*"
    elif option == 8:
        command = "sudo rm -rf /var/log/*"
    elif option == 9:
        command = "sudo rm -rf /Library/Caches/* && sudo rm -rf ~/Library/Caches/*"
    elif option == 10:
        command = "sudo rm -rf /System/Library/Caches/* && sudo rm -rf ~/Library/Caches/*"
    elif option == 11:
        # Disk Usage Analysis
        analysis_results = analyze_disk_usage()
        display_analysis(stdscr, analysis_results)
        return
    else:
        return

    with tqdm(total=100, desc="Processing", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
        for i in range(10):
            os.system(command)
            time.sleep(0.5)
            pbar.update(10)

    stdscr.clear()
    stdscr.refresh()


def clean_selected_app_caches(stdscr):
    curses.curs_set(0)
    analysis_results = analyze_disk_usage()
    app_caches = analysis_results["Application Cache"]

    current_selection = 0
    selected_caches = [False] * len(app_caches)
    scroll_offset = 0

    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()
        stdscr.addstr(
            0, 0, "Select Application Caches to Clean:\n", curses.A_BOLD)

        for i in range(scroll_offset, min(len(app_caches), scroll_offset + max_y - 3)):
            path, size = app_caches[i]
            if i == current_selection:
                stdscr.addstr(i - scroll_offset + 2, 0, "> ", curses.A_REVERSE)
            else:
                stdscr.addstr(i - scroll_offset + 2, 0, "  ")

            marker = "[x]" if selected_caches[i] else "[ ]"
            try:
                stdscr.addstr(i - scroll_offset + 2, 2,
                              f"{marker} {os.path.basename(path)}: {size}"[:max_x-4])
            except curses.error:
                pass

        stdscr.addstr(
            max_y-1, 0, "SPACE: select/deselect, ENTER: confirm, q: quit", curses.A_REVERSE)
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord(' '):
            selected_caches[current_selection] = not selected_caches[current_selection]
        elif key == curses.KEY_UP:
            if current_selection > 0:
                current_selection -= 1
                if current_selection < scroll_offset:
                    scroll_offset -= 1
        elif key == curses.KEY_DOWN:
            if current_selection < len(app_caches) - 1:
                current_selection += 1
                if current_selection >= scroll_offset + max_y - 3:
                    scroll_offset += 1
        elif key == ord('\n'):
            break
        elif key == ord('q'):
            return

    curses.endwin()
    for i, (path, _) in enumerate(app_caches):
        if selected_caches[i]:
            try:
                command = f"rm -rf '{path}'"
                os.system(command)
            except Exception as e:
                print(f"Error cleaning {path}: {str(e)}")

    stdscr.clear()
    stdscr.addstr(0, 0, "Selected caches have been cleaned.")
    stdscr.refresh()
    stdscr.getch()


def display_details(stdscr, option):
    details = f"Details for option {option}:\n"

    if option == 1:
        details += "This will remove all unused containers, networks, images, and optionally, volumes."
    elif option == 2:
        details += "This will remove all unused Docker images."
    elif option == 3:
        details += "This will remove all stopped containers."
    elif option == 4:
        details += "This will remove all unused Docker volumes."
    elif option == 5:
        details += "This will clean the Docker build cache."
    elif option == 6:
        details += "This will remove application cache files."
    elif option == 7:
        details += "This will remove user log files."
    elif option == 8:
        details += "This will remove system log files."
    elif option == 9:
        details += "This will clean system caches."
    elif option == 10:
        details += "This will clean all system caches."
    elif option == 11:
        details += "This will analyze disk usage."
    elif option == 12:
        details += "This will allow you to select and clean specific application caches."

    max_y, max_x = stdscr.getmaxyx()
    stdscr.clear()

    # Display the details on the right side
    for idx, line in enumerate(details.split('\n')):
        stdscr.addstr(3 + idx, max_x // 3 + 2, line[:max_x - (max_x // 3) - 4])

    stdscr.refresh()


def main(stdscr):
    stdscr.clear()

    options = [
        "1. Comprehensive Docker Cleanup (system prune)",
        "2. Remove Unused Docker Images (image prune)",
        "3. Remove Stopped Containers (container prune)",
        "4. Remove Unused Docker Volumes (volume prune)",
        "5. Clean Docker Build Cache (builder prune --all)",
        "6. Clean Application Cache (~/Library/Caches/* and /Library/Caches/*)",
        "7. Clean User Logs (~/Library/Logs/*)",
        "8. Clean System Logs (/var/log/*)",
        "9. Clean System Cache (/Library/Caches/* and ~/Library/Caches/*)",
        "10. Clean All System Caches (/System/Library/Caches/* and ~/Library/Caches/*)",
        "11. Disk Usage Analysis",
        "12. Clean Selected Application Caches",
        "13. Exit"
    ]

    current_option = 0

    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        # Sol ve sağ tarafı ayırmak için ekranın genişliğini üçe böler
        split_point = max_x // 3

        # Sol tarafta seçenekleri göster
        for i, option in enumerate(options):
            if i == current_option:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(3 + i, 2, option[:split_point - 4])
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(3 + i, 2, option[:split_point - 4])

        # Seçili seçenek için detayları sağ tarafta göster
        display_details(stdscr, current_option + 1)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == ord('\n'):
            if current_option == len(options) - 1:
                break
            elif current_option == 10:  # Disk Usage Analysis seçeneği
                analysis_results = analyze_disk_usage()
                display_analysis(stdscr, analysis_results)
            elif current_option == 11:  # Clean Selected Application Caches seçeneği
                clean_selected_app_caches(stdscr)
            else:
                perform_cleanup(current_option + 1, stdscr)

            stdscr.addstr(max_y - 2, 2,
                          "Operation complete. Press any key to continue.")
            stdscr.refresh()
            stdscr.getch()

    stdscr.clear()
    stdscr.refresh()


curses.wrapper(main)
