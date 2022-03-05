from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
# from keyboards.default.drinks import suvlar
from keyboards.default.amount import son
from states.state import Kafe

@dp.message_handler(text = 'Coca-Cola (0,5 L)',state=Kafe.product)
async def get_lk(message:types.Message,state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name': cat}
    )
    await message.answer("Coca-Cola (0,5 L)\n\nNarxi: 7000 so'm")
    await message.answer("Maxsulotni Savatga qo'shish uchun,sonini kiriting",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text = 'Coca-Cola (1,0 L)',state=Kafe.product)
async def get_lk(message:types.Message,state: FSMContext):
    cat = message.text
    await state.update_data(
        {"name": cat}
    )
    await message.answer("Coca-Cola (1,0 L)\n\nNarxi: 11000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text = 'Coca-Cola (1,5 L)',state=Kafe.product)
async def get_lk(message:types.Message,state: FSMContext):
    cat = message.text
    await state.update_data(
        {"name": cat}
    )
    await message.answer("Coca-Cola (1,5 L)\n\nNarxi: 13000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text = 'Fanta (0,5 L)',state=Kafe.product)
async def get_lk(message:types.Message,state: FSMContext):
    cat = message.text
    await state.update_data(
        {"name": cat}
    )
    await message.answer("Fanta (0,5 L)\n\nNarxi: 7000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text = 'Fanta (1,0 L)',state=Kafe.product)
async def get_lk(message:types.Message,state: FSMContext):
    cat = message.text
    await state.update_data(
        {"name": cat}
    )
    await message.answer("Fanta (1,0 L)\n\nNarxi: 10000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()    

@dp.message_handler(text = 'Fanta (1,5 L)',state=Kafe.product)
async def get_lk(message:types.Message,state: FSMContext):
    cat = message.text
    await state.update_data(
        {"name": cat}
    )
    await message.answer("Fanta (1,5 L)\n\nNarxi: 13000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

