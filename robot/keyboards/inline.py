from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

langs_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="uz"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru"),
            InlineKeyboardButton(text="🇺🇸 English", callback_data="en"),
        ]
    ]
)


ssilki_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram", url="https://t.me/Mamatmusayev_uz"),
            InlineKeyboardButton(text="Youtube", url="https://youtube.com/mamatmusayev.uz/")
        ],

    ]
)
