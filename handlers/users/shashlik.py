from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.shashlik_turi import shashliklar
from keyboards.default.amount import son
from states.state import Kafe

@dp.message_handler(text="Shashlik",state=Kafe.categor)
async def orqa1(message: types.Message, state: FSMContext):
    shash = message.text
    data = await state.get_data()
    
    if 'cart' in data.keys():
        cart = data.get('cart')
        await state.update_data(
            {
                'cart': cart
            }
        )
    else:
        await state.update_data(
            {'cat':shash, 'cart': []},
        )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=shashliklar)
    await Kafe.next()


@dp.message_handler(text="Kuskavoy (mol go'shti)",state=Kafe.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/8MXjNJG", "Kuskavoy (mol go'shti)\n\nNarxi: 13500 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Kuskavoy (qo'y go'shti)",state=Kafe.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/vDxXnNX", "Kuskavoy (qo'y go'shti)\n\nNarxi: 14000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Rulet",state=Kafe.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/fCZVKzB", "Rulet\n\nNarxi: 17000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="2 ichida 1",state=Kafe.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/RptdkVH", "2 ichida 1\n\nNarxi: 14000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Napoleon",state=Kafe.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/MGFB6Rn", "Napoleon\n\nNarxi: 17000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Qiymali kabob",state=Kafe.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/9WMk5YR", "Qiymali kabob\n\nNarxi: 12500 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Jigar kabob",state=Kafe.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/RyyzGb4", "Jigar kabob\n\nNarxi: 11000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Tovuq filesi",state=Kafe.product)
async def orqa1(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/42Xd5J8", "Tovuq filesi\n\nNarxi: 10000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



