import curses
import time
import os
from otterclean.config import init_colors
from otterclean.ui.layout import LayoutManager
from otterclean.features import perform_cleanup, clean_selected_app_caches, get_privacy_options, clean_privacy_traces, get_application_caches
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

        layout = LayoutManager(stdscr, options)

        while True:
            try:
                layout.render()

                key = stdscr.getch()

                if key == curses.KEY_RESIZE:
                    layout.handle_resize()
                elif key == curses.KEY_UP:
                    layout.menu_section.navigate("UP")
                elif key == curses.KEY_DOWN:
                    layout.menu_section.navigate("DOWN")
                elif key == ord('\n'):
                    selected_option = layout.menu_section.get_selected_option()

                    if selected_option == len(options) - 1:  # Exit option
                        break

                    process_selected_option(layout, selected_option)

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

def process_selected_option(layout, selected_option):
    operation_name = layout.menu_section.options[selected_option]

    try:
        if selected_option == 11:  # Clean Selected Application Caches
            app_caches = get_application_caches()
            selected_caches = layout.display_app_caches(app_caches)
            if selected_caches is None:  # User pressed 'q' to quit
                return  # Return to main menu
            if selected_caches:
                result = clean_selected_app_caches(selected_caches)
                layout.display_result(result)
            else:
                layout.display_operation_message("No caches selected for cleaning.")
        elif selected_option == 13:  # Secure File Deletion
            file_path = layout.display_file_browser("Select file/folder to securely delete:")
            if file_path:
                method = layout.display_deletion_methods()
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
                        layout.display_result(result)
                    else:
                        layout.display_operation_message("Operation cancelled")
                else:
                    layout.display_operation_message("No deletion method selected")
            else:
                layout.display_operation_message("No file/folder selected")
        else:
            start_time = time.time()
            for progress in range(101):
                elapsed_time = time.time() - start_time
                layout.footer_section.update_progress(progress, operation_name, elapsed_time)
                layout.render()
                time.sleep(0.05)  # Simulating operation progress

            result = perform_operation(selected_option, layout)
            layout.display_result(result)

        layout.display_operation_message("Operation complete. Press any key to continue.")
        layout.stdscr.getch()
    except Exception as e:
        layout.display_error(f"An error occurred: {str(e)}")
        layout.stdscr.getch()

def perform_operation(selected_option, layout):
    if selected_option == 0:
        return prune_docker_system()
    elif selected_option == 1:
        return prune_docker_images()
    elif selected_option == 2:
        return prune_docker_containers()
    elif selected_option == 3:
        return prune_docker_volumes()
    elif selected_option == 4:
        return prune_docker_builder_cache()
    elif selected_option == 5:
        return perform_cleanup(option=6)
    elif selected_option == 6:
        return perform_cleanup(option=7)
    elif selected_option == 7:
        return clean_system_logs(['/var/log'])
    elif selected_option == 8:
        return clean_system_cache(['/System/Library/Caches', '/Library/Caches'], layout)
    elif selected_option == 9:
        return clean_system_cache(['/System/Library/Caches', '~/Library/Caches'], layout)
    elif selected_option == 10:
        return analyze_disk_usage([os.path.expanduser('~')])
    elif selected_option == 12:
        return clean_browser_caches()
    elif selected_option == 14:  # Privacy Protection
        privacy_options = get_privacy_options()
        selected_privacy_options = layout.display_privacy_options(privacy_options)
        if selected_privacy_options:
            return clean_privacy_traces(selected_privacy_options)
        else:
            return "No privacy items selected for cleaning."
    else:
        return "Invalid option selected"

def run():
    curses.wrapper(main)

if __name__ == "__main__":
    run()