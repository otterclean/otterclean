import curses
import time
import os
from otterclean.config import init_colors
from otterclean.ui import MainMenu, LayoutManager
from otterclean.features import perform_cleanup, clean_selected_app_caches, get_privacy_options, clean_privacy_traces
from otterclean.features.analysis import analyze_disk_usage
from otterclean.features.docker_management import (
    prune_docker_system,
    prune_docker_images,
    prune_docker_containers,
    prune_docker_volumes,
    prune_docker_builder_cache
)
from otterclean.features.system import clean_system_logs, clean_system_cache
from otterclean.features.browser_cleanup import clean_browser_caches
from otterclean.features.secure_delete import secure_delete_file, secure_delete_folder


def main(stdscr):
    try:
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
            "Clean Browser Caches",
            "Secure File Deletion",
            "Privacy Protection",
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
                        elif selected_option == 12:
                            result = clean_browser_caches()
                        elif selected_option == 13:  # Secure File Deletion
                            file_path = layout.get_file_or_folder("Select file/folder to securely delete:")
                            if file_path:
                                method = layout.select_deletion_method()
                                if method:
                                    confirm = layout.get_confirmation(
                                        f"Are you sure you want to securely delete {file_path} using {method} method?")
                                    if confirm:
                                        if os.path.isfile(file_path):
                                            for progress in secure_delete_file(file_path, method):
                                                layout.display_operation_message(progress)
                                            result = "File deletion completed"
                                        elif os.path.isdir(file_path):
                                            for progress in secure_delete_folder(file_path, method):
                                                layout.display_operation_message(progress)
                                            result = "Folder deletion completed"
                                        else:
                                            result = "Invalid path"
                                        layout.display_operation_result(result)
                                    else:
                                        layout.display_operation_result("Operation cancelled")
                                else:
                                    layout.display_operation_result("No deletion method selected")
                            else:
                                layout.display_operation_result("No file/folder selected")
                        elif selected_option == 14:  # Privacy Protection
                            privacy_options = get_privacy_options()
                            selected_privacy_options = layout.display_privacy_options(privacy_options)

                            if selected_privacy_options:
                                result = clean_privacy_traces(selected_privacy_options)
                                layout.display_operation_result(result)
                            else:
                                layout.display_operation_result("No privacy items selected for cleaning.")


                            selected_options = []
                            current_selection = 0

                            while True:
                                key = stdscr.getch()
                                if key == curses.KEY_UP and current_selection > 0:
                                    current_selection -= 1
                                elif key == curses.KEY_DOWN and current_selection < len(privacy_options) - 1:
                                    current_selection += 1
                                elif key == ord(' '):
                                    if current_selection in selected_options:
                                        selected_options.remove(current_selection)
                                    else:
                                        selected_options.append(current_selection)
                                elif key == ord('\n'):
                                    break

                                layout.update_privacy_selection(privacy_options, selected_options, current_selection)

                            selected_privacy_options = [privacy_options[i] for i in selected_options]

                            if selected_privacy_options:
                                result = clean_privacy_traces(selected_privacy_options)
                                layout.display_operation_result(result)
                            else:
                                layout.display_operation_result("No privacy items selected for cleaning.")

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

    except KeyboardInterrupt:
        stdscr.clear()
        stdscr.refresh()
        curses.endwin()
        print("Program interrupted by user. Exiting...")

    except Exception as e:
        stdscr.clear()
        stdscr.refresh()
        curses.endwin()
        print(f"An unexpected error occurred: {str(e)}")
    pass

def run():
    curses.wrapper(main)

if __name__ == "__main__":
    curses.wrapper(main)