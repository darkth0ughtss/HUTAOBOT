

# <============================================== IMPORTS =========================================================>
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .. import app as bot
from ..state import state

# <=======================================================================================================>

# <================================================ FUNCTIONS =====================================================>
async def get_pokemon_info(name_or_id):
    try:
        response = await state.get(
            f"https://sugoi-api.vercel.app/pokemon?name={name_or_id}"
        )
        if response.status_code == 200:
            return response.json()

        response = await state.get(
            f"https://sugoi-api.vercel.app/pokemon?id={name_or_id}"
        )
        if response.status_code == 200:
            return response.json()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return None


@bot.on_message(filters.command("pokedex"))
async def pokedex(client, message):
    try:
        if len(message.command) > 1:
            name_or_id = message.command[1]
            pokemon_info = await get_pokemon_info(name_or_id)

            if pokemon_info:
                reply_message = (
                    f"🐾 𝗡𝗔𝗠𝗘: {pokemon_info['name']}\n"
                    f"•➥ 𝗜𝗗: {pokemon_info['id']}\n"
                    f"•➥ 𝗛𝗘𝗜𝗚𝗛𝗧: {pokemon_info['height']}\n"
                    f"•➥ 𝗪𝗘𝗜𝗚𝗛𝗧: {pokemon_info['weight']}\n"
                )

                abilities = ", ".join(
                    ability["ability"]["name"] for ability in pokemon_info["abilities"]
                )
                reply_message += f"•➥ 𝗔𝗕𝗜𝗟𝗜𝗧𝗜𝗘𝗦: {abilities}\n"

                types = ", ".join(
                    type_info["type"]["name"] for type_info in pokemon_info["types"]
                )
                reply_message += f"•➥ 𝗧𝗬𝗣𝗘𝗦: {types}\n"

                image_url = f"https://img.pokemondb.net/artwork/large/{pokemon_info['name']}.jpg"

                # Create inline buttons
                keyboard = [
                    [
                        InlineKeyboardButton(text="🔖 STATS", callback_data="stats"),
                        InlineKeyboardButton(text="⚜️ MOVES", callback_data="moves"),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)

                await message.reply_photo(
                    photo=image_url,
                    caption=reply_message,
                    reply_markup=reply_markup,
                )
            else:
                await message.reply_text("𝑃𝑜𝑘𝑒𝑚𝑜𝑛 𝑛𝑜𝑡 𝑓𝑜𝑢𝑛𝑑.")
        else:
            await message.reply_text("𝑃𝑙𝑒𝑎𝑠𝑒 𝑝𝑟𝑜𝑣𝑖𝑑𝑒 𝑎 𝑃𝑜𝑘𝑒𝑚𝑜𝑛 𝑛𝑎𝑚𝑒 𝑜𝑟 𝐼𝐷.")
    except Exception as e:
        await message.reply_text(f"𝗔𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱")


@bot.on_callback_query(filters.regex("^(stats|moves)$"))
async def callback_query_handler(client, query):
    await query.answer()

    try:
        name = query.message.caption.split("\n")[0].split(": ")[1]
        pokemon_info = await get_pokemon_info(name)

        if pokemon_info:
            stats = "\n".join(
                f"{stat['stat']['name'].upper()}: {stat['base_stat']}"
                for stat in pokemon_info["stats"]
            )
            stats_message = f"•➥ STATS:\n{stats}\n"

            moves = ", ".join(
                move_info["move"]["name"] for move_info in pokemon_info["moves"]
            )
            moves_message = f"•➥ MOVES: {moves}"

            if query.data == "stats":
                await query.message.reply_text(stats_message)
            elif query.data == "moves":
                if len(moves_message) > 1000:
                    with open("moves.txt", "w") as file:
                        file.write(moves_message)
                    await query.message.reply_text(
                        "𝑇ℎ𝑒 𝑚𝑜𝑣𝑒𝑠 𝑒𝑥𝑐𝑒𝑒𝑑 1000 𝑐ℎ𝑎𝑟𝑎𝑐𝑡𝑒𝑟𝑠. 𝑆𝑒𝑛𝑑𝑖𝑛𝑔 𝑎𝑠 𝑎 𝑓𝑖𝑙𝑒.",
                        disable_web_page_preview=True,
                    )
                    await query.message.reply_document(document="moves.txt")
                else:
                    await query.message.reply_text(moves_message)
        else:
            await query.message.reply_text("𝗣𝗼𝗸𝗲𝗺𝗼𝗻 𝗻𝗼𝘁 𝗳𝗼𝘂𝗻𝗱.")
    except Exception as e:
        await query.message.reply_text(f"𝗔𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱")

