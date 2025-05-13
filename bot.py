
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("BOT_TOKEN")
INVITE_LINK = os.getenv("INVITE_LINK", "https://t.me/WAVO_Initiatives_Test")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработка новых участников в чате
@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def welcome_new(message: types.Message):
    for new_member in message.new_chat_members:
        if new_member.is_bot:
            return
        await message.reply(
            f"🧬 Привет, {new_member.first_name}! Добро пожаловать в WAVO.\n\n"
            "Ты не просто в чате. Ты — у входа в живую систему.\n\n"
            "**Кто ты?** Напиши цифру:\n"
            "1 — Философ\n"
            "2 — Разработчик\n"
            "3 — Строитель культуры\n"
            "4 — Наблюдатель"
        )

# Обработка выбора роли
@dp.message_handler(lambda message: message.text in ['1', '2', '3', '4'])
async def handle_role(message: Message):
    roles = {
        '1': "🧠 Философ. Ты — архитектор мышления WAVO.",
        '2': "💻 Разработчик. Ты — руки и сердце WAVO.",
        '3': "🎨 Строитель культуры. Ты — дыхание WAVO.",
        '4': "👁 Наблюдатель. Ты — пространство и свобода WAVO."
    }
    await message.reply(f"{roles[message.text]}\n\n👉 Испытай WAVO в действии: {INVITE_LINK}")

# /start команда для ручного запуска
@dp.message_handler(commands=['start'])
async def send_start(message: Message):
    await message.reply("Бот работает. Напиши 1-4 для выбора роли.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
