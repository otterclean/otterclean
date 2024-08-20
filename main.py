import curses
from config.colors import init_colors
from ui.menu import MainMenu
from ui.layout import LayoutManager
from features.cleanup import perform_cleanup
from features.analysis import analyze_disk_usage
from features.docker_management import (
    prune_docker_system,
    prune_docker_images,
    prune_docker_containers,
    prune_docker_volumes,
    prune_docker_builder_cache
)
from features.system import clean_system_logs, clean_system_cache


def main(stdscr):
    # Başlangıç ayarları
    curses.curs_set(0)  # İmleci gizle
    init_colors()       # Renkleri başlat

    # Ana menü seçenekleri
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

    # Ana menü ve layout yöneticisi oluşturuluyor
    main_menu = MainMenu(stdscr, options)
    layout = LayoutManager(stdscr, main_menu)

    while True:
        try:
            layout.render(main_menu.get_selected_option())

            key = stdscr.getch()

            if key == curses.KEY_RESIZE:
                layout.handle_resize()
            elif key == curses.KEY_UP:
                main_menu.navigate("UP")
            elif key == curses.KEY_DOWN:
                main_menu.navigate("DOWN")
            elif key == ord('\n'):
                selected_option = main_menu.get_selected_option()

                if selected_option == 12:  # Exit option
                    break

                result = None

                if selected_option == 0:
                    result = prune_docker_system()
                elif selected_option == 1:
                    result = prune_docker_images()
                elif selected_option == 2:
                    result = prune_docker_containers()
                elif selected_option == 3:
                    result = prune_docker_volumes()
                elif selected_option == 4:
                    result = prune_docker_builder_cache()
                elif selected_option == 5:
                    # Clean Application Cache
                    result = perform_cleanup(option=6)
                elif selected_option == 6:
                    result = perform_cleanup(option=7)  # Clean User Logs
                elif selected_option == 7:
                    result = clean_system_logs(['/var/log'])
                elif selected_option == 8:
                    result = clean_system_cache(
                        ['/Library/Caches', '~/Library/Caches'])
                elif selected_option == 9:
                    result = clean_system_cache(
                        ['/System/Library/Caches', '~/Library/Caches'])
                elif selected_option == 10:
                    result = analyze_disk_usage(['/'])
                elif selected_option == 11:
                    # This option might require a submenu or additional UI for selecting caches
                    result = "Feature not implemented yet"

                if result:
                    layout.display_result(result)

                stdscr.addstr(curses.LINES - 2, 2,
                              "Operation complete. Press any key to continue.")
                stdscr.refresh()
                stdscr.getch()

        except curses.error as e:
            # Terminal boyutu çok küçük olduğunda bu hata oluşabilir
            stdscr.clear()
            stdscr.addstr(0, 0, str(e))
            stdscr.refresh()
            stdscr.getch()  # Kullanıcının bir tuşa basmasını bekle

    stdscr.clear()
    stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
