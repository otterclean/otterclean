import curses
from config.colors import init_colors
from ui.menu import MainMenu
from ui.layout import LayoutManager
from features.cleanup import perform_cleanup
from features.analysis import analyze_disk_usage


def main(stdscr):
    # Başlangıç ayarları
    curses.curs_set(0)  # İmleci gizle
    init_colors()       # Renkleri başlat

    # Ana menü ve layout yöneticisi oluşturuluyor
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

    main_menu = MainMenu(stdscr, options)
    layout = LayoutManager(stdscr, main_menu)

    current_option = 0
    while True:
        stdscr.clear()
        layout.render(current_option)

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
                layout.display_analysis(analysis_results)
            else:
                perform_cleanup(current_option + 1)

            stdscr.addstr(curses.LINES - 2, 2,
                          "Operation complete. Press any key to continue.")
            stdscr.refresh()
            stdscr.getch()

    stdscr.clear()
    stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
