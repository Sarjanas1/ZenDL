# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by Shin-Yue, < https://github.com/Shin-yue >.
# and is released under the "GNU v3.0 License Agreement
#
# All rights reserved.


import typing
import shlex
import asyncio
import requests
import functools

from urllib import request
from pyquery import PyQuery
from pyrogram import filters, types, enums
from html_telegraph_poster import TelegraphPoster

from roft import self
from roft.vars import vars
from roft.core import constants
from roft.core.database.dbfuncs import is_banned_user


def command(commands: typing.Union[str, typing.List[str]]):
    return filters.command(commands, vars.CommandPrefixesBOT)


def aiowrap(func: typing.Callable) -> typing.Callable:
    @functools.wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = functools.partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run


def pinterest_url(link):
    post_request = requests.post('https://www.expertsphp.com/download.php', data={'url': link})

    request_content = post_request.content
    str_request_content = str(request_content, 'utf-8')
    download_url = PyQuery(str_request_content)('table.table-condensed')('tbody')('td')('a').attr('href')

    return download_url


# function to download video
def download_video(url):
    video_to_download = request.urlopen(url).read()
    with open('pinterest_video.mp4', 'wb') as video_stream:
        video_stream.write(video_to_download)


# function to download gif
def download_gif(url):
    gif_to_download = request.urlopen(url).read()
    with open('pinterest_gif.gif', 'wb') as content_download_gif:
        content_download_gif.write(gif_to_download)


# function to download image
def download_image(url):
    image_to_download = request.urlopen(url).read()
    with open('pinterest_iamge.jpg', 'wb') as photo_stream:
        photo_stream.write(image_to_download)


def check_user_status(func):
    @functools.wraps(func)
    async def check_user(_, message: types.Message, *args, **kwargs):
        user_banned = await is_banned_user(message.from_user.id)
        if user_banned:
            return await message.reply_text(
                text=constants.message_12,
                parse_mode=enums.parse_mode.ParseMode.HTML
            )
        else:
            return await func(_, message, *args, **kwargs)
    return check_user


def callback_user(func):
    @functools.wraps(func)
    async def cb(_, callback: types.CallbackQuery, *args, **kwargs):
        cb_data = callback.data.strip()
        cb_nano = cb_data.split(None, 1)[1]
        id, duration, user_id = cb_nano.split('|')

        if callback.from_user.id == vars.SpecialUsers:
            return await func(
                _, 
                callback, 
                *args, 
                **kwargs
            )
        if callback.from_user.id != int(user_id):
            return await callback.answer(
                text=constants.message_10,
                show_alert=True
            )
        else:
            return await func(
                _, 
                callback, 
                *args, 
                **kwargs
            )
    return cb


def authorized_users(func):
    @functools.wraps(func)
    async def wrapper(_, message: types.Message, *args, **kwargs):
        if message.from_user.id == vars.SpecialUsers:
            return await func(_, message, *args, **kwargs)
        else:
            return
    return wrapper


async def log_info(message: types.Message, args):
    text = f'🆕 <b><u>#Log {args}</u></b>\n\n'
    user = message.from_user
    if user.username:
        text += (
            f'🆔 <b>ID:</b> <code>{user.id}</code>\n'
            f'👤 <b>Name:</b> @{user.username}\n'
        )
    else:
        text += (
            f'🆔 <b>ID:</b> <code>{user.id}</code>\n'
            f'👤 <b>Name:</b> {message.from_user.mention()}\n'
        )
    try:
        return await self.send_message(
            chat_id=vars.LogGroupChatID, text=text, parse_mode=enums.parse_mode.ParseMode.HTML
        )
    except Exception as e:
        print(e)
        return


async def extract_user(_, m: types.Message) -> types.User:
    if not m.reply_to_message:
        return
    if m.reply_to_message and m.reply_to_message.from_user:
        user = m.reply_to_message.from_user
    else:
        # try:
        entities = m.entities[1] if m.text.startswith("/") else m.entities[0]
        user = await self.get_users(
            entities.user.id
            if entities.type == enums.MessageEntityType.TEXT_MENTION 
            else int(m.command[1]) 
            if m.command[1].isdecimal() 
            else m.command[1]
        )
    return user    
    

async def reason_text(_, m: types.Message) -> types.Message:
    reply = m.reply_to_message
    spilt_text = m.text.split
    if not reply and len(spilt_text()) >= 3:
        reason = spilt_text(None, 2)[2]
    elif reply and len(spilt_text()) >= 2:
        reason = spilt_text(None, 1)[1]
    else:
        reason = None
    return reason 
  

def post_telegraph(title, html_format_content):

    post_client = TelegraphPoster(use_api=True)
    auth_name = '@Yuedlbot'
    bish = 'https://t.me/Yuedlbot'
    post_client.create_api_token(auth_name)
    try:
        post_page = post_client.post(
            title=title,
            author=auth_name,
            author_url=bish,
            text=html_format_content
        )
        return post_page["url"]
    except BaseException:
        return 't.me/Yuedlbot'


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":")))
    )


def convert_bytes(size: float) -> str:
    """humanize size"""
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        t_n += 1
    return "{:.2f} {}B".format(size, power_dict[t_n])
