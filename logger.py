import logging
from logging.handlers import RotatingFileHandler

Programing_Try = False

def setup_logger(txt=None):
    # Log formatı
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    # Logger oluştur
    logger = logging.getLogger(name=txt)
    logger.setLevel(logging.INFO)

    # --- 1) Konsol çıktısı ---
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter(log_format))
    logger.addHandler(console)

    # --- 2) Dosyaya yazma (otomatik dönen log) ---
    file_handler = RotatingFileHandler(
        f"{txt}.log", 
        maxBytes=2_000_000,  # 2 MB : 2 000 000KB
        backupCount=5        # 5 eski log saklanır
    )
    file_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(file_handler)

    return logger

# Test
if Programing_Try :

    # Logger başlat
    logger = setup_logger(txt="omer")
    
    # fonksiyonlar deneniyor.
    logger.info("Program başladı")
    logger.debug("Debug mesajı")
    logger.warning("Bu bir uyarıdır")
    logger.error("Hata oluştu!")
    logger.critical("Kritik hata!")
