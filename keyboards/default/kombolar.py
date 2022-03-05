from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kombos = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ORQAGA ↩️"),KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text="Сет Мясо по-китайски"),KeyboardButton(text="Сет Курица с овощами")],
        [KeyboardButton(text="Сет Бифштекс"),KeyboardButton(text="Сет Телятина с грибами")],
        [KeyboardButton(text="Сет Бефстроганов"),KeyboardButton(text="Сет Курица с грибами")],
        [KeyboardButton(text="Bosh Sahifa 🏠")],
    ],
    resize_keyboard=True
)