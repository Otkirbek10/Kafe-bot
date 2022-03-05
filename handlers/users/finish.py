
from loader import dp
from aiogram import types
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

@dp.message_handler(state=Kafe.amount)
async def order(message: types.Message, state: FSMContext):
	amount = message.text
	await state.update_data({
		'amount': amount
	})
	data = await state.get_data()
	cat = data.get('cat')
	if cat == "Shashlik":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=shashliklar)
	elif cat == "Baliq 🐠":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=fishs)
	elif cat == "Холодные закуски":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=zakuskalar)
	elif cat == "Salatlar":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=salatlar)
	elif cat == "Sho'rva":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=shurvalar)
	elif cat == "Ichimliklar 🥤":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=suvlar)
	elif cat == "Ikkinchi ovqatlar 🍛":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=second)
	elif cat == "Non 🥯":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=nonlar)
	elif cat == 'Kombo 🍛🥤':
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=kombos)	
	elif cat == 'Shashlikli setlar 🥩':
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=sh_set)

	await Kafe.product.set()
	
























# @dp.message_handler(state=Kafe.amount)
# async def order(message:types.Message, state: FSMContext):
#     amount = message.text
#     await state.update_data(
#         {'amount':amount}
#     )
#     await message.answer("Savatchaga🛒 qo'shildi")
#     await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=fishs)
#     await Kafe.product.set()
    