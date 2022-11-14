# Credit https://t.me/shin_yue
# Github https://github.com/Shin-yue


import asyncio
import contextlib

from pyrogram import types, filters
from pyrogram.errors import BadRequest, FloodWait
from pyrogram.enums.parse_mode import ParseMode

from roft import self
from roft.vars import vars

from roft.core import constants
from roft.core.functions import (
    extract_user,
    reason_text,
    authorized_users
)
from roft.core.database.dbfuncs import (
    add_ban_user, 
    get_served_chats, 
    is_banned_user, 
    remove_ban_user, 
    add_served_chat
)


@self.on_message(group=10)
@self.on_edited_message(group=10)
async def groups(_, m: types.Message):
    chat_id = m.chat.id
    if not chat_id:
        return
    await add_served_chat(chat_id)
    

@self.on_message(filters.command('superban'))
@authorized_users
async def superban(_, m: types.Message):
    reason = await reason_text(_, m)
    target_user = await extract_user(_, m)
    if target_user:
        if target_user.id == vars.SpecialUsers:
            return
        userGetBanned = await add_ban_user(target_user.id)
        if userGetBanned:
            text = constants.message_14.format(target_user.mention(), target_user.id)
            if reason:
                text += constants.message_19.format(reason)
            else:
                text = constants.message_14.format(target_user.mention(), target_user.id)
            await m.reply_text(text)
            try:
                await self.send_message(target_user.id, constants.message_12)
            except BadRequest as e:
                await self.send_message(vars.LogGroupChatID, str(e))
        else:
            await m.reply_text(constants.message_16)
            return 
        number_chat = 0  
        get_all_chat = await get_served_chats()
        for i in get_all_chat:
            try:
                await self.ban_chat_member(i['chat_id'], target_user.id)
                number_chat += 1
                await asyncio.sleep(1)
            except FloodWait as e:
                await asyncio.sleep(int(e.x))
            except Exception:
                pass
        text_in_chat = (
            f'🚷 <b>#Log User Superbanned!</b>\n'
            f'👤 User: {target_user.mention()} [<code>{target_user.id}</code>]\n'
            f'🏷️ Reason: {reason if reason else "Other"}\n'
            f'💭 Affected: <code>{number_chat}</code>\n'
            f'🧑🏻‍🔧 Operator: {m.from_user.mention()} [<code>{m.from_user.id}</code>]'
        )
        try:
            await self.send_message(chat_id=vars.LogGroupChatID, text=text_in_chat)
        except Exception as e:
            return await bot.send_message(chat_id=vars.LogGroupChatID, text=str(e))
    else:
        return await m.reply_text(constants.message_18)


@self.on_message(filters.command('unsuperban'))
@authorized_users
async def unban(_, m: types.Message):
    target_user = await extract_user(_, m)
    if target_user: 
        if target_user.id == vars.SpecialUsers:
            return
        try:
            ungbanUser = await remove_ban_user(target_user.id)
            if ungbanUser:
                return await m.reply_text(
                    text=constants.message_15.format(
                        user.mention(), user.id), parse_mode=ParseMode.HTML
                )
                await self.send_message(
                     target_user.id, constants.message_13, parse_mode=ParseMode.HTML
                )
            else:
                return await m.reply_text(constants.message_17)
        except BadRequest as e:
            return await self.send_message(
                chat_id=vars.LogGroupChatID, text=str(e)
            ) 
    else:
        await m.reply_text(constants.message_18)


# broadcast message
@self.on_message(filters.command('broadcast'))
@authorized_users
async def broadcast(_, m: types.Message):
    if m.reply_to_message:
        chat_id = m.chat.id
        m_id = m.reply_to_message_id
        sent = 0
        sleep = 0.1
        schats = await get_served_chats()
        chats = [int(chat['chat_id']) for chat in schats]
        reply = await m.reply_text(
            constants.message_21.format(len(chats) * sleep),
            parse_mode=ParseMode.HTML
        )
        for i in chats:
            try:
                with contextlib.suppress(Exception):
                    await self.forward_messages(i, chat_id, m_id)
                    await asyncio.sleep(sleep)
                    sent += 1
            except FloodWait as e:
                await asyncio.sleep(int(e.x))
            except Exception:
                pass
        return await reply.edit(
                   constants.message_22.format(sent), parse_mode=ParseMode.HTML
        )

    if len(m.command) < 2:
        return await m.reply_text(constants.message_20, parse_mode=ParseMode.HTML)
    text = m.text.split(None, 1)[1]
    sent = 0
    chats = []
    sleep = 0.1
    schats = await get_served_chats()
    chats.extend(int(chat["chat_id"]) for chat in schats)
    reply = await m.reply_text(
            constants.message_21.format(len(chats) * sleep),
            parse_mode=ParseMode.HTML
        )
    for i in chats:
        with contextlib.suppress(Exception):
            await self.send_message(i, text=text)
            await asyncio.sleep(sleep)
            sent += 1
    return await reply.edit(
               constants.message_22.format(sent), parse_mode=ParseMode.HTML
        )
