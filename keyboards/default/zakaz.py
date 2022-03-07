from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

zak = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Yetkazib berish 🚕")],
        [KeyboardButton(text="O’zim olib ketaman 🚶🏻")],
        [KeyboardButton(text="Bekor qilish♨️")],
    ],
    resize_keyboard=True
)
loc = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Manzilni jo'natish",request_location=True)],
        [KeyboardButton(text="ORQAGA🔙")]
    ],
    resize_keyboard=True
)