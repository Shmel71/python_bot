from aiogram import Bot, Dispatcher, executor, types
import string
import random

from aiogram.types import message, InputFile

TOKEN = "5447551279:AAFPnuYC_Pts8ow87dk9x2AleguyZzJSgTA"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

HELP_COMMAND = '''
/help - список
/start - начать работу
/pic - картинка
'''


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply(text=HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['start'])
async def help(message: types.Message):
    await message.answer(text="Ok, lets go!")
    await message.delete()


@dp.message_handler(commands=['pic'])
async def give(message: types.Message):
    photo = InputFile("P1010643.JPG")
    await message.answer(text="Держи!")
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler()
async def send_random(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))


if __name__ == '__main__':
    executor.start_polling(dp)
