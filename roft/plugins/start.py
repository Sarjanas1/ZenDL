from pyrogram import filters, types, enums

from roft import self
from roft.vars import vars
from roft.core import constants
from roft.core.functions import check_user_status
from roft.core.database.dbfuncs import add_served_user


@self.on_message(filters.command('start'))
@check_user_status
async def start(_, m: types.Message):
    await add_served_user(m.from_user.id) 
    user = await self.get_me()
    usrn = user.username
    if m.chat.type != enums.ChatType.PRIVATE:
        text = f'<a href="https://t.me/{usrn}?start=help">Commands explanation.</a>'
        await self.send_message(m.chat.id, text, disable_web_page_preview=True) 
        return
    if len(m.text.split()) > 1:
        val = (m.text.split(None, 1)[1]).lower()
        if val == 'help':
            return await m.reply_text(constants.message_3)
    else:
        await m.reply_text(
            constants.message_1.format(
                m=m.from_user.mention(), 
                bn=usrn
            ),
            reply_markup=constants.keyboard
        )            
    return


@self.on_message(filters.group & filters.command('help'))
async def help(_, m: types.Message):
    return await m.reply_text(constants.message_3)


@self.on_callback_query(filters.regex(pattern=r'self_'))
async def cb_button(_, c: types.CallbackQuery):
    value = c.data.replace('self_', '')
    if value == 'info':
        await c.edit_message_text(
            constants.message_4.format(vars.__roft_version__), 
            disable_web_page_preview=True,
            reply_markup=constants.back_kb
        )
    elif value == 'help':
        await c.edit_message_text(constants.message_3, reply_markup=constants.back_kb)
    elif value == 'backhome':
        user = await self.get_me()
        usrn = user.username
        await c.edit_message_text(
            constants.message_1.format(
                m=c.from_user.mention(), 
                bn=usrn
            ),
            reply_markup=constants.keyboard
        )

    await c.answer()
    return           
