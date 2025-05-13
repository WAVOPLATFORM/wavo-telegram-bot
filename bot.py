
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ChatMemberUpdated
from aiogram.utils import executor
from aiogram.dispatcher.filters import ChatMemberUpdatedFilter
import os

API_TOKEN = os.getenv("BOT_TOKEN")
INVITE_LINK = os.getenv("INVITE_LINK", "https://t.me/WAVO_Initiatives_Test")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.chat_member_handler(ChatMemberUpdatedFilter(member_status_changed=True))
async def welcome_new(chat_member: ChatMemberUpdated):
    if chat_member.new_chat_member.user.is_bot:
        return
    user = chat_member.new_chat_member.user
    await bot.send_message(
        chat_member.chat.id,
        f"🧬 Привет, {user.first_name}! Добро пожаловать в WAVO.\n\n"
        "WAVO — это живой организм. Мы здесь не просто чатимся. Мы эволюционируем.\n\n"
        "**Кто ты?** Напиши цифру:\n"
        "1 — Философ\n"
        "2 — Разработчик\n"
        "3 — Строитель культуры\n"
        "4 — Наблюдатель"
    )

@dp.message_handler(lambda message: message.text in ['1', '2', '3', '4'])
async def handle_role(message: Message):
    roles = {
        '1': "🧠 Философ. Ты — архитектор мышления WAVO.",
        '2': "💻 Разработчик. Ты — руки и сердце WAVO.",
        '3': "🎨 Строитель культуры. Ты — дыхание WAVO.",
        '4': "👁 Наблюдатель. Ты — пространство и свобода WAVO."
    }
    await message.reply(f"{roles[message.text]}\n\n👉 Испытай WAVO в действии: {INVITE_LINK}")

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.reply("Бот работает. Напиши 1-4 для выбора роли.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
