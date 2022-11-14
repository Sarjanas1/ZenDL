import re
import string
import random
import lyricsgenius

from pyrogram import filters, types
from pyrogram.errors import BadRequest

from roft import self
from roft.vars import vars
from roft.core.functions import check_user_status, post_telegraph


api = lyricsgenius.Genius(vars.GeniusLyricsAPI)

lyrical = {}

@self.on_message(filters.command("lyrics"))
@check_user_status
async def lyrics(_, m: types.Message):
    if len(m.command) < 2:
        text = (
            "To get lyrics of the song you want, "
            "you must type the title or artist of the song.\n"
            "Example:\n"
            "1. /lyrics Justin Bieber\n"
            "2. /lyrics Justin Bieber What do you mean"
        )
        return await self.send_message(m.chat.id, text)

    value = m.text.split(None, 1)[1]
    r = api.search_song(value, get_full_info=False)

    ran_hash = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=10)
    )
    lyrics = r.lyrics
    if 'Embed' in lyrics:
        lyrics = re.sub(r"\d*Embed", "", lyrics)    
    lyrical[ran_hash] = lyrics

    artist = r.artist.replace("&", "ft")
    caption = f"<a href='{r.url}'>{r.title} - {artist}</a>\n{lyrics}"
    
    content = f"""<p align="center"><a href="#"><img src="{r.song_art_image_url}" width="100"></a></p>"""
    results = content + f"{lyrics}\n-\nVia @Yuedlbot"
    contents = results.replace("\n", "<br/>")
    telegraphurl = post_telegraph(f"{artist} - {r.title}", contents)

    try:
        kb = types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton(text=f"🎵 {r.title[:20]}", url=f"{telegraphurl}")]]
        )
        if r.song_art_image_url:
            await self.send_message(
                m.chat.id,
                text=caption,
                disable_web_page_preview=True,
                reply_markup=kb
            )
        else:
            await self.send_message(m.chat.id, f"<a href='{r.url}'>{r.title} - {artist}\n\n{r.lyrics}", disable_web_page_preview=True)
    except Exception as e:
        return await m.reply_text(str(e))

    return
