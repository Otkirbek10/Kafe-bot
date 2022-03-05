from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

cats = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "ORQAGA ↩️"),KeyboardButton(text='Savatcha 🛒')],
        [KeyboardButton(text="Shashlik"),KeyboardButton(text="Baliq 🐠")],
        [KeyboardButton(text="Холодные закуски"),KeyboardButton(text="Salatlar")],
        [KeyboardButton(text="Ichimliklar 🥤"),KeyboardButton(text="Sho'rva")],
        [KeyboardButton(text='Ikkinchi ovqatlar 🍛'),KeyboardButton(text = 'Non 🥯')],
        [KeyboardButton(text="Kombo 🍛🥤"),KeyboardButton(text="Shashlikli setlar 🥩")],
        [KeyboardButton(text="Bosh Sahifa 🏠")]

    ],
    resize_keyboard=True
)