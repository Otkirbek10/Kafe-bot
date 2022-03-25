from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.state import Kafe
from keyboards.default.amount import son
from keyboards.default.shurvalar import shurvalar

@dp.message_handler(text="Sho'rva", state=Kafe.categor)
async def shurva(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat': cat}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=shurvalar)
    await Kafe.next()

@dp.message_handler(text="Mastava", state=Kafe.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/m5N1h03", "Mastava\n\nNarxi: 16000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()


@dp.message_handler(text="Moshxurda", state=Kafe.product)
async def shur(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/m5N1h03", "Moshxurda\n\nNarxi: 16000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()


@dp.message_handler(text="Borsh", state=Kafe.product)
async def shurv(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/V96PMps", "Borsh\n\nNarxi: 16000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()


@dp.message_handler(text="Frikadelkali sho'rva", state=Kafe.product)
async def shurva(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/x7RWHgK", "Frikadelkali sho'rva\n\nNarxi: 15000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()


@dp.message_handler(text="Sho'rva(mol go'shti)", state=Kafe.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/8XNH8kq", "Sho'rva(mol go'shti)\n\nNarxi: 19000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()


@dp.message_handler(text="Solyanka", state=Kafe.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/TgTNsVF", "Solyanka\n\nNarxi: 17000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Balaza", state=Kafe.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/ZHhN775", "Balaza\n\nNarxi: 18000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Chuchvara", state=Kafe.product)
async def mas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/r7rwVND", "Chuchvara\n\nNarxi: 15000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()
