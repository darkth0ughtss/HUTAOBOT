#MIT License
#Copyright (c) 2023, ©NovaNetworks

import sys
from logging import getLogger

LOGGER = getLogger(__name__)

# Required ENV
try:
    BOT_TOKEN = "6617412135:AAFc7F-H7xoNbDMHTO8y-MrKWiurymgGwT8" # BOT TOKEN
    API_ID =  20028561 # API ID
    API_HASH = "0f3793daaf4d3905e55b0e44d8719cad" # API HASH
except Exception as e:
    LOGGER.error(f"Looks Like Something Is Missing!! Please Check Variables\n{e}")
    sys.exit(1)


TIMEZONE = "Asia/Kolkata" # YOUR TIME ZONE

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

SUDO = list({int(x)for x in ("").split()})

SUPPORT_CHAT = "DominosXD" # SUPPORT GROUP (ID OR USERNAME)

LOG_CHANNEL_ID = -1002102898878 #LOG GROUP ID FOR YOUR BOT

OWNER = list({int(x)for x in ("5630057244").split()}) #OWNER ID

DB_URL = "mongodb+srv://centerphoenix093:loniko0908@cluster0.yzoijiq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" # MONGO DB URL

SQL_URL = "" # ELEPHANT SQL URL
