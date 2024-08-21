import os
import shutil

def clean_chrome_cache():
    chrome_cache_path = os.path.expanduser("~/Library/Caches/Google/Chrome/Default/Cache")
    if os.path.exists(chrome_cache_path):
        shutil.rmtree(chrome_cache_path)
        return f"Chrome cache cleaned: {chrome_cache_path}"
    return "Chrome cache not found"

def clean_firefox_cache():
    firefox_cache_path = os.path.expanduser("~/Library/Caches/Firefox")
    if os.path.exists(firefox_cache_path):
        shutil.rmtree(firefox_cache_path)
        return f"Firefox cache cleaned: {firefox_cache_path}"
    return "Firefox cache not found"

def clean_browser_caches():
    results = []
    results.append(clean_chrome_cache())
    results.append(clean_firefox_cache())
    return "\n".join(results)