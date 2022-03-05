from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.shash_set import sh_set
from keyboards.default.amount import son
from states.state import Kafe

@dp.message_handler(text='Shashlikli setlar 🥩', state=Kafe.categor)
async def salats(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=sh_set)
    await Kafe.next()

@dp.message_handler(text="Shashlikli set (kichik)",state=Kafe.product)
async def shas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/0Bgv3DB", "Shashlikli set (kichik)\n\nМолотый х5\nКуриное филе х5\nРулет х4\nКусковой из говядины х4\nПомидор х1\nФри х2\nСалат Коул сло х1\nОливье х1\nКола 1,5л х1\nЛепешка х2\nСоус х5\n\nNarxi: 280000")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

@dp.message_handler(text="Shashlikli set (katta)",state=Kafe.product)
async def shas(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'name':cat}
    )
    await message.answer_photo("https://ibb.co/XspSYCZ", "Shashlikli set (katta)\n\nМолотый х10\nКрылышки х5\nРулет х6\nКуриное филе х6\nКусковой (говядина) х6\nПечень х5\nПомидор х1\nФри х3,\nСалат Коул сло х2\nОливье х2\nКола 1,5л х2\nЛепешка х4\nСоус х10\n\nNarxi: 550000")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼",reply_markup=son)
    await Kafe.next()

