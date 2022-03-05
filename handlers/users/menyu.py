from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.categoriya import cats
from keyboards.default.asosiy import menu
from states.state import Kafe

@dp.message_handler(text = 'Menu')
async def get_menu(message:types.Message):
    await message.answer("Xo'sh, buyurtmaga o'tamizmi, sizni issiq taomlarimiz kutmoqda 👨🏻‍🍳🔥",reply_markup=cats)
    await Kafe.categor.set()

@dp.message_handler(text="Bosh Sahifa 🏠", state=Kafe.product)
async def mennu(message: types.Message, state: FSMContext):
    await message.answer(f"Buyurtma berishni boshlaymizmi?😊", reply_markup=menu)
    await state.finish()
