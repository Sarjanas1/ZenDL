# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by Shin-Yue, < https://github.com/Shin-yue >.
# and is released under the "GNU v3.0 License Agreement
#
# All rights reserved.

import time
import logging
import psutil
import datetime

from pyrogram.errors import BadRequest
from pyrogram.enums.parse_mode import ParseMode
from pyrogram import Client, __version__ as vers

from .vars import vars


log = logging.getLogger(__name__)

class RoftTelegramBot(Client):
    def __init__(self):
        roft = self.__class__.__name__.lower()

        super().__init__(
            name=roft,
            api_id=vars.ApiID,
            api_hash=vars.ApiHASH,  
            bot_token=vars.TelegramBot,
            in_memory=True
        ) 
    async def start(self):
        await super().start()

        self.me = await self.get_me()
        self.username = self.me.username
        self.first_name = self.me.first_name
        self.start_time = time.time()

        log.info(
            "YueDL music running with Pyrogram v%s (Layer %s) started on @%s. Hi!",
            vers,
            self.me.username,
        )
        bot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        start_message = (
            f'<b>{self.first_name} Actived</b>\n'
            f'    <b>version:</b> <code>v{vars.__roft_version__}</code>\n'
            f'    <b>pyrogram:</b> <code>v{vers}</code>\n'
            f'    <b>start_time:</b> <code>{bot_time}</code>'
        )
        await self.send_message(
            chat_id=vars.LogGroupChatID, text=start_message
        )
    async def stop(self):
        await super().stop()
        log.warning("YueDL Stopped")
