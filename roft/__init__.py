# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by Shin-Yue, < https://github.com/Shin-yue >.
# and is released under the "GNU v3.0 License Agreement
#
# All rights reserved.

import httpx
import logging


# Enable the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s.%(funcName)s | %(levelname)s | %(message)s",
    datefmt="[%X]",
)

# To avoid some annoying log
logging.getLogger("pyrogram.syncer").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# httpx 
timeout = httpx.Timeout(40, pool=None)
http = httpx.AsyncClient(http2=True, timeout=timeout)


from .roft_class import RoftTelegramBot

# pyrogram.Client
self = RoftTelegramBot()
