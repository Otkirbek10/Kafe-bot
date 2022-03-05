from loader import dp
from aiogram import types
from keyboards.default.zakuska import zakuskalar
from states.state import Kafe
from aiogram.dispatcher import FSMContext
from keyboards.default.amount import son

@dp.message_handler(text="Холодные закуски", state=Kafe.categor)
async def v(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=zakuskalar)
    await Kafe.next()

@dp.message_handler(text='Suzma',state=Kafe.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/txBwFCS", "Suzma\n\nNarxi: 7500 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Ruscha Seld balig'i",state=Kafe.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/56NbjCj", "Ruscha Seld balig'i\n\nNarxi: 21000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text='Assorti',state=Kafe.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/xHfXcHX", "Assorti\n\nNarxi: 72000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text='Xolodes',state=Kafe.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/6w6C8Yd", "Xolodes\n\nNarxi: 17000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text='Assorti (tuzli)',state=Kafe.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/z5Pp4wk", "Assorti (tuzli)\n\nNarxi: 16000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text='Свежие нарезки',state=Kafe.product)
async def suzm(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/5rGbdxk", "Свежие нарезки\n\nNarxi: 15000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()