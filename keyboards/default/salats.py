from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

salatlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ORQAGA ↩️"),KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text="Olivye"),KeyboardButton(text="Smak")],
        [KeyboardButton(text="Cesar"),KeyboardButton(text="Fransuzcha")],
        [KeyboardButton(text="Mimoza"),KeyboardButton(text="Селёдка под шубой")],
        [KeyboardButton(text="Vinigret"),KeyboardButton(text="Grecheskiy")],
        [KeyboardButton(text="Bosh Sahifa 🏠")]
        ],
    resize_keyboard= True
)