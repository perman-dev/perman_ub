#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from virtualuserbot import ALIVE_NAME
from virtualuserbot.modules import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/07f2d9a43562b26f1ba76.png"
pm_caption = " **¦✵ Assɪsᴛᴀɴᴛ Is Oɴʟɪɴᴇ ✵¦** \n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ¦** `1.15.0` \n"
pm_caption += "➥ **Pʏᴛʜᴏɴ:** `3.7.4` \n"
pm_caption += "➥ **Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs:**  `Functionaing`\n"
pm_caption += "➥ **Cᴜʀʀᴇɴᴛ Bʀᴀɴᴄʜ** ¦ `Master`\n"
pm_caption += f"➥ **Vᴇʀsɪᴏɴ** ¦ `{currentversion}`\n"
pm_caption += f"➥ **Mʏ Bᴏss** ¦ {DEFAULTUSER} \n"
pm_caption += "➥ **Hᴇʀᴏᴋᴜ Dᴀᴛᴀʙᴀsᴇ** ¦ `AWS - Working Properly`\n\n"
pm_caption += "➥ **Cᴏᴘʏʀɪɢʜᴛ** ¦ By [Perman](GitHub.com/Perman-dev)\n"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def friday(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
