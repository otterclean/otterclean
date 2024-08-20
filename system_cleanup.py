import curses
import os
import time
from tqdm import tqdm
from disk_usage_analyzer import analyze_disk_usage  # Disk analizini içe aktar


def display_analysis(stdscr, analysis_results):
    stdscr.clear()
    stdscr.addstr(0, 0, "Disk Usage Analysis:\n", curses.A_BOLD)

    row = 2
    for section, results in analysis_results.items():
        stdscr.addstr(row, 2, f"{section}:", curses.A_BOLD)
        row += 1
        for path, size in results:
            stdscr.addstr(row, 4, f"{path}: {size}")
            row += 1
        row += 1

    stdscr.refresh()
    stdscr.getch()


def perform_cleanup(option, stdscr):
    curses.endwin()  # curses arayüzünden çık

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

    # İlerleme çubuğunu başlat
    with tqdm(total=100, desc="Processing", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
        for i in range(10):  # Bu örnekte, ilerleme çubuğu 10 adımda tamamlanıyor
            os.system(command)  # Temizlik veya analiz komutunu çalıştır
            # İlerleme çubuğunun yavaşça dolmasını simüle etmek için
            time.sleep(0.5)
            pbar.update(10)  # Her adımda ilerleme çubuğunu %10 ilerlet

    stdscr.clear()  # curses arayüzünü tekrar başlat ve temizle
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
        "12. Exit"
    ]

    current_option = 0

    while True:
        stdscr.clear()

        for i, option in enumerate(options):
            if i == current_option:
                stdscr.addstr(i + 1, 2, option, curses.A_REVERSE)
            else:
                stdscr.addstr(i + 1, 2, option)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == ord('\n'):
            if current_option == len(options) - 1:
                break
            else:
                perform_cleanup(current_option + 1, stdscr)
                stdscr.addstr(len(options) + 2, 2,
                              "Operation complete. Press any key to continue.")
                stdscr.refresh()
                stdscr.getch()

    stdscr.clear()
    stdscr.refresh()


curses.wrapper(main)
