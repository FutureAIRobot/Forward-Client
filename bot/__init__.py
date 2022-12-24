import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 16029596
API_HASH = "8c6b3ce7f23e51dfebbdbe98a0ee674d"
USER_SESSION = "BQBzIxSLJi_N6fYhQ6TOK9xrTUtaWiVdrdZhvRXk8QBCWj6MgHUpTbLVaRNJ761ckUNrTMGR0QDJjhNtv080ke7A4vMlkqaHnKSylRcxQcflobSBSBacusNdw3brTpWCS6qgfg-ha_L39npMTAQYqLCEq5qv5NUBPwo1LLpBMVGHIRP9pbopNGGuWn6o7YBt4e_NaAPYvy-dHzT357pLy1I89ShSPPSOVNDC6JslVVZqwt6yiOz4QsG_2wJCOBOdeDhMYFFQxJDpXBdn611MTwpXlccuTFeBLwhKJUEZDCZh0zsWX8mn9whi6eSfS7TQY-IZupG_KzvlRBjFL-BYkKqJAAAAAWHA4M8A"
BOT_TOKEN = "5975576942:AAHpaWamjCcNusVEg3rw7KhHitwmXe5Ua0Y"
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
