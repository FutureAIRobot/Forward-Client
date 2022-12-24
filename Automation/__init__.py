import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 26686963
API_HASH = "7cce2717e7e89eb534b7da973926f6c4"
USER_SESSION = "BQBYqSiNym2pnWaWy48Vga4Qw1JmNOdq-2tHZul2zEUFHy-Dxvx7DSwx1mErvsk5JXai_Aylv7hFSzQH3trdu5Mjj9xtN7FUh1eIt4XtEjLh24kKlKXwb7RwI1ZrIINRGfJ3Mf6aK1dtD3zAM3Lg_GEn88Sfkimjm4HP6UIz9jI-mRgPVuBSOLKaDe6XLpnBlqJl7i5MKjTLJquzw8umokJx9Oh0eokDLMHJ9AYlesdFTRWbQRKnuCin_ipAUWqaBTKHDNx-t5ypkOmcXvS0eKUV_0vJY7Y_Bn-pxeQQbLunCh2lz5w4Nxm-0dHT03kEnNfqzS0PM3QN2oW8a3AG8Zd2AAAAAVLx0FUA"
BOT_TOKEN = "5444048309:AAHqbcQjdlYHZXhHn6z9oU8xyjfQkYzEqHM" 
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
