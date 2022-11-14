import time, datetime, platform, psutil

from pyrogram import __version__
from pyrogram import types, filters

from roft import self
from roft.core.functions import authorized_users
from roft.core.database.dbfuncs import get_served_chats, get_served_users


@self.on_message(filters.command('ping'))
@authorized_users
async def ping(_, m: types.Message):
    first = datetime.datetime.now()
    sent = await m.reply_text("<b>Pong!</b>")
    second = datetime.datetime.now()
    await sent.edit(
        f"<b>Pong!</b> <code>{(second - first).microseconds / 1000}</code>ms"
    )


@self.on_message(filters.command('system'))
@authorized_users
async def system(_, m: types.Message):
    cpu = psutil.cpu_percent()
    vers = platform.python_version()
    user = len(await get_served_users())
    chat = len(await get_served_chats())
    yues = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
    text = (
        f"📊 <b>YueDL Systems:</b>\n"
        f" • <b>Users:</b> <code>{user}</code>\n"
        f" • <b>Chats:</b> <code>{chat}</code>\n"
        f" • <b>CPU:</b> <code>{cpu}</code>\n"
        f" • <b>Python:</b> <code>{vers}</code>\n"
        f" • <b>Pyrogram:</b> <code>{__version__}</code>\n"
        f" • <b>Start_time:</b> <code>{yues}</code>"
    )
    return await m.reply_text(text)
