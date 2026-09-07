import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8836336061:AAHDYFUKgcsjI8FOwL2yphufOfNKyWyRO1U"
CHANNEL_LINK = "https://t.me/animehubuzbek"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Kanalga obuna bo'lish",
                    url=CHANNEL_LINK
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Obuna bo'ldim",
                    callback_data="check"
                )
            ]
        ]
    )
    await message.answer(
        "Salom! Botdan foydalanish uchun kanalimizga obuna bo'ling:",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

