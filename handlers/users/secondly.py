from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.amount import son
from states.state import Kafe

@dp.message_handler(text = 'Мясо по-гречески',state=Kafe.product)
async def ik(message:types.Message,state:FSMContext):
    cat = message.text
    await state.update_data(
        {'name': cat}
    )
    await message.answer_photo(photo='https://www.linkpicture.com/q/photo_2022-02-21_21-04-50.jpg',caption='Мясо по-гречески\n\nNarxi: 28000 so\'m')
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text = 'Мясо по-французски',state=Kafe.product)
async def pf(message:types.Message,state:FSMContext):
    cat = message.text
    await state.update_data(
        {'name': cat}
    )
    await message.answer_photo(photo="https://www.linkpicture.com/q/photo_2022-02-21_21-14-37.jpg",caption="Мясо по-французски\n\nNarxi: 28000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text = 'Мясо по-царски',state=Kafe.product)
async def ph(message:types.Message,state:FSMContext):
    cat = message.text
    await state.update_data(
        {'name': cat}
    )
    await message.answer_photo(photo="https://www.linkpicture.com/q/photo_2022-02-21_21-20-44.jpg",caption='Мясо по-царски\n\nNarxi: 28000 so\'m')
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text = 'Мясо по-армянски',state=Kafe.product)
async def ph(message:types.Message,state:FSMContext):
    cat = message.text
    await state.update_data(
        {'name': cat}
    )
    await message.answer_photo(photo="https://www.linkpicture.com/q/photo_2022-02-21_21-22-32.jpg",caption='Мясо по-армянски\n\nNarxi: 28000 so\'m')
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text = 'Мишель',state=Kafe.product)
async def ph(message:types.Message,state:FSMContext):
    cat = message.text
    await state.update_data(
        {'name': cat}
    )
    await message.answer_photo(photo="https://www.linkpicture.com/q/photo_2022-02-21_23-00-06.jpg",caption='Мишель\n\nNarxi: 30000 so\'m')
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()


@dp.message_handler(text = 'Bifshteks',state=Kafe.product)
async def ph(message:types.Message,state:FSMContext):
    cat = message.text
    await state.update_data(
        {'name': cat}
    )
    await message.answer_photo(photo="https://www.linkpicture.com/q/photo_2022-02-21_23-05-28.jpg",caption='Bifshteks\n\nNarxi: 20000 so\'m')
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()


