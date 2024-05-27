from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

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
    await message.answer("Привет, я твой первый ЭХО бот")

@dp.message_handler(commands="help")
async def start(message: types.Message):
    await message.answer("Я могу помочь тебе с ....")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
