import curses
import sys
import os
import argparse
import logging
from otterclean.config import LOG_FILE_PATH, APP_TITLE, APP_VERSION, init_colors, logger
from otterclean.ui.layout import LayoutManager
from otterclean.features import (
    perform_cleanup, clean_selected_app_caches, get_privacy_options,
    clean_privacy_traces, get_application_caches
)
from otterclean.features.analysis import analyze_disk_usage
from otterclean.features.docker_management import (
    prune_docker_system, prune_docker_images, prune_docker_containers,
    prune_docker_volumes, prune_docker_builder_cache
)
from otterclean.features.system import clean_system_logs, clean_system_cache
from otterclean.features.browser_cleanup import clean_browser_caches
from otterclean.features.secure_delete import secure_delete_file, secure_delete_folder

def setup_logging(verbose):
    """Logging yapılandırmasını yapar, verbose flag'ine göre günceller."""
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

def setup_exception_handling():
    """Exception handler'ı tanımlar ve sistem için uygular."""
    def exception_handler(exc_type, exc_value, exc_traceback):
        logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    sys.excepthook = exception_handler

def main(stdscr):
    try:
        logger.info("Starting application")
        curses.curs_set(0)
        if curses.has_colors():
            curses.start_color()
            init_colors()  # Initialize colors after curses has started
        else:
            logger.warning("Terminal does not support colors")

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
                layout.update_footer_help_text("Press 'q' to quit | Arrow keys to navigate | Enter to select")
                layout.render()

                key = stdscr.getch()
                logger.debug(f"Key pressed: {key}")

                if key == ord('h') or key == ord('H'):
                    layout.display_help()  # Display the help screen
                    stdscr.getch()  # Wait for user to press a key to return to the main screen
                    layout.render()  # Re-render the main screen after exiting help
                    continue

                if key == curses.KEY_RESIZE:
                    layout.handle_resize()
                elif key == curses.KEY_UP:
                    layout.menu_section.navigate("UP")
                elif key == curses.KEY_DOWN:
                    layout.menu_section.navigate("DOWN")
                elif key == ord('\n'):
                    selected_option = layout.menu_section.get_selected_option()
                    logger.info(f"Selected option: {options[selected_option]}")

                    if selected_option == len(options) - 1:  # Exit option
                        break

                    process_selected_option(layout, selected_option)

                elif key in [ord('q'), ord('Q')]:
                    logger.info("User chose to quit")
                    break

            except curses.error as e:
                logger.error(f"Curses error: {str(e)}")
                layout.footer_section.display_message(f"Curses error: {str(e)}", 3)

        stdscr.clear()
        stdscr.refresh()

    except KeyboardInterrupt:
        logger.info("Program interrupted by user. Exiting...")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {str(e)}")
    finally:
        logger.info("Application shutting down")

def process_selected_option(layout, selected_option):
    operation_name = layout.menu_section.options[selected_option]
    logger.info(f"Processing selected option: {operation_name}")

    try:
        layout.footer_section.start_progress()

        if selected_option == 11:  # Clean Selected Application Caches
            app_caches = get_application_caches()
            layout.display_operation_interface(
                "Clean Selected Application Caches",
                "Listing application caches...",
                "Use ↑↓ to navigate, SPACE to select/deselect, ENTER to confirm, Q to quit"
            )
            layout.footer_section.set_help_text("↑↓: Navigate | SPACE: Select/Deselect | ENTER: Confirm | Q: Quit")
            selected_caches = layout.display_app_caches(app_caches)
            if selected_caches is None:  # User pressed 'q' to quit
                logger.info("User cancelled cache selection")
                layout.footer_section.stop_progress()
                return  # Return to main menu
            if selected_caches:
                logger.info(f"Cleaning selected caches: {selected_caches}")
                result = clean_selected_app_caches(selected_caches)
                layout.display_result(result)
            else:
                logger.info("No caches selected for cleaning")
                layout.display_operation_message("No caches selected for cleaning.")
        elif selected_option == 13:  # Secure File Deletion
            layout.display_operation_interface(
                "Secure File Deletion",
                "Select a file or folder to delete securely.",
                "Use ↑↓ to navigate, ENTER to select, Q to quit"
            )
            layout.footer_section.set_help_text("↑↓: Navigate | ENTER: Select | Q: Quit")
            file_path = layout.display_file_browser("Select file/folder to securely delete:")
            if file_path is None:
                logger.info("User cancelled file selection")
                layout.footer_section.stop_progress()
                return  # Return to main menu
            if file_path:
                logger.info(f"Selected file/folder for secure deletion: {file_path}")
                layout.display_operation_interface(
                    "Secure File Deletion",
                    f"Selected: {file_path}\nChoose deletion method:",
                    "Use ↑↓ to navigate, ENTER to select, Q to quit"
                )
                layout.footer_section.set_help_text("↑↓: Navigate | ENTER: Select | Q: Quit")
                method = layout.select_deletion_method()
                if method is None:
                    logger.info("User cancelled deletion method selection")
                    layout.footer_section.stop_progress()
                    return  # Return to main menu
                logger.info(f"Selected deletion method: {method}")
                confirm = layout.get_confirmation(
                    f"Are you sure you want to securely delete {file_path} using {method} method?")
                if confirm:
                    if os.path.isfile(file_path):
                        layout.footer_section.start_progress()
                        for progress, percentage in secure_delete_file(file_path, method):
                            layout.display_operation_message(progress)
                            layout.footer_section.update_progress(percentage, "Secure File Deletion", 0)
                        layout.footer_section.stop_progress()
                        result = "File deletion completed"
                    elif os.path.isdir(file_path):
                        layout.footer_section.start_progress()
                        for progress, percentage in secure_delete_folder(file_path, method):
                            layout.display_operation_message(progress)
                            layout.footer_section.update_progress(percentage, "Secure Folder Deletion", 0)
                        layout.footer_section.stop_progress()
                        result = "Folder deletion completed"
                    else:
                        result = "Invalid path"
                    logger.info(result)
                    layout.display_result(result)
                else:
                    logger.info("User cancelled secure deletion")
                    layout.display_operation_message("Operation cancelled")
            else:
                logger.info("No file/folder selected for secure deletion")
                layout.display_operation_message("No file/folder selected")
        else:
            layout.display_operation_interface(
                operation_name,
                "Processing..."
            )
            layout.footer_section.set_help_text("Please wait...")
            result = perform_operation(selected_option, layout)
            layout.display_result(result)

        layout.footer_section.stop_progress()
        layout.footer_section.display_message("Operation complete. Press any key to continue.", 3)
        layout.stdscr.getch()
    except Exception as e:
        logger.exception(f"An error occurred during operation: {str(e)}")
        layout.footer_section.stop_progress()
        layout.display_error(f"An error occurred: {str(e)}")
        layout.stdscr.getch()
    finally:
        layout.footer_section.reset_help_text()  # Reset to default help text

