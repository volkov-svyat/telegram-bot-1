from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboards.keyboards import get_keyboard_1, get_keyboard_2
from keyboards.inline_keyboards import get_inline_cat, get_inline_dog

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Команда, которая запускает бота"),
        types.BotCommand(command="/help", description="Команда, которая расписывает функционал бота")
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Привет, я твой первый ЭХО бот, вот клавиатура", reply_markup=get_keyboard_1())

@dp.message_handler(commands="help")
async def help(message: types.Message):
    await message.answer("Я могу помочь тебе с ....")

@dp.message_handler(lambda message: message.text == "Отправь фото кота")
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id,photo="https://64.media.tumblr.com/1a50aabba50507597a20dba85b59aff2/07c5da4d9ea27f10-81/s2048x3072/4f22f443febca74646b182afa0e8c874fae9696a.jpg",caption="Хотите увидеть целый каталог разных кошачьих пород?",reply_markup=get_inline_cat())

@dp.message_handler(lambda message: message.text == "Перейти на следущую клавиатуру")
async def button_2_click(message: types.Message):
    await message.answer("Тут ты сможешь попросить бота отправить фото собаки",reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == "Отправь фото собаки")
async def button_1_2_click(message: types.Message):
    await bot.send_photo(message.chat.id,photo="https://down.imgspng.com/download/0720/dog_PNG50260.png",caption="Хотите увидеть целый каталог разных пород собак?",reply_markup=get_inline_dog())

@dp.message_handler(lambda message: message.text == "Вернуться на 1 клаиватуру")
async def button_2_2_click(message: types.Message):
    await message.answer("Тут ты сможешь попросить бота отправить фото кота",reply_markup=get_keyboard_1())

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
