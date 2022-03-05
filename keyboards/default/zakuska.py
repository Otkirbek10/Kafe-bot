from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

zakuskalar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ORQAGA ↩️"),KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text="Suzma"),KeyboardButton(text="Ruscha Seld balig'i")],
        [KeyboardButton(text="Assorti"),KeyboardButton(text="Xolodes")],
        [KeyboardButton(text="Assorti (tuzli)"),KeyboardButton(text="Свежие нарезки")],
        [KeyboardButton(text="Bosh Sahifa 🏠")]
        ],
    resize_keyboard= True
)