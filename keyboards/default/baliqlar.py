from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

fishs = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ORQAGA ↩️"),KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text = 'Sazan (300g)'),KeyboardButton(text='Sudak (300g)')],
        [KeyboardButton(text='Sous 300ml'),KeyboardButton(text = "Sous 500ml")],
        [KeyboardButton(text='Bosh Sahifa 🏠')]
    ],
    resize_keyboard=True
)