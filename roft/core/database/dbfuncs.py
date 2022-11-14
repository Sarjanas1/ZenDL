from typing import Dict, List, Union

from roft.core.database import MongoClients

bans = MongoClients.bans
usersdb = MongoClients.users
chatsdb = MongoClients.chats

# banned database
async def get_banned() -> list:
    results = []
    async for user in bans.find({"user_id": {"$gt": 0}}):
        user_id = user["user_id"]
        results.append(user_id)
    return results


async def is_banned_user(user_id: int) -> bool:
    user = await bans.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_ban_user(user_id: int):
    is_banned = await is_banned_user(user_id)
    if is_banned:
        return
    return await bans.insert_one({"user_id": user_id})


async def remove_ban_user(user_id: int):
    is_banned = await is_banned_user(user_id)
    if not is_banned:
        return
    return await bans.delete_one({"user_id": user_id})


# served chats database
async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def get_served_chats() -> list:
    chats_list = []
    async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return
    return await chatsdb.delete_one({"chat_id": chat_id})


# users database
async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})
