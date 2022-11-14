from pyrogram import filters, enums, types

from roft import self, logger
from roft.core import constants
from roft.core.functions import (
    log_info,
    pinterest_url, 
    check_user_status,
    download_video, 
    download_image, 
    download_gif
)
from roft.core.api.tiktok import TikTokDownloaderAPI


@self.on_message(filters.command('pints'))
@check_user_status
async def pinterest(_, m: types.Message):
    if len(m.command) < 2:
        return await m.reply_text(constants.message_23)

    content = m.text.split(None, 1)[1]
    pinterest = pinterest_url(content)
    i = await m.reply_text(constants.message_5)

    await log_info(m, args='Pinterest')
    await i.edit(constants.message_24)
    try:
        if '.mp4' in pinterest:
            download_video(pinterest)
            await m.reply_video(pinterest, caption=constants.message_28)
        elif '.gif' in pinterest:
            download_gif(pinterest)
            await m.reply_animation(pinterest, caption=constants.message_28)
        else:
            download_image(pinterest)
            await m.reply_photo(pinterest, caption=constants.message_28)
        await i.delete()
    except Exception as err:
        return await i.edit(constants.message_30.format('https://pin.it/7Dl1a6y'), disable_web_page_preview=True)
       

@self.on_message(filters.command('tiktok'))
@check_user_status
async def tiktok(_, m: types.Message):
    if len(m.command) < 2:
        text = (
            'You must send the correct url to get video from TikTok.\n'
            'Example:\n'
            '1. https://vm.tiktok.com/nq431N/\n'
            '2. https://www.tiktok.com/@avani/video/6810857914052398342\n'
        )
        return await m.reply_text(text, disable_web_page_preview=True)

    val = TikTokDownloaderAPI()
    value = m.text.split(None, 1)[1]

    if 'tiktok.com' in value and 'https://' in value:
        message_wait = await m.reply_text(constants.message_5)

        video = val.downloader(url=value, output_name='video.mp4')
        video_id = open('video.mp4', 'rb')

        if video:
            user_id = m.from_user.id
            await self.send_video(m.chat.id, video_id, caption=constants.message_28)  
        else:
            await message_wait.edit(constants.message_30)

        await message_wait.delete()  
    else:
        text = (
            'You sent the wrong link to the post, please send the correct link.\n'
            'Example:\n'
            '1. https://vm.tiktok.com/nq431N/\n'
            '2. https://www.tiktok.com/@avani/video/6810857914052398342\n'
        )
        return await self.send_message(m.chat.id, text, disable_web_page_preview=True)

    await m.delete()
