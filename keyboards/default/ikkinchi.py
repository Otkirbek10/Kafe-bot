from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

second = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='ORQAGA ↩️'),KeyboardButton(text='Savatcha 🛒')],
        [KeyboardButton(text="Мясо по-гречески"),KeyboardButton(text="Мясо по-французски")],
        [KeyboardButton(text='Мясо по-царски'),KeyboardButton(text='Мясо по-армянски')],
        [KeyboardButton(text='Мишель'),KeyboardButton(text='Bifshteks')],
        [KeyboardButton(text='Bosh Sаhifa 🏠')]
    ],
    resize_keyboard=True
)