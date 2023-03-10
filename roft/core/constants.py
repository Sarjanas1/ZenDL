message_1 = (
    "👋🏻 Hai, {m} dan <b>Selamat datang.</b>\n\n"
     "💭 @{bn} memungkinkan Anda mengunduh"
     " media dari TikTok, YouTube, Pinterest, Spotify, dan Instagram. "
     "Untuk mengetahui lebih lanjut tentang cara menggunakan saya, tekan tombol '📮 <b>Bantuan</b>'."
)
message_2 = "💭 Halo {}!"
pesan_3 = (
     "📮 <b>Bantuan</b>\n\n"
     "<b>Perintah YouTube:</b>\n"
     "Cukup ketik /lagu [judul lagu]"
     " Anda bisa mendapatkan audio atau video dari YouTube.\n"
     "Anda juga bisa mendapatkan lirik dari genius.com melalui saya, gunakan perintah / lirik [judul]\n\n"
     "<b>Perintah TikTok:</b>\n"
     "Bagaimana cara mengunduh video dari TikTok?\n"
     " <b>1.</b> Buka aplikasi TikTok\n"
     " <b>2.</b> Pilih video yang menarik bagi Anda\n"
     " <b>3.</b> Klik tombol ↪️ atau tiga titik di pojok kanan atas\n"
     " <b>4.</b> Klik tombol 'Salin'\n"
     " <b>5.</b> Kirim tautan ke bot setelah menggunakan perintah /tiktok, dan dalam beberapa detik Anda akan menerima video tanpa tanda air.\n\n"
     "<b>Perintah Pinterest:</b>\n"
     "Pinterest memiliki 3 jenis media seperti: Gambar, GIF, video.\n"
     "Anda cukup menyalin tautan dari pinterest ke saya dengan menggunakan perintah /pints [pint link].\n\n"
     "<b>Perintah Wikipedia:</b>\n"
     "Cukup ketik /wiki [kata] dan saya akan mencarinya di Wikipedia.\n\n"
     "Anda dapat menemukan kode sumber bot ini di github dengan type/source"
)
message_4 = (
    "ℹ️ <b>Info</b>\n\n"
     "Zen adalah bot yang dikembangkan di <b>Python3</b>"
     " dan menggunakan <a href='https://github.com/pyrogram/pyrogram'>Pyrogram</a> sebagai framework dengan MongoDB sebagai database.\n\n"
     "🆚 Versi<b>:</b> {} | 📣 Saluran<b>:</b> @ZennXSupport"
)
# download module 
message_5 = "🔍 <b>Sabar...</b>"
message_6 = "Untuk mendownload lagu, lakukan /song [Song name]"
message_7 = (
    "{}\n\n"
    "<b>1.</b> <i>{}</i>\n<b>2.</b> <i>{}</i>\n<b>3.</b> <i>{}</i>\n<b>4.</b> <i>{}</i>\n<b>5.</b> <i>{}</i>\n"
    "<b>6.</b> <i>{}</i>\n<b>7.</b> <i>{}</i>\n<b>8.</b> <i>{}</i>\n<b>9.</b> <i>{}</i>\n<b>10.</b> <i>{}</i>"
)
message_9 = "😕 Maaf, video langsung tidak didukung."
message_10 = "😕 Maaf opsi ini bukan untuk Anda, silakan cari sendiri."
message_11 = "❌ Durasi error, durasi hanya diperbolehkan 1000 detik"
# bans module
message_12 = "🚷 Anda telah <b>banned</b>"
message_13 = "🔓 Anda telah <b>unbanned</b>"
message_14 = "🚷 {} [<code>{}</code>] telah <b>banned</b>"
message_15 = "🔓 {} [<code>{}</code>] telah <b>unbanned</b>"
message_16 = "🚷 <b>Pengguna sudah diban</b>"
message_17 = "🔓 <b>User tidak ban</b>"
message_18 = "⚠️ <b>perintah tidak valid</b>\n💭 Gunakan <b>perintah yang menentukan ID</b> atau membalas <b>pesan pengguna</b>"
message_19 = "\n• <b>Karena:</b> {}"
# bot broadcast 
message_20 = "<b>Penggunaan:</b> <code>/broadcast [pesan Anda]</code> atau Anda dapat membalas pesan."
message_21 = "⌛<b>Sabar pesan siaran...</b> Akan memakan waktu <code>{}</code> detik."
message_22 = "✅ Berhasil menyiarkan pesan di {} obrolan"
# pinterest text
message_23 = "Untuk mendapatkan media pinterest, lakukan /pints [Pinterest URL]"
message_24 = "⌛ <b>Tunggu...</b>"
message_25 = (
   "<b>Mengunduh Pinterest</b>\n"
   "<a href='https://t.me/ZennXSupport'>Channel</a> | <a href='https://t.me/onlybionn'>Developer</a>"
)
message_26 = "🔍 <b>No results found, please try again.</b>"
# TikTok Module
message_27 = "Untuk mengunduh video tiktok, lakukan /tiktok [TikTok URL]"
message_28 = "• Donwload Via [zenDL](https://t.me//zencovert_bot)"
message_29 = "🔍 <b>Tidak ada hasil yang ditemukan, silakan coba lagi.</b>"
message_30 = "Maaf, saya tidak dapat memperoleh informasi tentang file ini.\Coba lagi nanti atau kirim tautan lain."

