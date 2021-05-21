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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>🖐️ Haii.. {message.from_user.first_name} Welcome To 𝗩𝗜𝗥𝗧𝗨𝗔𝗟 𝗠𝗨𝗦𝗜𝗖\n
Aku Adalah Bot Music Telegram Yang Akan Menemani mu Di Voice Call Group.
Jika Ingin Menggunakan Invite Aku Dan Asisstantnya Ke Dalam Group Lalu Angkat Bot Menjadi Admin. Jika Ada Kendala Bisa Chat Pemilik Nya.
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Lagu.
┣• Mencari Lagu Yang ingin di Putar atau di Download.
┗━━━━━━━━━━━━━━
🦇 Managed With By : [IKYY](https://t.me/boyfriednnice)
☘️𝓣𝓱𝓪𝓷𝓴𝓼 𝓯𝓸𝓻 : [Grup Support](https://t.me/Familythunder)
━━━━━━━━━━━━━━━
𝐁𝐎𝐓 𝐌𝐔𝐒𝐈𝐊 : @Virtualsong_bot - 𝐀𝐒𝐈𝐒𝐒𝐓𝐀𝐍𝐓 𝐌𝐔𝐒𝐈𝐊 : @AsisstantMusicVirtual
 </b>""",

# Edit Yang Perlu Lu ganti 
# Tapi Jangan di Hapus Thanks To nya Yaaa :D

        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🦇 Owner Music", url="https://t.me/boyfriendnice")
                  ],[
                    InlineKeyboardButton(
                        "👥 Support Group", url="https://t.me/Familythunder"
                    ),
                    InlineKeyboardButton(
                        "📢 Support Channel", url="https://t.me/MusikManagement"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Cara Menggunakan BOT 📜", url="https://t.me/Lunatic0de/20"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil dimulai ulang!**\n\n• **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👥 Support Group", url="https://t.me/Familythunder"
                    ),
                    InlineKeyboardButton(
                        "🦇 Owner Music", url="https://t.me/boyfriendnice"
                    )
                ]
            ]
        )
   )
