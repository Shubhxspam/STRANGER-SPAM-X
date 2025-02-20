import glob
from pathlib import Path
from utils import load_plugins
import logging
import asyncio
from config import MK1, MK2 

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "AltronX/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\⚡️𝐒𝗛𝗨𝗕𝗛⚡️𝐒𝐏𝐀𝐌 𝐁𝐎𝐓𝐒 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😎🤘🏻\nᴍʏ ᴍᴀsᴛᴇʀ ---> @Demonxcoder")


async def main():
    await MK1.run_until_disconnected()
    await MK2.run_until_disconnected()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
