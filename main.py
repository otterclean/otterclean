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
        "Comprehensive Docker Cleanup",
        "Remove Unused Docker Images",
        "Remove Stopped Containers",
        "Remove Unused Docker Volumes",
        "Clean Docker Build Cache",
        "Clean Application Cache",
        "Clean User Logs",
        "Clean System Logs",
        "Clean System Cache",
        "Clean All System Caches",
        "Disk Usage Analysis",
        "Clean Selected Application Caches",
        "Exit"
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

                if selected_option == len(options) - 1:  # Exit option
                    break

                operation_name = options[selected_option]

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
                        result = clean_system_cache(['/System/Library/Caches', '/Library/Caches'], layout)
                    elif selected_option == 9:
                        result = clean_system_cache(['/System/Library/Caches', '~/Library/Caches'], layout)
                    elif selected_option == 10:
                        result = analyze_disk_usage([os.path.expanduser('~')])

                    if result:
                        if selected_option in [0, 1, 2, 3, 4]:  # Docker işlemleri
                            layout.display_operation_result(str(result))
                        else:
                            if isinstance(result, dict):
                                layout.display_result(result)
                            else:
                                layout.display_operation_result(str(result))
                        layout.stdscr.getch()

                layout.display_operation_result("Operation complete. Press any key to continue.")
                stdscr.getch()
                layout.render(selected_option)

            elif key == curses.KEY_RIGHT:
                selected_option = main_menu.get_selected_option()
                if selected_option == 11:  # Clean Selected Application Caches
                    clean_selected_app_caches(layout)

            elif key in [ord('q'), ord('Q')]:
                break

        except curses.error as e:
            layout.display_error(f"Curses error: {str(e)}")
            stdscr.getch()

    stdscr.clear()
    stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)