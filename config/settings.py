# settings.py

# Uygulama Başlığı
APP_TITLE = "Clean My System TUI"

# Versiyon bilgisi
APP_VERSION = "1.0.0"

# Menüdeki öğe sayısı
MENU_ITEM_COUNT = 13

# Terminalin minimum genişlik ve yükseklik değerleri
MIN_TERMINAL_WIDTH = 80
MIN_TERMINAL_HEIGHT = 24

# Disk analiz raporları için format ayarları
DISK_ANALYSIS_FORMAT = {
    "size_unit": "GB",  # Boyutları GB cinsinden göster
    "precision": 2      # Virgülden sonra 2 basamak göster
}

# İşlemlerin yapılma süre sınırları (saniye cinsinden)
PROCESS_TIMEOUTS = {
    "cleanup": 300,     # Temizlik işlemleri için maksimum süre: 5 dakika
    "analysis": 120     # Disk analizi için maksimum süre: 2 dakika
}

# Uygulama renk şeması (colors.py dosyasındaki renk çiftleri ile eşleşir)
COLOR_SCHEME = {
    "default": 1,       # Normal metin rengi
    "highlight": 2,     # Seçili öğe rengi
    "header": 3,        # Başlık rengi
    "error": 4,         # Hata mesajları rengi
    "info": 5,          # Bilgi mesajları rengi
    "warning": 6,       # Uyarı mesajları rengi
    "menu": 8           # Menü arka plan rengi
}

# Uygulama genelinde kullanılacak olan diğer sabitler
LOG_FILE_PATH = "/var/log/clean_my_system_tui.log"
TEMP_DIR = "/tmp/clean_my_system_tui"
CACHE_DIR = "/var/cache/clean_my_system_tui"
