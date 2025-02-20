from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("⚡️𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦⚡️", data="help_back")
        ],
        [
        Button.url("⚡️𝗠𝗢𝗩𝗜𝗘𝗦⚡️", "https://t.me/MoviesWDs_bot"),
        Button.url("⚡️𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️", "https://t.me/Mrshubh_1227")
        ],
        [
        Button.url("⚡️𝗢𝗪𝗡𝗘𝗥⚡️", "https://t.me/Demonxcoder")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))

async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝗛𝗘𝗬 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝗜 𝗔𝗠  [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗗 𝗕𝗬 :~ [𝗦𝗛𝗨𝗕𝗛](https://t.me/Demonxcoder)**\n\n"
        TEXT += f"» **𝗦𝗛𝗨𝗕𝗛 𝗦𝗣𝗔𝗠 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 :** `3.2`\n"
        TEXT += f"» **𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 𝗩𝗘𝗥𝗦𝗜𝗢𝗡:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://graph.org/file/db0fbc02a08c2a28349f1-3671ff24b68aa73e82.jpg",
                caption=TEXT, 
                buttons=PythonButton)
