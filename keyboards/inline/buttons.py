from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔒️ Shifrlash', callback_data='nom_shif'),
            InlineKeyboardButton(text='🔐 Deshifrlash', callback_data='nom_desh')
        ]
    ]
)
button1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='📝 Vernam Vijinir', callback_data='👍ver'),
            InlineKeyboardButton(text='✏️ Gammalash', callback_data='👍gam')
        ],
        [
            InlineKeyboardButton(text='🧮 Gamilton', callback_data='👍mash'),
            InlineKeyboardButton(text='🎲 Sezar', callback_data='👍sez')
        ]
    ]
)
reply_markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
reply_markup.add(
    KeyboardButton(text='🔙 Orqaga')
)
