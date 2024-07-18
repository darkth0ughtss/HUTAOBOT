import requests
import asyncio
from pyrogram import Client, filters
from .. import app as bot

async def fetch_question(url, params):
    response = await asyncio.to_thread(requests.get, url, params=params)
    return response.json().get("question")

@bot.on_message(filters.command("truth"))
async def truth(client, message):
    params = {
        "rating": "pg13"  # Change this to "pg" or "r" if needed
    }
    truth = await fetch_question("https://api.truthordarebot.xyz/v1/truth", params)
    await message.reply_text(truth)

@bot.on_message(filters.command("dare"))
async def dare(client, message):
    params = {
        "rating": "pg13"  # Change this to "pg" or "r" if needed
    }
    dare = await fetch_question("https://api.truthordarebot.xyz/v1/dare", params)
    await message.reply_text(dare)

@bot.on_message(filters.command("wyr"))
async def wyr(client, message):
    params = {
        "rating": "pg13"  # Change this to "pg" or "r" if needed
    }
    wyr = await fetch_question("https://api.truthordarebot.xyz/v1/wyr", params)
    await message.reply_text(wyr)

@bot.on_message(filters.command("nhie"))
async def nhie(client, message):
    params = {
        "rating": "pg13"  # Change this to "pg" or "r" if needed
    }
    nhie = await fetch_question("https://api.truthordarebot.xyz/v1/nhie", params)
    await message.reply_text(nhie)

@bot.on_message(filters.command("paranoia"))
async def paranoia(client, message):
    params = {
        "rating": "pg13"  # Change this to "pg" or "r" if needed
    }
    paranoia = await fetch_question("https://api.truthordarebot.xyz/v1/paranoia", params)
    await message.reply_text(paranoia)
