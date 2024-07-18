#MIT License
#Copyright (c) 2023, ©NovaNetworks

import time
from pyrogram import filters

from HuTao import app, start, Hutao_Ver
from HuTao.helpers.readable_time import get_readable_time
from HuTao.Config import COMMAND_HANDLER
from HuTao.modules.start import VERSION


@app.on_message(filters.command(["ping"], COMMAND_HANDLER))
async def ping(_, message):
    currentTime = get_readable_time(time.time() - start)
    start_t = time.time()
    rm = await message.reply_photo("https://telegra.ph/file/88e49e34c67873e694139.jpg", caption="Pong..")
    end_t = time.time()
    time_taken_s = round(end_t - start_t, 3)
    await rm.edit_caption(
        f"""
**BOT VERSION:** {VERSION}

**PING:** {time_taken_s} seconds
**UPTIME:** {currentTime}"""
    )

__mod__ = "MISC"
__help__ = """
**» /ping** - Check If The Bot Is Alive
**» /joinreq** - To Turn On Approve And Decline Buttons In The Chat
**» /tgm** - Upload Photo (Under 5mb) To Cloud And Give Link 
**» /upscale** - Reply To A Image To Upscale It (Improve Its Quality)
**» /id** - Get The Id of a User
**» /gstatus** - Get The Group Stats (TRY IT)

**[NOTE: JOIN REQUESTS ONLY WORKS IF APPROVE SETTINGS ARE ENABLED]**
"""