# features/couple.py

import random
from datetime import datetime
from pyrogram import filters
from .. import app as bot
from ..database1 import get_couple, save_couple
from ..imgs_config import COUPLES_PIC

# Helper functions
def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list

def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a

tomorrow = str(dt_tom())
today = str(dt()[0])

C = """
✧ 𝖢𝖮𝖴𝖯𝖫𝖤𝖲 𝖮𝖥 𝖳𝖧𝖤 𝖣𝖠𝖸 ✧
─────────────────
{} + ( PGM🎀 (https://t.me/WhyyYouObsessesWithMe) + 花火 (https://t.me/Senpaiii10)) = 🤍
─────────────────
𝖭𝖤𝖶 𝖢𝖮𝖴𝖯𝖫𝖤 𝖮𝖥 𝖳𝖧𝖤 𝖣𝖠𝖸 𝖢𝖠𝖭 𝖡𝖤 𝖢𝖧𝖮𝖲𝖤𝖭 𝖠𝖳 12𝖠𝖬 {}
"""

CAP = """
✧ 𝖢𝖮𝖴𝖯𝖫𝖤𝖲 𝖮𝖥 𝖳𝖧𝖤 𝖣𝖠𝖸 ✧
─────────────────
{} + {} = 🤍
─────────────────
𝖭𝖤𝖶 𝖢𝖮𝖴𝖯𝖫𝖤 𝖮𝖥 𝖳𝖧𝖤 𝖣𝖠𝖸 𝖢𝖠𝖭 𝖡𝖤 𝖢𝖧𝖮𝖲𝖤𝖭 𝖠𝖳 12𝖠𝖬 {}
"""

CAP2 = """
✧ 𝖢𝖮𝖴𝖯𝖫𝖤𝖲 𝖮𝖥 𝖳𝖧𝖤 𝖣𝖠𝖸 ✧
─────────────────
{} (tg://openmessage?user_id={}) + {} (tg://openmessage?user_id={}) = 🤍\n
─────────────────
𝖭𝖤𝖶 𝖢𝖮𝖴𝖯𝖫𝖤 𝖮𝖥 𝖳𝖧𝖤 𝖣𝖠𝖸 𝖢𝖠𝖭 𝖡𝖤 𝖢𝖧𝖮𝖲𝖤𝖭 𝖠𝖳 12𝖠𝖬 {}
"""

@bot.on_message(filters.command(["couple", "couples", "shipping"]) & ~filters.private)
async def nibba_nibbi(client, message):
    if message.from_user.id == 123456789:
        my_ = await client.get_users("rfxtuv")
        me = await client.get_users(123789456)
        await message.reply_photo(
            photo=COUPLES_PIC, caption=C.format(me.mention, tomorrow)
        )
    else:
        try:
            chat_id = message.chat.id
            is_selected = await get_couple(chat_id, today)
            if not is_selected:
                list_of_users = []
                async for i in client.get_chat_members(message.chat.id, limit=50):
                    if not i.user.is_bot:
                        list_of_users.append(i.user.id)
                if len(list_of_users) < 2:
                    return await message.reply_text("𝑁𝑜𝑡 𝑒𝑛𝑜𝑢𝑔ℎ 𝑢𝑠𝑒𝑟𝑠 𝑖𝑛 𝑡ℎ𝑖𝑠 𝑔𝑟𝑜𝑢𝑝.")
                c1_id = random.choice(list_of_users)
                c2_id = random.choice(list_of_users)
                while c1_id == c2_id:
                    c1_id = random.choice(list_of_users)
                c1_mention = (await client.get_users(c1_id)).mention
                c2_mention = (await client.get_users(c2_id)).mention
                await client.send_photo(
                    message.chat.id,
                    photo=COUPLES_PIC,
                    caption=CAP.format(c1_mention, c2_mention, tomorrow),
                )

                couple = {"c1_id": c1_id, "c2_id": c2_id}
                await save_couple(chat_id, today, couple)

            else:
                c1_id = int(is_selected["c1_id"])
                c2_id = int(is_selected["c2_id"])

                c1_name = (await client.get_users(c1_id)).first_name
                c2_name = (await client.get_users(c2_id)).first_name
                couple_selection_message = f"""✧ 𝖢𝖮𝖴𝖯𝖫𝖤𝖲 𝖮𝖥 𝖳𝖧𝖤 𝖣𝖠𝖸 ✧
─────────────────
[{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = 🤍
─────────────────
𝖭𝖤𝖶 𝖢𝖮𝖴𝖯𝖫𝖤 𝖮𝖥 𝖳𝖧𝖤 𝖣𝖠𝖸 𝖢𝖠𝖭 𝖡𝖤 𝖢𝖧𝖮𝖲𝖤𝖭 𝖠𝖳 12𝖠𝖬 {tomorrow}"""

                await client.send_photo(
                    message.chat.id, photo=COUPLES_PIC, caption=couple_selection_message
                )
        except Exception as e:
            print(e)
            await message.reply_text(str(e))
