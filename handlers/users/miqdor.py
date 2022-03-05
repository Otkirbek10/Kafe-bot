from aiogram import types
from keyboards.default.baliqlar import fishs
from keyboards.default.shashlik_turi import shashliklar
from keyboards.default.salats import salatlar
from keyboards.default.zakuska import zakuskalar
from keyboards.default.drinks import suvlar
from keyboards.default.shurvalar import shurvalar
from keyboards.default.ikkinchi import second
from keyboards.default.bread import nonlar
from keyboards.default.kombolar import kombos
from keyboards.default.shash_set import sh_set
from aiogram.dispatcher import FSMContext
from states.state import Kafe
from handlers.users.narx import price
from loader import dp, db

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@dp.message_handler(state=Kafe.amount)
async def gg(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        od = data.get('name')
        cat = data.get('cat')
        if cat == 'Shashlik':
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=shashliklar)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            
            await Kafe.product.set()
        elif cat == 'Baliq 🐠':
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=fishs)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kafe.product.set()

        elif cat == "Холодные закуски":
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=zakuskalar)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kafe.product.set()

        elif cat == "Salatlar":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=salatlar)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kafe.product.set()

        elif cat == "Ichimliklar 🥤":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=suvlar)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kafe.product.set()

        elif cat == "Sho'rva":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=shurvalar)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kafe.product.set()

        elif cat == 'Ikkinchi ovqatlar 🍛':
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=second)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kafe.product.set()
        
        elif cat == 'Non 🥯':
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=nonlar)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kafe.product.set()

        elif cat == 'Kombo 🍛🥤':
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=kombos)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kafe.product.set()
        
        elif cat == 'Shashlikli setlar 🥩':
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=sh_set)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kafe.product.set()
    else:
        await message.answer("Faqat son kiriting!")
        await Kafe.amout.set()