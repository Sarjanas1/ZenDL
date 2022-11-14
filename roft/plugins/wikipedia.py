from pyrogram import types, filters
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty

from roft import self
from roft.core.functions import check_user_status

from roft.core.api.imbd import search_movie
from roft.core.api.wikipedia import WikipediaContent


@self.on_message(filters.command('wiki'))
@check_user_status
async def wikipedia(_, m: types.Message):
    if len(m.command) != 2:
        text = 'Send me any word and I will look it up on Wikipedia.'
        return await m.reply_text(text)

    enums = m.text.split(" ", 1)[1]
    content = m.text.replace('/wiki', enums)
    try:
        await self.send_message(m.chat.id, WikipediaContent(content))           
    except Exception as e:
        return await m.reply_text('The encyclopedia has no information about it.')


@self.on_message(filters.command('imdb'))
async def imbd(_, m: types.Message):
    if ' ' in m.text:
        val, title = m.text.split(None, 1)
        movies = await search_movie(title, bulk=True)
        i = await m.reply_text('🔍 <b>Searching...</b>')

        if not movies:
            return await i.edit('❌ <b>No result found.</b>')

        keyb = [
            [
                types.InlineKeyboardButton(
                    text=f"{movie.get('title')} - {movie.get('year')}",
                    callback_data=f"imdb#{movie.movieID}")                   
            ]  
                    for movie in movies  
                    
        ]
        await i.edit('🎬 This is the Imdb result I found.', reply_markup=types.InlineKeyboardMarkup(keyb))       
    else:
        return await m.reply_text('Give me a movie or series name.')


@self.on_callback_query(filters.regex('^imdb'))
async def imdbcb(_, c: types.CallbackQuery):
    i, movie = c.data.split('#')
    imdb = await search_movie(query=movie, id=True)  

    kb = types.InlineKeyboardMarkup([
        [types.InlineKeyboardButton(
             text=f"{imdb.get('title')[:20]}", url=imdb["url"])]
        ]
    )
   
    m = c.message.reply_to_message or c.message
    if imdb:
        ImdbCaption = (
            "<b>Title:</b> <a href={url}>{title}</a>\n<b>Type:</b> {kind}\n<b>Genre:</b> {genres}\n"
            "<b>A.K.A:</b> {aka}\n\n<b>Duration:</b> {runtime} minutes\n<b>Rating:</b> {rating} (<code>{votes}</code> votes)\n"
            "<b>Realese Date:</b> {release_date}\n<b>Certificates:</b> {certificates}\n\n<b>Writers:</b> {writer}\n<b>Director:</b> {director}\n<b>Countries:</b> {countries}\n<b>Languages:</b> {languages}\n"
        ) 
        caption = ImdbCaption.format(
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            kind = imdb['kind'],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"][:25],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url'],
            **locals()
        )
    else:
        caption = '❌ <b>No result found.</b>'

    if imdb.get('poster'):
        try:
            await c.message.reply_photo(photo=imdb['poster'], caption=caption, reply_markup=kb)
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            photo = imdb.get('poster')
            poster = photo.replace('.jpg', '._V1_UX360.jpg')
            await c.message.reply_photo(photo=poster, caption=caption, reply_markup=kb)
        except Exception as e:
            await c.message.reply_text(caption, disable_web_page_preview=True, reply_markup=kb)
        await c.message.delete()
    else:
        await c.message.edit(caption, disable_web_page_preview=True, reply_markup=kb)

    await c.answer()    
