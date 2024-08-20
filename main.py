import curses
import time
import os
from config.colors import init_colors
from ui.menu import MainMenu
from ui.layout import LayoutManager
from features.cleanup import perform_cleanup, clean_selected_app_caches
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
    curses.curs_set(0)
    init_colors()

    options = [
        "1. Comprehensive Docker Cleanup",
        "2. Remove Unused Docker Images",
        "3. Remove Stopped Containers",
        "4. Remove Unused Docker Volumes",
        "5. Clean Docker Build Cache",
        "6. Clean Application Cache",
        "7. Clean User Logs",
        "8. Clean System Logs",
        "9. Clean System Cache",
        "10. Clean All System Caches",
        "11. Disk Usage Analysis",
        "12. Clean Selected Application Caches",
        "13. Exit"
    ]

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

                operation_name = options[selected_option].split(". ", 1)[1]

                if selected_option == 11:  # Clean Selected Application Caches
                    clean_selected_app_caches(layout)
                else:
                    start_time = time.time()
                    for progress in range(101):
                        elapsed_time = time.time() - start_time
                        layout.progress_bar.update(
                            progress, operation_name, elapsed_time)
                        layout.render(selected_option)
                        time.sleep(0.05)  # Simulating operation progress

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
                        result = perform_cleanup(option=6)
                    elif selected_option == 6:
                        result = perform_cleanup(option=7)
                    elif selected_option == 7:
                        result = clean_system_logs(['/var/log'])
                    elif selected_option == 8:
                        result = clean_system_cache(
                            ['/Library/Caches', '~/Library/Caches'])
                    elif selected_option == 9:
                        result = clean_system_cache(
                            ['/System/Library/Caches', '~/Library/Caches'])
                    elif selected_option == 10:
                        result = analyze_disk_usage([os.path.expanduser('~')])

                    if result:
                        layout.display_result(str(result))

                layout.display_message(
                    "Operation complete. Press any key to continue.")
                stdscr.getch()
                layout.render(selected_option)

            elif key == curses.KEY_RIGHT:
                selected_option = main_menu.get_selected_option()
                if selected_option == 12:  # Clean Selected Application Caches
                    clean_selected_app_caches(layout)


        except curses.error as e:
            layout.display_error(f"Curses error: {str(e)}")
            stdscr.getch()

    stdscr.clear()
    stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
