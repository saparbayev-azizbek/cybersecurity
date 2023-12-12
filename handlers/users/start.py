from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>✋ Assalomu alaykum, <i>{message.from_user.full_name}!</i></b>\n"
                         f"<b>🤖 Shifrlashni boshlash uchun /boshlash buyrug'ini tanlang</b>")
