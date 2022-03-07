from aiogram.types import ReplyKeyboardRemove
from loader import dp, db
from keyboards.default.asosiy import menu
from keyboards.default.categoriya import cats
from aiogram import types
from states.state import Kafe
@dp.message_handler(text_contains="❌")
async def delete_product(message: types.Message):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Product=product.strip())
    await message.answer(f"{product.strip()} savatingiz o'chirildi!", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Bo'shatish 🗑")
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Savatchangiz tozalandi!", reply_markup=menu)

@dp.message_handler(text="Bo'shatish 🗑",state=Kafe.product)
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Savatchangiz tozalandi!", reply_markup=cats)

@dp.message_handler(text="Bo'shatish 🗑",state=Kafe.categor)
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Savatchangiz tozalandi!", reply_markup=cats)

