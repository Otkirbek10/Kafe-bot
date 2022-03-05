from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

shashliklar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ORQAGA ↩️"),KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text="Kuskavoy (mol go'shti)"),KeyboardButton(text="Kuskavoy (qo'y go'shti)")],
        [KeyboardButton(text="Rulet"),KeyboardButton(text="2 ichida 1")],
        [KeyboardButton(text="Napoleon"),KeyboardButton(text="Qiymali kabob")],
        [KeyboardButton(text="Jigar kabob"),KeyboardButton(text="Tovuq filesi")],
        [KeyboardButton(text="Bosh Sahifa 🏠")]
    ],
    resize_keyboard= True
)