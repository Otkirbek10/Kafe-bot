from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.amount import son
from keyboards.default.baliqlar import fishs
from states.state import Kafe



@dp.message_handler(text="Baliq 🐠", state=Kafe.categor)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
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
            {'cat':cat, 'cart': []},
        )
    
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=fishs)
    await Kafe.next()


@dp.message_handler(text="Sazan (300g)", state=Kafe.product)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/XYMMF4D", "Sazan (300g)\n\nNarxi: 45000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Sudak (300g)", state=Kafe.product)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/D7m47gs", "Sudak (300g)\n\nNarxi: 48000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Sous 300ml", state=Kafe.product)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer("Sous 300ml\n\nNarxi: 7000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()



@dp.message_handler(text="Sous 500ml", state=Kafe.product)
async def baliq(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer("Sous 500ml\n\nNarxi: 11000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()
