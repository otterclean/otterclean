import argparse
from otterclean.features import browser_cleanup, secure_delete
from otterclean.features import privacy_protection


def parse_arguments():
    parser = argparse.ArgumentParser(description="System Cleanup Utility")
    parser.add_argument("--clean-browsers", action="store_true", help="Clean browser caches")
    parser.add_argument("--secure-delete", metavar="FILE", help="Securely delete a file")
    parser.add_argument("--privacy", action="store_true", help="Clean privacy traces")
    return parser.parse_args()


def run_cli():
    args = parse_arguments()
    results = []

    if args.clean_browsers:
        results.append(browser_cleanup.clean_browser_caches())

    if args.secure_delete:
        results.append(secure_delete.secure_delete_file(args.secure_delete))

    if args.privacy:
        results.append(privacy_protection.clean_privacy_traces())

    for result in results:
        print(result)


if __name__ == "__main__":
    run_cli()