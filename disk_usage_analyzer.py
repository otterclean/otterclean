import os


def get_directory_size(path):
    """Returns the size of a directory in bytes."""
    expanded_path = os.path.expanduser(path)
    if not os.path.exists(expanded_path):
        return 0

    result = os.popen(f'du -sk "{expanded_path}"').read().strip()
    if result:
        return int(result.split()[0]) * 1024  # Convert KB to bytes
    else:
        return 0


def human_readable_size(size_in_bytes):
    """Convert size in bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.1f}{unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.1f}PB"


def scan_application_caches():
    """Scans for application caches in the user's Library/Caches directory."""
    cache_dir = os.path.expanduser("~/Library/Caches")
    app_caches = []
    total_size = 0

    for item in os.listdir(cache_dir):
        full_path = os.path.join(cache_dir, item)
        if os.path.isdir(full_path):
            try:
                size = get_directory_size(full_path)
                total_size += size
                app_caches.append((full_path, human_readable_size(size)))
            except Exception:
                pass  # Erişilemeyen dizinleri atla

    app_caches.append(("Total", human_readable_size(total_size)))
    return app_caches


def analyze_disk_usage():
    sections = {
        "Application Cache": scan_application_caches(),
        "User Logs": [
            ("~/Library/Logs", human_readable_size(get_directory_size("~/Library/Logs")))
        ],
        "System Logs": [
            ("/var/log", human_readable_size(get_directory_size("/var/log")))
        ],
        "System Cache": [
            ("/Library/Caches", human_readable_size(get_directory_size("/Library/Caches"))),
            ("~/Library/Caches", human_readable_size(get_directory_size("~/Library/Caches")))
        ]
    }

    # Calculate total for each section
    for section, items in sections.items():
        if section != "Application Cache":  # Application Cache already has a total
            total = sum(get_directory_size(path) for path, _ in items)
            items.append(("Total", human_readable_size(total)))

    return sections