def perform_operation(selected_option, layout):
    layout.footer_section.start_progress()
    result = None

    try:
        if selected_option == 0:
            logger.info("Performing comprehensive Docker cleanup")
            result = prune_docker_system()
        elif selected_option == 1:
            logger.info("Removing unused Docker images")
            result = prune_docker_images()
        elif selected_option == 2:
            logger.info("Removing stopped containers")
            result = prune_docker_containers()
        elif selected_option == 3:
            logger.info("Removing unused Docker volumes")
            result = prune_docker_volumes()
        elif selected_option == 4:
            logger.info("Cleaning Docker build cache")
            result = prune_docker_builder_cache()
        elif selected_option == 5:
            logger.info("Cleaning application cache")
            result = perform_cleanup(option=6)
        elif selected_option == 6:
            logger.info("Cleaning user logs")
            result = perform_cleanup(option=7)
        elif selected_option == 7:
            logger.info("Cleaning system logs")
            result = clean_system_logs(['/var/log'])
        elif selected_option == 8:
            logger.info("Cleaning system cache")
            result = clean_system_cache(['/System/Library/Caches', '/Library/Caches'], layout)
        elif selected_option == 9:
            logger.info("Cleaning all system caches")
            result = clean_system_cache(['/System/Library/Caches', '~/Library/Caches'], layout)
        elif selected_option == 10:
            logger.info("Performing disk usage analysis")
            result = analyze_disk_usage([os.path.expanduser('~')])
        elif selected_option == 12:  # Clean Browser Caches
            logger.info("Cleaning browser caches")
            layout.display_operation_interface(
                "Clean Browser Caches",
                "Select browser caches to clean:",
                "Use ↑↓ to navigate, SPACE to select/deselect, ENTER to confirm, Q to quit"
            )
            result = layout.display_browser_cache_selection()
            if result:
                layout.display_result(result)
        elif selected_option == 14:  # Privacy Protection
            logger.info("Starting privacy protection")
            privacy_options = get_privacy_options()
            selected_privacy_options = layout.display_privacy_options(privacy_options)
            if selected_privacy_options:
                logger.info(f"Selected privacy options: {selected_privacy_options}")
                result = clean_privacy_traces(selected_privacy_options)
            else:
                logger.info("No privacy items selected for cleaning")
                result = "No privacy items selected for cleaning."
        else:
            logger.warning(f"Invalid option selected: {selected_option}")
            result = "Invalid option selected"
    except Exception as e:
        logger.exception(f"Error during operation: {str(e)}")
        result = f"Error: {str(e)}"

    layout.footer_section.stop_progress()
    return result

def run():
    # Argument parser setup
    parser = argparse.ArgumentParser(description=f"{APP_TITLE} System Cleanup Utility v{APP_VERSION}")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")
    args = parser.parse_args()

    # Logging ve exception handling ayarları
    setup_logging(args.verbose)
    setup_exception_handling()

    try:
        # Start curses
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        # Call the main function
        main(stdscr)

    except Exception as e:
        logger.exception("An error occurred in the main function")
    finally:
        # Terminate curses
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

if __name__ == "__main__":
    run()
