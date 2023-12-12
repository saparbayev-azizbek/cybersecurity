import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram import executor

API_TOKEN = '6694578707:AAH55eAJvgwi9vGtIBio6mdSeTaqhKHlveU'  # O'zingizning botingizni tokeni bilan almashtiring

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def vernam_encrypt(message_text, key):
    encrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message_text, key))
    return encrypted_text

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Men Vernam shifrlash usulidagi botman. Xabar jo'nating.")


@dp.message_handler()
async def encrypt_message(message: types.Message):
    # Shifrlanadigan matn
    plaintext = message.text
    # Random kalit generatsiya qilish
    key1 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in plaintext)
    # Matnni shifrlash
    print(type(key1))
    key = 'dast'
    print(type(key))
    ciphertext = vernam_encrypt(plaintext, key)

    # Shifrlangan matnni jo'natish
    await message.reply(f"Matn: {plaintext}\nKalit: {key}\nShifrlangan matn: {ciphertext}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
