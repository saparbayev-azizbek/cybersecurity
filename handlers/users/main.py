from loader import dp, bot
from aiogram import types
from states.holat import Holat
from aiogram.dispatcher import FSMContext
from source.shirflash.vernam_vijinir import for_shifr
from source.shirflash.gammalash_usuli import main
from source.deshifrlash.gammalash_usuli import main1
from source.shirflash.sezar import sezar1
from source.deshifrlash.sezar import sezar2
from aiogram.dispatcher.filters import Text
from keyboards.inline.buttons import button, button1, reply_markup


@dp.message_handler(commands='boshlash', state=None)
async def cmd_boshlash(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='<b>🙂 Qaysi amalni bajarishni xohlaysiz?👇</b>',
                           reply_markup=button, parse_mode='HTML')
    await Holat.turi.set()

@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.message_handler(text='🔙 Orqaga', state=Holat.kalit)
async def kb_button(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id,
                           text='<b>🙂 Qaysi amalni bajarishni xohlaysiz?👇</b>',
                           reply_markup=button, parse_mode='HTML')
    await Holat.turi.set()


@dp.message_handler(text='❌ Bekor qilish', state=Holat.kalit)
async def kb_button(message: types.Message, state: FSMContext):
    await message.delete()
    await Holat.previous()
    await bot.send_message(chat_id=message.from_user.id, text='<b>✍️ Matnni kiriting!</b>', parse_mode='HTML')
    await Holat.turi.set()


@dp.callback_query_handler(Text(startswith='nom_'), state=Holat.turi)
async def first(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=20)
    data = call.data
    await state.update_data({'turi': data[4:]})
    await call.message.delete()
    if data[4:] == 'shif':
        await call.message.answer(text='<b>🧑‍💻 Shifrlash usulini tanlang</b>',
                                  reply_markup=button1, parse_mode='HTML')
    else:
        await call.message.answer(text='<b>🧑‍💻 Deshifrlash usulini tanlang</b>',
                                  reply_markup=button1, parse_mode='HTML')
    await Holat.next()


@dp.callback_query_handler(Text(startswith='👍'), state=Holat.usuli)
async def second(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=20)
    data = call.data[1:]
    await state.update_data({'usuli': data})
    if data == 'ver' or data == 'gam' or data == 'sez':
        await call.message.answer('<b>✍️ Matnni kiriting!</b>')
        await Holat.next()
    elif data == 'mash':
        await call.message.answer('<b>🛠 Bu bosqich hozircha botda mavjud emas</b>')
        await Holat.turi.set()
        await bot.send_message(chat_id=call.from_user.id,
                               text='<b>🙂 Qaysi amalni bajarishni xohlaysiz?👇</b>',
                               reply_markup=button, parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.TEXT, state=Holat.matn)
async def second(message: types.Message, state: FSMContext):
    matn = message.text

    def tek(matn1):
        a = 0
        for harf in matn1:
            if harf.isalpha() or harf.isspace():
                a += 1
        return a

    if tek(matn) != len(matn):
        await message.answer('<b>⚠️ Iltimos faqat matn kiriting</b>', parse_mode='HTML')
        await Holat.matn.set()
    else:
        await state.update_data({'matn': matn})
        await message.answer('<b>✍️ Endi kalitni yuboring</b>')
        await Holat.kalit.set()


@dp.message_handler(content_types=types.ContentType.TEXT, state=Holat.kalit)
async def third(message: types.Message, state: FSMContext):
    try:
        xabar = message.text
        await state.update_data({'kalit': xabar})
        data = await state.get_data()
        n = data.get("matn")
        shifr = data.get('turi')
        usul = data.get('usuli')
        if shifr == 'shif':
            if usul == 'ver':
                if len(n) == len(xabar):
                    text = for_shifr(n, xabar)
                    await message.answer(text=text, reply_markup=reply_markup)
                else:
                    await message.answer("<b>📋 Matnlar uzunligi to'g'ri kelmadi</b>",
                                         parse_mode='HTML')

            elif usul == 'gam':
                if len(n) == len(xabar):
                    text = main(n, xabar)
                    await message.answer(text=text, reply_markup=reply_markup)
                else:
                    await message.answer("<b>📋 Matnlar uzunligi to'g'ri kelmadi</b>",
                                         parse_mode='HTML')
            elif usul == 'sez':
                if xabar.isdigit():
                    if 1 <= int(xabar) <= 26:
                        son = int(xabar)
                        text = sezar1(n, son)
                        await message.answer(text=text, reply_markup=reply_markup)
                    else:
                        await message.answer(text='<b>1️⃣ va 2️⃣6️⃣ oralig`idagi son kiriting!</b>', parse_mode="HTML")
                else:
                    await message.answer("<b>⚠️ Ilimos faqat raqam kiriting</b>", parse_mode='HTML')
        else:
            if usul == 'ver':
                if len(n) == len(xabar):
                    text = for_shifr(n, xabar)
                    await message.answer(text=text, reply_markup=reply_markup)
                else:
                    await message.answer("<b>📋 Matnlar uzunligi to'g'ri kelmadi</b>",
                                         parse_mode='HTML')
            elif usul == 'gam':
                if len(n) == len(xabar):
                    text = main1(n, xabar)
                    await message.answer(text=text, reply_markup=reply_markup)
                else:
                    await message.answer("<b>📋 Matnlar uzunligi to'g'ri kelmadi</b>",
                                         parse_mode='HTML')
            elif usul == 'sez':
                if xabar.isdigit():
                    if 1 <= int(xabar) <= 26:
                        text = sezar2(n, int(xabar))
                        await message.answer(text=text, reply_markup=reply_markup)
                    else:
                        await message.answer(text='<b>1️⃣ va 2️⃣6️⃣ oralig`idagi son kiriting!</b>', parse_mode="HTML")
                else:
                    await message.answer("<b>⚠️ Ilimos faqat raqam kiriting</b>", parse_mode='HTML')
    except:
        await message.answer("<b>🙅‍♂️ Noto'g'ri ma'lumot kiritdingiz</b>", reply_markup=reply_markup, parse_mode='HTML')

