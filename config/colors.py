import curses


def init_colors():
    """
    Curses renk çiftlerini başlatır. Her renk çifti bir ön plan ve arka plan renginden oluşur.
    Bu fonksiyon, terminalin desteklediği renkleri kullanarak arayüzü daha kullanıcı dostu hale getirir.
    """
    # Normal metin için beyaz metin, siyah arka plan
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Seçili öğe için siyah metin, beyaz arka plan
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Başlıklar için cyan metin, siyah arka plan
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # Uyarılar için kırmızı metin, siyah arka plan
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    # Bilgilendirme mesajları için yeşil metin, siyah arka plan
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Vurgulanan metin için sarı metin, siyah arka plan
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # Uygulamanın belirli alanları için magenta metin, siyah arka plan
    curses.init_pair(7, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    # Menüler için beyaz metin, mavi arka plan
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLUE)


def get_color_pair(index):
    """
    Renk çiftlerini almak için yardımcı fonksiyon. Örneğin, bir metni vurgulamak için bu fonksiyon kullanılabilir.
    """
    return curses.color_pair(index)
