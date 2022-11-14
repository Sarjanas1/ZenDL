from pyrogram import Client
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

from roft import logger, self
from roft.vars import vars


MongoDB = (
    'mongodb+srv://rizexx:bdg12345..@cluster0.qzxaj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
)
if vars.MongoDatabaseURI is None:
    logger.warning(
        'Database not found, please add the mongo uri database'
    )
    self_get = self.get_me()
    usernamee = self_get.username

    MongoAsync = AsyncIOMotorClient(MongoDB)
    MongoSyncs = MongoClient(MongoDB)
    MongoClients = MongoAsync[usernamee]
    DatabaseMongo = MongoSyncs[usernamee]

else:
    MongoAsync = AsyncIOMotorClient(vars.MongoDatabaseURI)
    MongoSyncs = MongoClient(vars.MongoDatabaseURI)
    MongoClients = MongoAsync.usernamee
    DatabaseMongo = MongoSyncs.usernamee
