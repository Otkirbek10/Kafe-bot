from loader import dp,db
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.state import Kafe
from handlers.users.narx import get_price
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

@dp.message_handler(text='Savatcha')
async def korzina(message: types.Message):
    try:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Buyurtma berish 🚚")
        products = db.get_products(tg_id=message.from_user.id)
        total = 0
        msg = "Sizning buyurtmalaringiz\n\n"
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            price = get_price(product[1], product[2])
            total += price
            msg += f"{product[1]} x {product[2]} = {price} so'm\n"    

        msg += f"\nUmumiy narx: {total} so'm"
        markup.row("ORQAGA ↩️", "Bo'shatish 🗑")
        await message.answer(msg, reply_markup=markup)
    except:
        await message.answer("Savatchangiz bo'sh,keling men sizga uni yig'ishda yordam beraman!")

@dp.message_handler(text='Savatcha 🛒', state=Kafe.categor)
async def korzina(message: types.Message):
    try:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Buyurtma berish 🚚")
        products = db.get_products(tg_id=message.from_user.id)
        total = 0
        msg = "Sizning buyurtmalaringiz\n\n"
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            price = get_price(product[1], product[2])
            total += price
            msg += f"{product[1]} x {product[2]} = {price} so'm\n"    

        msg += f"\nUmumiy narx: {total} so'm"
        markup.row("ORQAGA ↩️", "Bo'shatish 🗑")
        await message.answer(msg, reply_markup=markup)
    except:
        await message.answer("Savatchangiz bo'sh,keling men sizga uni yig'ishda yordam beraman!")

@dp.message_handler(text='Savatcha 🛒', state=Kafe.product)
async def korzina(message: types.Message):
    try:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Buyurtma berish 🚚")
        products = db.get_products(tg_id=message.from_user.id)
        total = 0
        msg = "Sizning buyurtmalaringiz\n\n"
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            price = get_price(product[1], product[2])
            total += price
            msg += f"{product[1]} x {product[2]} = {price} so'm\n"    

        msg += f"\nUmumiy narx: {total} so'm"
        markup.row("ORQAGA ↩️", "Bo'shatish 🗑")
        await message.answer(msg, reply_markup=markup)
    except:
        await message.answer("Savatchangiz bo'sh,keling men sizga uni yig'ishda yordam beraman!")

