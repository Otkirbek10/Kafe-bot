from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
suvlar = ReplyKeyboardMarkup(
    keyboard=[
         [KeyboardButton(text="ORQAGA ↩️"),KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text = 'Coca-Cola (0,5 L)'),KeyboardButton(text='Coca-Cola (1,0 L)')],
        [KeyboardButton(text = 'Coca-Cola (1,5 L)'),KeyboardButton(text='Fanta (0,5 L)')],
        [KeyboardButton(text = 'Fanta (1,0 L)'),KeyboardButton(text='Fanta (1,5 L)')],
        [KeyboardButton(text='Bosh Sahifa 🏠')],
    ],
    resize_keyboard=True
)

