import os
import shutil
import subprocess

def get_privacy_options():
    return [
        "Chrome browsing history",
        "System clipboard",
        "Recent items",
        "Trash"
    ]

def empty_trash():
    try:
        subprocess.run(["osascript", "-e", 'tell app "Finder" to empty trash'], check=True)
        return "Trash emptied successfully"
    except subprocess.CalledProcessError as e:
        return f"Failed to empty Trash: {str(e)}"

def clean_privacy_traces(selected_options):
    results = []

    if "Chrome browsing history" in selected_options:
        chrome_history_path = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/History")
        if os.path.exists(chrome_history_path):
            try:
                os.remove(chrome_history_path)
                results.append("Chrome browsing history cleared")
            except Exception as e:
                results.append(f"Failed to clear Chrome history: {str(e)}")

    if "System clipboard" in selected_options:
        try:
            os.system("pbcopy < /dev/null")  # MacOS specific
            results.append("System clipboard cleared")
        except Exception as e:
            results.append(f"Failed to clear clipboard: {str(e)}")

    if "Recent items" in selected_options:
        recent_items_path = os.path.expanduser("~/Library/Application Support/com.apple.sharedfilelist/")
        if os.path.exists(recent_items_path):
            try:
                for item in os.listdir(recent_items_path):
                    if item.endswith(".sfl2"):
                        os.remove(os.path.join(recent_items_path, item))
                results.append("Recent items cleared")
            except Exception as e:
                results.append(f"Failed to clear recent items: {str(e)}")

    if "Trash" in selected_options:
        results.append(empty_trash())

    return "\n".join(results)