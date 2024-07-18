import requests
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from .. import app as bot
import logging

logger = logging.getLogger(__name__)

@bot.on_message(
    filters.command(["github", "git"]) & (filters.group | filters.private),
)
async def github(_, m: Message):
    if len(m.text.split()) == 2:
        username = m.text.split(maxsplit=1)[1]
        logger.info(f"{m.from_user.id} used github cmd in {m.chat.id}")
    else:
        await m.reply_text(
            f"Usage: <code>/github username</code>",
        )
        return
    username = username.split("/")[-1].strip("@")
    URL = f"https://api.github.com/users/{username}"
    try:
        r = requests.get(URL, timeout=5)
    except requests.exceptions.ConnectTimeout:
        return await m.reply_text("Request timeout")
    except Exception as e:
        return await m.reply_text(f"ERROR:\n`{e}`")
    if r.status_code != 200:
        await m.reply_text(f"{username} this user is not available on GitHub\nMake sure you have given the correct username")
        return
    r = r.json()
    avatar = r.get("avatar_url", None)
    if avatar:
        avatar = avatar.rsplit("=", 1)
        avatar.pop(-1)
        avatar.append("5")
        avatar = "=".join(avatar)
    url = r.get("html_url", None)
    name = r.get("name", None)
    company = r.get("company", None)
    followers = r.get("followers", 0)
    following = r.get("following", 0)
    public_repos = r.get("public_repos", 0)
    bio = r.get("bio", None)
    created_at = r.get("created_at", "NA").replace("T", " ").replace("Z", "")
    location = r.get("location", None)
    email = r.get("email", None)
    updated_at = r.get("updated_at", "NA").replace("T", " ").replace("Z", "")
    blog = r.get("blog", None)
    twitter = r.get("twitter_username", None)

    REPLY = ""
    if name:
        REPLY += f"<b>🧑‍💻 GitHub Info of {name}:</b>"
    if url:
        REPLY += f"\n<b>📎 URL:</b> <a href='{url}'>{username}</a>"
    REPLY += f"\n<b>🔑 Public Repos:</b> {public_repos}"
    REPLY += f"\n<b>🧲 Followers:</b> {followers}"
    REPLY += f"\n<b>✨ Following:</b> {following}"
    if email:
        REPLY += f"\n<b>✉️ Email:</b> <code>{email}</code>"
    if company:
        org_url = company.strip("@")
        REPLY += f"\n<b>™️ Organization:</b> <a href='https://github.com/{org_url}'>{company}</a>"
    if blog:
        bname = blog.split(".")[-2]
        bname = bname.split("/")[-1]
        REPLY += f"\n<b>📝 Blog:</b> <a href={blog}>{bname}</a>"
    if twitter:
        REPLY += f"\n<b>⚜️ Twitter:</b> <a href='https://twitter.com/{twitter}'>{twitter}</a>"
    if location:
        REPLY += f"\n<b>🚀 Location:</b> <code>{location}</code>"
    if created_at != "NA":
        REPLY += f"\n<b>💫 Created at:</b> <code>{created_at}</code>"
    if updated_at != "NA":
        REPLY += f"\n<b>⌚️ Updated at:</b> <code>{updated_at}</code>"
    if bio:
        REPLY += f"\n\n<b>🎯 Bio:</b> {bio}"

    if avatar:
        return await m.reply_photo(photo=f"{avatar}", caption=REPLY)
    await m.reply_text(REPLY)
    return
