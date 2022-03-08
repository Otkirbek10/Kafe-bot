from aiogram.types import ReplyKeyboardRemove
from loader import dp, db
from keyboards.default.asosiy import menu
from keyboards.default.categoriya import cats
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.state import Kafe
@dp.message_handler(text_contains="❌")
async def delete_product(message: types.Message):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Product=product.strip())
    await message.answer(f"{product.strip()} savatingiz o'chirildi!", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text_contains="❌",state=Kafe.categor)
async def delete_product(message: types.Message,state:FSMContext):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Product=product.strip())
    await message.answer(f"{product.strip()} savatingiz o'chirildi!", reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text_contains="❌",state=Kafe.product)
async def delete_product(message: types.Message,state:FSMContext):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Product=product.strip())
    await message.answer(f"{product.strip()} savatingiz o'chirildi!", reply_markup=ReplyKeyboardRemove())
    await state.finish()
    

@dp.message_handler(text="Bo'shatish 🗑")
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Savatchangiz tozalandi!", reply_markup=menu)

@dp.message_handler(text="Bo'shatish 🗑",state=Kafe.product)
async def clearcart(message: types.Message,state:FSMContext):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Savatchangiz tozalandi!", reply_markup=cats)
    await Kafe.categor.set()

@dp.message_handler(text="Bo'shatish 🗑",state=Kafe.categor)
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Savatchangiz tozalandi!", reply_markup=cats)

