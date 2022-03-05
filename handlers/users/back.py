from loader import dp
from aiogram import types
from states.state import Kafe
from keyboards.default.asosiy import menu
from keyboards.default.categoriya import cats
from aiogram.dispatcher import FSMContext
from keyboards.default.drinks import suvlar
from keyboards.default.baliqlar import fishs
from keyboards.default.ikkinchi import second
from keyboards.default.shashlik_turi import shashliklar
from keyboards.default.zakuska import zakuskalar
from keyboards.default.salats import salatlar
from keyboards.default.shurvalar import shurvalar
from keyboards.default.bread import nonlar
from keyboards.default.kombolar import kombos
from keyboards.default.shash_set import sh_set

@dp.message_handler(text="ORQAGA ↩️", state=Kafe.categor)
async def back_cat(message: types.Message, state: FSMContext):
	await message.answer("Sahifani tanlang 😊", reply_markup=menu)
	await state.finish()

@dp.message_handler(text="ORQAGA ↩️", state=Kafe.product)
async def back_prod(message: types.Message):
    await message.answer("Taomlarni tanlash uchun sahifani tanlang",reply_markup=cats)
    await Kafe.categor.set()

@dp.message_handler(text="Bosh Sahifa 🏠", state=Kafe.amount)
async def back_amount(message: types.Message,state: FSMContext):
	await message.answer("Buyurtma berishni boshlaymizmi?", reply_markup=menu)
	await state.finish()

@dp.message_handler(text="Bosh Sahifa 🏠", state=Kafe.categor)
async def back_amount(message: types.Message,state: FSMContext):
	await message.answer("Buyurtma berishni boshlaymizmi?", reply_markup=menu)
	await state.finish()


@dp.message_handler(text = 'ORQAGA ↩️',state=Kafe.amount)
async def back_a(message:types.Message, state: FSMContext):
    data = await state.get_data()
    cat = data.get('cat')
    if cat == "Shashlik":
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=shashliklar)
    elif cat == 'Baliq 🐠':
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=fishs)
    elif cat == 'Холодные закуски':
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=zakuskalar)
    elif cat == 'Salatlar':
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=salatlar)
    elif cat == "Sho'rva":
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=shurvalar)
    elif cat == 'Ichimliklar 🥤':
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=suvlar)
    elif cat == 'Ikkinchi ovqatlar 🍛':
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=second)
    elif cat == "Non 🥯":
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=nonlar)
    elif cat == 'Kombo 🍛🥤':
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=kombos)
    elif cat == 'Shashlikli setlar 🥩':
        await message.answer("Batafsil ma'lumot uchun taomni tanlang",reply_markup=sh_set)
    await Kafe.product.set()


  








