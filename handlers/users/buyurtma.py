from loader import dp
from aiogram import types
from keyboards.default.zakaz import zak,loc
from states.state import Kafe
from aiogram.dispatcher import FSMContext
from keyboards.default.categoriya import cats


@dp.message_handler(text="Buyurtma berish 🚚")
async def zakaz(message:types.Message):
    await message.answer("Buyurtmani berishda mening ko'rsatmalarimga amal qiling")
    await message.answer("<i>Buyurtma turini tanlang</i>",parse_mode="html",reply_markup=zak)

@dp.message_handler(text="Buyurtma berish 🚚",state=Kafe.categor)
async def zakaz(message:types.Message,state:FSMContext):
    await message.answer("Buyurtmani berishda mening ko'rsatmalarimga amal qiling")
    await message.answer("<i>Buyurtma turini tanlang</i>",parse_mode="html",reply_markup=zak)

@dp.message_handler(text="Buyurtma berish 🚚",state=Kafe.product)
async def zakaz(message:types.Message,state:FSMContext):
    await message.answer("Buyurtmani berishda mening ko'rsatmalarimga amal qiling")
    await message.answer("<i>Buyurtma turini tanlang</i>",parse_mode="html",reply_markup=zak)

@dp.message_handler(text="Yetkazib berish 🚕")
async def zakaz(message:types.Message):
    await message.answer("Geolokatsiyangizni jo'nating📍, va men sizga eng yaqin bo'lgan filialni aniqlayman ☕️ ")
    await message.answer("<i>Joingizni jo'nayotganda, geolokatsiyangiz aniqligini tekshiring</i>",parse_mode="html",reply_markup=loc)

@dp.message_handler(text="Yetkazib berish 🚕",state=Kafe.categor)
async def zakaz(message:types.Message):
    await message.answer("Geolokatsiyangizni jo'nating📍, va men sizga eng yaqin bo'lgan filialni aniqlayman ☕️ ")
    await message.answer("<i>Joingizni jo'nayotganda, geolokatsiyangiz aniqligini tekshiring</i>",parse_mode="html",reply_markup=loc)

@dp.message_handler(text="Yetkazib berish 🚕",state=Kafe.product)
async def zakaz(message:types.Message):
    await message.answer("Geolokatsiyangizni jo'nating📍, va men sizga eng yaqin bo'lgan filialni aniqlayman ☕️ ")
    await message.answer("<i>Joingizni jo'nayotganda, geolokatsiyangiz aniqligini tekshiring</i>",parse_mode="html",reply_markup=loc)

@dp.message_handler(text='ORQAGA🔙')
async def bak(message:types.Message):
    await message.answer("<i>Buyurtma turini tanlang</i>",reply_markup=zak)

@dp.message_handler(text='ORQAGA🔙',state=Kafe.categor)
async def bak(message:types.Message,state:FSMContext):
    await message.answer("<i>Buyurtma turini tanlang</i>",reply_markup=zak)
    await state.finish()

@dp.message_handler(text='ORQAGA🔙',state=Kafe.product)
async def bak(message:types.Message):
    await message.answer("<i>Buyurtma turini tanlang</i>",reply_markup=zak)

@dp.message_handler(text="O’zim olib ketaman 🚶🏻")
async def ds(message:types.Message):
    await message.answer("Geolokatsiyangizni jo'nating📍, va men sizga eng yaqin bo'lgan filialni aniqlayman ☕️ ")
    await message.answer("<i>Joingizni jo'nayotganda, geolokatsiyangiz aniqligini tekshiring</i>",parse_mode="html",reply_markup=loc)


@dp.message_handler(text="O’zim olib ketaman 🚶🏻",state=Kafe.categor)
async def ds(message:types.Message):
    await message.answer("Geolokatsiyangizni jo'nating📍, va men sizga eng yaqin bo'lgan filialni aniqlayman ☕️ ")
    await message.answer("<i>Joingizni jo'nayotganda, geolokatsiyangiz aniqligini tekshiring</i>",parse_mode="html",reply_markup=loc)

@dp.message_handler(text="O’zim olib ketaman 🚶🏻",state=Kafe.product)
async def ds(message:types.Message):
    await message.answer("Geolokatsiyangizni jo'nating📍, va men sizga eng yaqin bo'lgan filialni aniqlayman ☕️ ")
    await message.answer("<i>Joingizni jo'nayotganda, geolokatsiyangiz aniqligini tekshiring</i>",parse_mode="html",reply_markup=loc)



@dp.message_handler(text="Bekor qilish♨️")
async def bek(message:types.Message,state:FSMContext):
    await message.answer("Buyurtma berish fikringizdan qaytganingizdan afsusdamiz😞",reply_markup=cats)
    await Kafe.categor.set()

@dp.message_handler(text="Bekor qilish♨️",state=Kafe.categor)
async def bek(message:types.Message,state:FSMContext):
    await message.answer("Buyurtma berish fikringizdan qaytganingizdan afsusdamiz😞",reply_markup=cats)
    await Kafe.categor.set()

@dp.message_handler(text="Bekor qilish♨️",state=Kafe.product)
async def bek(message:types.Message,state:FSMContext):
    await message.answer("Buyurtma berish fikringizdan qaytganingizdan afsusdamiz😞",reply_markup=cats)
    await Kafe.categor.set()


    
