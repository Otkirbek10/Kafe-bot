from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

sh_set = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ORQAGA ↩️"),KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text="Shashlikli set (kichik)"),KeyboardButton(text="Shashlikli set (katta)")],
        [KeyboardButton(text="Bosh Sahifa 🏠")]

    ],
    resize_keyboard=True
)