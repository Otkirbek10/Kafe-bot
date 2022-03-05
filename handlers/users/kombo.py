from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.kombolar import kombos
from keyboards.default.amount import son
from states.state import Kafe

@dp.message_handler(text='Kombo 🍛🥤', state=Kafe.categor)
async def salats(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=kombos)
    await Kafe.next()

@dp.message_handler(text="Сет Мясо по-китайски",state=Kafe.product)
async def kombo(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/cr0b6nQ", "Сет Мясо по-китайски\n\nМясо по-китайски, Хлеб, Coca-Cola 0,5\n\nNarxi: 37000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Сет Курица с овощами",state=Kafe.product)
async def kombo(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/b3PWLy3", "Сет Курица с овощами\n\nКурица с овощами, Хлеб, Coca-Cola 0,5\n\nNarxi: 29000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Сет Бифштекс",state=Kafe.product)
async def kombo(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://www.linkpicture.com/q/photo_2022-03-03_10-22-06.jpg", "Сет Бифштекс\n\nБифштекс, Хлеб, Coca-Cola 0,5\n\nNarxi: 28000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Сет Телятина с грибами",state=Kafe.product)
async def kombo(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://www.linkpicture.com/q/photo_2022-03-03_10-34-13.jpg", "Сет Телятина с грибами\n\nТелятина с грибами, Хлеб, Coca-Cola 0,5\n\nNarxi: 38000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Сет Бефстроганов",state=Kafe.product)
async def kombo(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/cQNXsgn", "Сет Бефстроганов\n\nБефстроганов, Хлеб, Coca-Cola 0,5\n\nNarxi: 30000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Сет Курица с грибами",state=Kafe.product)
async def kombo(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/hZqbPmh", "Сет Курица с грибами\n\nБефстроганов, Хлеб, Coca-Cola 0,5\n\nNarxi: 30000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()






