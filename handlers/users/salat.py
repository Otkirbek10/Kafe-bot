from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.salats import salatlar
from keyboards.default.amount import son
from states.state import Kafe

@dp.message_handler(text='Salatlar', state=Kafe.categor)
async def salats(message: types.Message, state: FSMContext):
    shash = message.text
    await state.update_data(
        {'cat':shash}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=salatlar)
    await Kafe.next()

@dp.message_handler(text="Olivye",state=Kafe.product)
async def olivye(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/9brLns7", "Olivye\n\nNarxi: 20000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Smak",state=Kafe.product)
async def smak(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/m5jy6w5", "Smak\n\nNarxi: 14000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Cesar",state=Kafe.product)
async def cesr(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/wg8wrbM", "Cesar\n\nNarxi: 20000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Fransuzcha",state=Kafe.product)
async def fran(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/8zfLFqv", "Fransuzcha\n\nNarxi: 21000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Mimoza",state=Kafe.product)
async def mimoza(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/Mc4S3x2", "Mimoza\n\nNarxi: 24000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Селёдка под шубой",state=Kafe.product)
async def ss(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/87N0mt0", "Селёдка под шубой\n\nNarxi: 24000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Vinigret",state=Kafe.product)
async def ving(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/3c8wXMd", "Vinigret\n\nNarxi: 11000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()


@dp.message_handler(text="Grecheskiy",state=Kafe.product)
async def ving(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/1RXmqXx", "Vinigret\n\nNarxi: 24000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()