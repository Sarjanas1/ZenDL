# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by Shin-Yue, < https://github.com/Shin-yue >.
# and is released under the "GNU v3.0 License Agreement
#
# All rights reserved.


import asyncio
import importlib

from pyrogram import idle

from roft import self
from roft.plugins import all_modules
            

async def init():    
    # loaded the all modules
    for all_module in all_modules:
        print("Loaded the all modules")
        importlib.import_module("roft.plugins." + all_module)
    await self.start()
    await idle()


if __name__ == "__main__":
    # asyncio event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
