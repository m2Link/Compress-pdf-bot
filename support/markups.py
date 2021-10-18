from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('💬 Update Channel', url='https://t.me/m2botz'),
            InlineKeyboardButton('🗣 Support Group', url='https://t.me/m2botzsupport')
        ]
        [
            InlineKeyboardButton('🧑‍💻Developer', url='t.me/ask_admin01'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Support', url='t.me/rmprojects'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
