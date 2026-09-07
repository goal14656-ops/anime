import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "BU_YERGA_BOT_TOKENINGNI_YOZ"

CHANNEL_LINK = "https://t.me/animehubuzbek"

bot = Bot(token="8836336061:AAHDYfUKgcsjI8FOwL2yphufOfNkYWyROlU"
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Kanalga obuna bo‘lish",
                    url=CHANNEL_LINK
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Obuna bo‘ldim",
                    callback_data="check"
                )
            ]
        ]
    )

    await message.answer(
        "👋 Salom!\n\n"
        "🎬 Anime botimizga xush kelibsiz!\n\n"
        "Botdan foydalanish uchun avval kanalimizga obuna bo‘ling 👇",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
