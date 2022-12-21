from pyrogram import Client, __version__

from bot import API_HASH, APP_ID, LOGGER, \
    USER_SESSION


class User(Client):
    def __init__(self):
        super().__init__(
            "Clientbot",
            api_hash=API_HASH,
            api_id=APP_ID,
            session_string=USER_SESSION,
            workers=20,
#            plugins={
#                "root": "AutoForward/plugins"
#            }
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        try: await self.export_session_string()
        except: pass
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
