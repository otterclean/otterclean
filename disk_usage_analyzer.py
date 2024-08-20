import os


def get_directory_size(path):
    """Returns the size of a directory in human-readable format."""
    expanded_path = os.path.expanduser(path)
    if not os.path.exists(expanded_path):
        return "Directory not found"

    result = os.popen(f'du -sh "{expanded_path}"').read().strip()
    if result:
        return result.split()[0]
    else:
        return "Error calculating size"


def analyze_disk_usage():
    sections = {
        "Application Cache": [
            "~/Library/Caches/JetBrains",
            "~/Library/Caches/com.spotify.client",
            "~/Library/Caches/Homebrew",
            "~/Library/Caches/Google",
            "~/Library/Caches/Firefox",
            "~/Library/Caches/Yarn",
            "~/Library/Caches/com.brave.Browser",
        ],
        "User Logs": [
            "~/Library/Logs"
        ],
        "System Logs": [
            "/var/log"
        ],
        "System Cache": [
            "/Library/Caches",
            "~/Library/Caches"
        ]
    }

    analysis_results = {}
    for section, paths in sections.items():
        section_result = []
        for path in paths:
            size = get_directory_size(path)
            section_result.append((path, size))
        analysis_results[section] = section_result

    return analysis_results
