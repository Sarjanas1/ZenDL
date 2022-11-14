# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by Shin-Yue, < https://github.com/Shin-yue >.
# and is released under the "GNU v3.0 License Agreement
#
# All rights reserved.
# Vars of the bot

import os


class RoftConfiguration:

    __roft_version__ = '1.5.8'

    ApiID = os.environ.get('API_ID', None)
    ApiHASH = os.environ.get('API_HASH', None) 

    TelegramBot = os.environ.get('TELEGRAM', None)
    SpecialUsers = int(os.environ.get('CREATOR_ID', None))

    MongoDatabaseURI = os.environ.get('DATABASE_URI', None)
    LogGroupChatID = int(os.environ.get('LOG_CHAT_ID', None)) 

    MusicDurationLimit = int(os.getenv("MusicDurationLimit", "3600"))
    CommandPrefixesBOT = list(os.getenv("CommandPrefixesBOT", '. / !').split())

    GeniusLyricsAPI = os.getenv('GeniusLyricsAPI', '1QNnajK5oSh2Ut_bJVXbKzwFV_BqyZxUssSpWdcjpVHr5qRcql0BMx3pMSVWSFoj')
    UserMustJoinChannel = os.getenv('UserMustJoinChannel', 'yueblog')


vars = RoftConfiguration() 
