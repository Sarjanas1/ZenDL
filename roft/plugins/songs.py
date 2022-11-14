# Copyright (c) 2018-2022 Shin-yue

import io
import os
import re
import shutil
import tempfile
import yt_dlp

from pyrogram import filters, types, enums
from pyrogram.errors import BadRequest
from pyrogram.enums.parse_mode import ParseMode
from youtubesearchpython import VideosSearch

from roft import self, logger, http
from roft.vars import vars
from roft.core import constants
from roft.core.functions import (
    aiowrap, 
    command, 
    time_to_seconds, 
    check_user_status,
    callback_user, 
    log_info
)


MAX_FILESIZE = 200000000


@aiowrap
def extract_info(instance: yt_dlp.YoutubeDL, url: str, download=True):
    return instance.extract_info(url, download)


@self.on_message(command('song'))
@check_user_status
async def song(_, m: types.Message):
    if len(m.command) < 2:
        return await m.reply_text(
            text=constants.message_6, parse_mode=ParseMode.HTML
        )

    await m.delete()
    await log_info(m, args='YouTube') 

    value = m.text.split(None, 1)[1]
    i = await m.reply_text(
            text=constants.message_5, parse_mode=ParseMode.HTML
       )
    try:
        song = VideosSearch(value, limit=10)
        result = (song.result()).get('result')
        id_1 = (result[0]['id'])
        id_2 = (result[1]['id'])
        id_3 = (result[2]['id'])
        id_4 = (result[3]['id'])
        id_5 = (result[4]['id'])
        id_6 = (result[5]['id'])
        id_7 = (result[6]['id'])
        id_8 = (result[7]['id'])
        id_9 = (result[8]['id'])
        id_10 = (result[9]['id'])
        title_1 = (result[0]['title'])
        title_2 = (result[1]['title'])
        title_3 = (result[2]['title']) 
        title_4 = (result[3]['title'])
        title_5 = (result[4]['title'])
        title_6 = (result[5]['title'])
        title_7 = (result[6]['title'])
        title_8 = (result[7]['title'])
        title_9 = (result[8]['title'])
        title_10 = (result[9]['title'])
        duration_1 = (result[0]['duration'])
        duration_2 = (result[1]['duration'])
        duration_3 = (result[2]['duration'])
        duration_4 = (result[3]['duration'])
        duration_5 = (result[4]['duration'])
        duration_6 = (result[5]['duration'])
        duration_7 = (result[6]['duration'])
        duration_8 = (result[7]['duration'])
        duration_9 = (result[8]['duration'])
        duration_10 = (result[9]['duration'])
    except Exception as e:
        return await i.edit(str(e))
    user_id = m.from_user.id
    keyboard = constants.keyboard_song(
        id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10, 
        duration_1, duration_2, duration_3, duration_4, duration_5, 
        duration_6, duration_7, duration_8, duration_9, duration_10,
        user_id, value
    )    
    await i.edit(
        text=constants.message_7.format(
            value, title_1, title_2, title_3, title_4, title_5,
            title_6, title_7, title_8, title_9,title_10
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )
    return


@self.on_callback_query(filters.regex(pattern=r'change'))
async def change(_, callback: types.CallbackQuery):
    userid = callback.from_user.id
    cb_data = callback.data.strip()
    cb_request = cb_data.split(None, 1)[1]
    try:
        id, value, user_id = cb_request.split('|')
    except Exception as e:
        return await callback.message.edit(str(e))

    if userid != int(user_id):
        return await callback.answer(
            text=constants.message_10, show_alert=True
    )
    i = int(id)
    value = str(value)
    try:
        song = VideosSearch(value, limit=10)
        result = (song.result()).get('result')
        id_1 = (result[0]['id'])
        id_2 = (result[1]['id'])
        id_3 = (result[2]['id'])
        id_4 = (result[3]['id'])
        id_5 = (result[4]['id'])
        id_6 = (result[5]['id'])
        id_7 = (result[6]['id'])
        id_8 = (result[7]['id'])
        id_9 = (result[8]['id'])
        id_10 = (result[9]['id'])
        title_1 = (result[0]['title'])
        title_2 = (result[1]['title'])
        title_3 = (result[2]['title']) 
        title_4 = (result[3]['title'])
        title_5 = (result[4]['title'])
        title_6 = (result[5]['title'])
        title_7 = (result[6]['title'])
        title_8 = (result[7]['title'])
        title_9 = (result[8]['title'])
        title_10 = (result[9]['title'])
        duration_1 = (result[0]['duration'])
        duration_2 = (result[1]['duration'])
        duration_3 = (result[2]['duration'])
        duration_4 = (result[3]['duration'])
        duration_5 = (result[4]['duration'])
        duration_6 = (result[5]['duration'])
        duration_7 = (result[6]['duration'])
        duration_8 = (result[7]['duration'])
        duration_9 = (result[8]['duration'])
        duration_10 = (result[9]['duration'])
    except Exception as e:
        return await callback.message.edit(str(e))
        
    if i == 1:
        keyboard = constants.keyboard_song2(
            id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10, 
            duration_1, duration_2, duration_3, duration_4, duration_5, 
            duration_6, duration_7, duration_8, duration_9, duration_10,
            user_id, value
        )
        await callback.edit_message_text(
            text=constants.message_7.format(
                value, title_1, title_2, title_3, title_4, title_5,
                title_6, title_7, title_8, title_9,title_10
            ),
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )
        await callback.answer()
        return
    if i == 2:
        keyboard = constants.keyboard_song(
            id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10, 
            duration_1, duration_2, duration_3, duration_4, duration_5, 
            duration_6, duration_7, duration_8, duration_9, duration_10,
            user_id, value
        )
        await callback.edit_message_text(
            text=constants.message_7.format(
                value, title_1, title_2, title_3, title_4, title_5,
                title_6, title_7, title_8, title_9,title_10
            ),
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )
        await callback.answer()
        return
        
    
@self.on_callback_query(filters.regex(pattern=r'download'))
@callback_user
async def download_cb(_, callback: types.CallbackQuery):
    cb_data = callback.data.strip()
    cb_nano = cb_data.split(None, 1)[1]
    id, duration, user_id = cb_nano.split('|')
     
    if duration == 'None':
        return await callback.answer(
            constants.message_9, show_alert=True
        )

    dur = int(time_to_seconds(duration))
    if dur > vars.MusicDurationLimit:
        return await callback.answer(
            constants.message_11, show_alert=True
        )

    await callback.message.edit(constants.message_5)

    url = (f'https://youtube.com/watch?v={id}')
    with tempfile.TemporaryDirectory() as tempdir:
        path = os.path.join(tempdir, 'ytdl')

    ydl = yt_dlp.YoutubeDL(
        {
            'outtmpl': f'{path}/%(title)s-%(id)s.%(ext)s',
            'format': 'bestaudio[ext=m4a]',
            'max_filesize': MAX_FILESIZE,
            'noplaylist': True,
        }
    )
    try:
        yt = await extract_info(ydl, url, download=True)
    except BaseException as e:
        return await callback.message.edit(str(e))
  
    filename = ydl.prepare_filename(yt)
    thumb = io.BytesIO((await http.get(yt['thumbnail'])).content)
    thumb_name = 'thumbnail.png'
 
    await callback.message.edit('⌛ <b>Sending...</b>') 
    await self.send_chat_action(
        chat_id=callback.message.chat.id,
        action=enums.ChatAction.UPLOAD_AUDIO
    )
    try:
        if " - " in yt["title"]:
            performer, title = yt['title'].rsplit(' - ', 1)
        else:
            performer = yt.get('creator') or yt.get('uploader')
            title = yt['title']

        title2 = yt['title']
        captions = f'<a href="{url}">{title2}</a>'
        await callback.message.reply_audio(
                filename,
                title=title,
                performer=performer,
                caption=captions,
                duration=yt["duration"],
                thumb=thumb,
                parse_mode=ParseMode.HTML,
                reply_markup=constants.keyboard_down(id, duration, user_id)            
        )
        os.remove(filename)
    except BadRequest as e:
        await callback.message.reply_text(str(e))
        return
    else:
        await callback.message.delete()
    shutil.rmtree(tempdir, ignore_errors=True)


@self.on_callback_query(filters.regex(pattern=r'video_'))
@callback_user
async def video_db(_, callback: types.CallbackQuery):
    cb_data = callback.data.strip()
    cb_nano = cb_data.split(None, 1)[1]
    id, duration, user_id = cb_nano.split('|')

    url = (f'https://youtube.com/watch?v={id}')
    with tempfile.TemporaryDirectory() as tempdir:
        path = os.path.join(tempdir, 'ytdl')

    ydl = yt_dlp.YoutubeDL(
        {
            'outtmpl': f'{path}/%(title)s-%(id)s.%(ext)s',
            'format': 'best[ext=mp4]',
            'max_filesize': MAX_FILESIZE,
            'noplaylist': True,
        }
    )
    await callback.message.delete()
    try:
        yt = await extract_info(ydl, url, download=True)
    except BaseException as e:
        await callback.message.reply_text(str(e))
        return

    videofile = ydl.prepare_filename(yt)
    thumb = io.BytesIO(
        (await http.get(yt['thumbnail'])).content
    )
    thumb_name = 'thumbnail.png'
  
    await self.send_chat_action(
        chat_id=callback.message.chat.id,
        action=enums.ChatAction.UPLOAD_VIDEO
    )
    try:
        if " - " in yt["title"]:
            performer, title = yt['title'].rsplit(' - ', 1)
        else:
            performer = yt.get('creator') or yt.get('uploader')
            title = yt['title']

        title2 = yt['title']
        captions = f'<a href="{url}">{title2}</a>'
        await callback.message.reply_video(
            videofile,
            width=1920,
            height=1080,
            caption=captions,
            duration=yt['duration'],
            thumb=thumb,
            parse_mode=ParseMode.HTML
        )
        os.remove(videofile)
    except BadRequest as e:
        return await callback.message.reply_text(str(e))
 
    shutil.rmtree(tempdir, ignore_errors=True)


@self.on_callback_query(filters.regex(pattern=r'close'))
async def close_cb(_, callback: types.CallbackQuery):
    cb_data = callback.data.strip()
    cb_nano = cb_data.split(None, 1)[1]
    close, user_id = cb_nano.split('|')
    if callback.from_user.id != int(user_id):
        return await callback.answer(
            text=constants.message_10, show_alert=True
    )
    try:
        await callback.answer()
        await callback.message.delete()
    except BadRequest as e:
        return await callback.message.reply_text(str(e))
