from os import getenv

class Config(object):      
      ADMIN_ID = "1903280447"     
      ADMINS = 1903280447
      FILES_FROM_CHANNEL = -1001667023505       
      FILES_TO_CHANNEL = -1001531149575
      FILES_CAPTION = "@HQFilms4U"
      AUTO_FILTER_CHANNEL =  -1001743048821   
      MULTIFORWARD_ID = list(x for x in getenv("CHANNEL_ID", "-1001793975460:-1001840022987").replace("\n", " ").split(' '))