# button
from pyrogram import types

def keyboard_song(
    id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10, 
    duration_1, duration_2, duration_3, duration_4, duration_5, 
    duration_6, duration_7, duration_8, duration_9, duration_10, 
    user_id, value
):
    buttons = (
        types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(text='1', callback_data=f'download {id_1}|{duration_1}|{user_id}'),
                    types.InlineKeyboardButton(text='2', callback_data=f'download {id_2}|{duration_2}|{user_id}'),
                    types.InlineKeyboardButton(text='3', callback_data=f'download {id_3}|{duration_3}|{user_id}'),
                    types.InlineKeyboardButton(text='4', callback_data=f'download {id_4}|{duration_4}|{user_id}'),
                    types.InlineKeyboardButton(text='5', callback_data=f'download {id_5}|{duration_5}|{user_id}'),
                ],
                [
                    types.InlineKeyboardButton(text='6', callback_data=f'download {id_6}|{duration_6}|{user_id}'),
                    types.InlineKeyboardButton(text='7', callback_data=f'download {id_7}|{duration_7}|{user_id}'),
                    types.InlineKeyboardButton(text='8', callback_data=f'download {id_8}|{duration_8}|{user_id}'),
                    types.InlineKeyboardButton(text='9', callback_data=f'download {id_9}|{duration_9}|{user_id}'),
                    types.InlineKeyboardButton(text='10', callback_data=f'download {id_10}|{duration_10}|{user_id}')
                ],
                [
                    types.InlineKeyboardButton(text='x', callback_data=f'close |{user_id}'),
                    types.InlineKeyboardButton(text='»', callback_data=f'change 1|{value}|{user_id}')
                ]
            ]
        )
    )
    return buttons

def keyboard_song2(
    id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10, 
    duration_1, duration_2, duration_3, duration_4, duration_5, 
    duration_6, duration_7, duration_8, duration_9, duration_10, 
    user_id, value
):
    buttons = (
        types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(text='1', callback_data=f'download {id_1}|{duration_1}|{user_id}'),
                    types.InlineKeyboardButton(text='2', callback_data=f'download {id_2}|{duration_2}|{user_id}'),
                    types.InlineKeyboardButton(text='3', callback_data=f'download {id_3}|{duration_3}|{user_id}'),
                    types.InlineKeyboardButton(text='4', callback_data=f'download {id_4}|{duration_4}|{user_id}'),
                    types.InlineKeyboardButton(text='5', callback_data=f'download {id_5}|{duration_5}|{user_id}'),
                ],
                [
                    types.InlineKeyboardButton(text='6', callback_data=f'download {id_6}|{duration_6}|{user_id}'),
                    types.InlineKeyboardButton(text='7', callback_data=f'download {id_7}|{duration_7}|{user_id}'),
                    types.InlineKeyboardButton(text='8', callback_data=f'download {id_8}|{duration_8}|{user_id}'),
                    types.InlineKeyboardButton(text='9', callback_data=f'download {id_9}|{duration_9}|{user_id}'),
                    types.InlineKeyboardButton(text='10', callback_data=f'download {id_10}|{duration_10}|{user_id}')
                ],
                [
                    types.InlineKeyboardButton(text='«', callback_data=f'change 2|{value}|{user_id}')
                ]
            ]
        )
    )
    return buttons

def keyboard_down(id, duration, user_id):
    buttons = (
        types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(text="📽️ Download Video", callback_data=f'video_ {id}|{duration}|{user_id}')
                ]
            ]
        )
    )
    return buttons


keyboard = (
    types.InlineKeyboardMarkup(
        [
            [
                types.InlineKeyboardButton(text='📮 Help', callback_data='self_help'),
                types.InlineKeyboardButton(text='📣 Channel', url='https://t.me/ZennXSupport')
            ]
        ]
    )
)

back_kb = (types.InlineKeyboardMarkup([
     [types.InlineKeyboardButton(text='🔙', callback_data='self_backhome')]])
)
