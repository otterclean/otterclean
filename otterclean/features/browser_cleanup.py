import os
import shutil

def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

def clean_chrome_cache():
    chrome_cache_path = os.path.expanduser("~/Library/Caches/Google/Chrome/Default/Cache")
    if os.path.exists(chrome_cache_path):
        size = get_directory_size(chrome_cache_path)
        shutil.rmtree(chrome_cache_path)
        return f"Chrome cache cleaned: {chrome_cache_path}", human_readable_size(size)
    return "Chrome cache not found", "0 B"

def clean_firefox_cache():
    firefox_cache_path = os.path.expanduser("~/Library/Caches/Firefox")
    if os.path.exists(firefox_cache_path):
        size = get_directory_size(firefox_cache_path)
        shutil.rmtree(firefox_cache_path)
        return f"Firefox cache cleaned: {firefox_cache_path}", human_readable_size(size)
    return "Firefox cache not found", "0 B"

def clean_safari_cache():
    safari_cache_path = os.path.expanduser("~/Library/Caches/com.apple.Safari")
    if os.path.exists(safari_cache_path):
        size = get_directory_size(safari_cache_path)
        shutil.rmtree(safari_cache_path)
        return f"Safari cache cleaned: {safari_cache_path}", human_readable_size(size)
    return "Safari cache not found", "0 B"

def get_browser_caches():
    return [
        ("Chrome", clean_chrome_cache),
        ("Firefox", clean_firefox_cache),
        ("Safari", clean_safari_cache)
    ]

def clean_browser_caches(selected_browsers):
    results = []
    for browser, clean_func in get_browser_caches():
        if browser in selected_browsers:
            result, size = clean_func()
            results.append(f"{result} ({size})")
    return "\n".join(results)