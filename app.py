from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7266035860:AAFSHIDBIuJindOQAxYMZF9EoCjmmO9v_io'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(text="Open Web App", web_app=types.WebAppInfo(url="https://neurospacex-ruspamlib-serverandsite.hf.space"))
    keyboard.add(web_app_button)
    await message.answer("Welcome! Click the button below to open the web app.", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
