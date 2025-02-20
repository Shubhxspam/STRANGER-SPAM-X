import os
import sys
import heroku3
from datetime import datetime
from config import MK1, MK2, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))

async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"»𝗦𝗛𝗨𝗕𝗛_𝗦𝗣𝗔𝗠_𝗕𝗢𝗧_ᴏᴘ_ʙᴏʟᴛᴀ", parse_mode=None, link_preview=None)
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"_⚡️𝗞𝗜𝗦𝗞𝗜 𝗚𝗔𝗔𝗡𝗗 𝗠𝗔𝗥𝗡𝗜 𝗕𝗢𝗦𝗦⚡️_\n» `{mp} ms`")


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))

async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"😖ʀᴇʙᴏᴏᴛ ᴋᴀʀᴋᴇ ᴛᴜɴᴇ ᴀᴘɴɪ ᴀᴜᴋᴀᴀᴛ ᴅɪᴋʜᴀ ᴅɪ...!😪😒")
        try:
            await MK1.disconnect()
        except Exception:
            pass
        try:
            await MK2.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
sudousers = os.environ.get("SUDO_USER", None)

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))

async def addsudo(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"» __ᴇᴋ ɴᴀʏᴀ🍃𝗦𝗛𝗨𝗕𝗛 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧🍃  ᴀᴅᴅ ʜᴏ ʀʜᴀ...__")
        mks = "SUDO_USER"
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except Exception:
            await ok.edit("» ᴀʙᴇ ɢᴀɴᴅᴜ....ᴜsᴇʀ ᴘᴇ ʀᴇᴘʟʏ ᴋᴀʀʀ !!")
        if len(sudousers) > 0:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"» **ɴᴇᴡ🍃𝗦𝗛𝗨𝗕𝗛 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧🍃**: `{target}`\n» `ʙᴏᴛ ғɪʀ sᴇ sᴜʀᴜ ʜᴏ ʀʜᴀ...`")
        heroku_var[mks] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(GetFullUserRequest(previous_message.forward.sender_id))
        else:
            replied_user = await event.client(GetFullUserRequest(previous_message.sender_id))
    return replied_user.user.id
