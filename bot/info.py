from os import getenv

class Config(object):
      CAPTION_POSITION = "bottom"

      ADMIN_USERNAME = "TTYUIOPTSREW"
      ADMIN_ID = "1903280447"
      DB_URL = "mongodb+srv://Channel-Automation-Robot:seCWS0GPZS4WIveQ@cluster0.r8flwuy.mongodb.net/?retryWrites=true&w=majority"
     
      FILES_FROM_CHANNEL = "@bdbdhdhvh"       
      FILES_TO_CHANNEL = -1001531149575

      FILES_CAPTION = "HQFilms4U"

      FILTERCHANNEL_ID =  -1001743048821   

      MULTI_CHANNEL_FORWARD_IDS = list(x for x in getenv("CHANNEL_ID", "-1001688669689:-1001641840781").replace("\n", " ").split(' '))

      MEDIACOPY_ID = -1001774936179
