# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by Shin-Yue, < https://github.com/Shin-yue >.
# and is released under the "GNU v3.0 License Agreement
#
# All rights reserved.
# Vars of the bot

import os
import dotenv


class RoftConfiguration:

    dotenv.load_dotenv()

    __roft_version__ = '1.5.8'

    ApiID = int(os.getenv('API_ID', None))
    ApiHASH = os.getenv('API_HASH', None) 

    TelegramBot = os.getenv('TELEGRAM', None)
    SpecialUsers = int(os.getenv('CREATOR_ID', None))

    MongoDatabaseURI = os.getenv('DATABASE_URI', None)
    LogGroupChatID = int(os.getenv('LOG_CHAT_ID', None)) 

    MusicDurationLimit = int(os.getenv("MusicDurationLimit", "3600"))
    CommandPrefixesBOT = list(os.getenv("CommandPrefixesBOT", '. / !').split())

    GeniusLyricsAPI = os.getenv('GeniusLyricsAPI', '1QNnajK5oSh2Ut_bJVXbKzwFV_BqyZxUssSpWdcjpVHr5qRcql0BMx3pMSVWSFoj')
    UserMustJoinChannel = os.getenv('UserMustJoinChannel', 'yueblog')


vars = RoftConfiguration() 
