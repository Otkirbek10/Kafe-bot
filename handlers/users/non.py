from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.amount import son
from keyboards.default.bread import nonlar
from states.state import Kafe

@dp.message_handler(text='Non 🥯', state=Kafe.categor)
async def salats(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=nonlar)
    await Kafe.next()

@dp.message_handler(text="Kichkina non (300gr)",state=Kafe.product)
async def olivye(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/7bCChy3", "Kichkina non 300gr\n\nNarxi: 3500 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()