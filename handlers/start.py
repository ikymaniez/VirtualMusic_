# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Haii 🖐️ {message.from_user.first_name} My Name is 𝗩𝗜𝗥𝗧𝗨𝗔𝗟 𝗠𝗨𝗦𝗜𝗖\n
Aku Adalah Bot Music Telegram Yang Akan Menemani mu Di Voice Call Group.
Jika Ingin Menggunakan Invite Aku Dan Asisstantnya Ke Dalam Group Lalu Angkat Bot Menjadi Admin. Jika Ada Kendala Bisa Chat Pemilik Nya.
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Lagu.
┣• Mencari Lagu Yang ingin di Putar atau di Download.
┗━━━━━━━━━━━━━━
🤵𝓒𝓻𝓮𝓪𝓽𝓮𝓭 𝓫𝔂 : [IKYY](https://t.me/boyfriendnice)
☘️𝓣𝓱𝓪𝓷𝓴𝓼 𝓯𝓸𝓻 : [Grup Support](https://t.me/remaja_virtual62)
━━━━━━━━━━━━━━
𝐁𝐎𝐓 𝐌𝐔𝐒𝐈𝐊 : @Virtualsong_bot - 𝐀𝐒𝐈𝐒𝐒𝐓𝐀𝐍𝐓 𝐌𝐔𝐒𝐈𝐊 : @AsisstantMusicVirtual
 
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🤵Owner Music", url="https://t.me/boyfriendnice")
                  ],[
                    InlineKeyboardButton(
                        "👥Official Group", url="https://t.me/Familythunder"
                    ),
                    InlineKeyboardButton(
                        "📢Official Channel", url="https://t.me/MusikManagement") 
                  ],[
                    InlineKeyboardButton(
                        "🍀Instagram", url="https://www.instagram.com/ikyyy_35"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.edited)
async def gstart(_, message: Message):
      await message.reply_text("""**Aku sudah online, ayo kita joget ceria! 🎶**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤵Owner Music", url="https://t.me/boyfriendnice"
                    )
                ],[
                    InlineKeyboardButton(
                        "✅ Yes!", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ No!", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.edited)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik tombol dibawah untuk melihat panduan menggunakan bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦇 Cara Memakai Bot Music!", url="https://t.me/humangabutguys/91577"
                    )
                ]
            ]
        ),
    )
