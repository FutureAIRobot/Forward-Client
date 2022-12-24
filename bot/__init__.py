import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 16029596
API_HASH = "8c6b3ce7f23e51dfebbdbe98a0ee674d"
USER_SESSION = "BQA9jmRESrP82JwRGbGE0JFTKFrQIVB29cMO5So4Qn36w85vYs0ggx7FzBE2w_5fZ0EFD5IgLGHfe8Xb9UimGwFapZRlT3VJ4fzShpnQCR0a0v6zxrddEghhJ42UqpRk_hKwmOu3zh6f9KWaZG5w0f_ccHZ1uo28Fm4gIoMnMfUfSB4YFMDk0nz_at6uFMNFwEEmeNjm2LYnD8jNLdilBhPU8u5W3URm12UXDu_2VsfHD-xwqk1wpdD_1ewIPv3m0ceOOCCdft0597eBhLpuGmKGhNDH31omFGtOR_Y6eXTOh51iSEBdqA3oWzUvmbVWFmwADcd6gb4rxeiz4kOoIzzeAAAAAWHA4M8A"

BOT_TOKEN = "5975576942:AAEKAlb4FgK0CvXRxuR0x69gog2nKISTFH8"

MAINCHANNEL_ID = -1001743048821
CAPTION_TEXT = "test message"
FROMCHANNEL_ID = -1001873549778

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "automated.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
