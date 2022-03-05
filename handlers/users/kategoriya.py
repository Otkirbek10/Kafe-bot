from loader import dp
from aiogram import types
from keyboards.default.categoriya import cats
from states.state import Kafe
from aiogram.dispatcher import FSMContext
from keyboards.default.baliqlar import fishs
from keyboards.default.drinks import suvlar
from keyboards.default.ikkinchi import second
from keyboards.default.shashlik_turi import shashliklar
from keyboards.default.zakuska import zakuskalar
from keyboards.default.salats import salatlar
from keyboards.default.shurvalar import shurvalar
from keyboards.default.bread import nonlar
from keyboards.default.kombolar import kombos
from keyboards.default.shash_set import sh_set


@dp.message_handler(text="Shashlik",state=Kafe.categor)
async def sh_amount(message: types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot olish uchun taomni tanlang",reply_markup=shashliklar)
    await Kafe.next()


@dp.message_handler(text = 'Baliq 🐠',state=Kafe.categor)
async def b_amount(message:types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot olish uchun taomni tanlang",reply_markup=fishs)
    await Kafe.next()

@dp.message_handler(text = 'Холодные закуски',state=Kafe.categor)
async def b_amount(message:types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot olish uchun taomni tanlang",reply_markup=zakuskalar)
    await Kafe.next()

@dp.message_handler(text = 'Salatlar',state=Kafe.categor)
async def b_amount(message:types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot olish uchun taomni tanlang",reply_markup=salatlar)
    await Kafe.next()

@dp.message_handler(text = "Sho'rva",state=Kafe.categor)
async def b_amount(message:types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot olish uchun taomni tanlang",reply_markup=shurvalar)
    await Kafe.next()

@dp.message_handler(text = 'Ichimliklar 🥤',state=Kafe.categor)
async def gd(message:types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot uchun ichimlikni  tanlang",reply_markup=suvlar)
    await Kafe.next()


@dp.message_handler(text = 'Ikkinchi ovqatlar 🍛',state=Kafe.categor)
async def gd(message:types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot uchun ichimlikni  tanlang",reply_markup=second)
    await Kafe.next()

@dp.message_handler(text = 'Non 🥯',state=Kafe.categor)
async def gd(message:types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot uchun ichimlikni  tanlang",reply_markup=nonlar)
    await Kafe.next()

@dp.message_handler(text = 'Kombo 🍛🥤',state=Kafe.categor)
async def gd(message:types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot uchun ichimlikni  tanlang",reply_markup=kombos)
    await Kafe.next()

@dp.message_handler(text = "'Shashlikli setlar 🥩'",state=Kafe.categor)
async def gd(message:types.Message, state: FSMContext):
    cat =message.text
    await state.update_data(
        {'cat':cat}
    )
    await message.answer("Batafsil ma'lumot uchun ichimlikni  tanlang",reply_markup=sh_set)
    await Kafe.next()





