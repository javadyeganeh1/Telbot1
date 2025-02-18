import asyncio
import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from config import Config
from keyboards import get_main_keyboard, get_back_keyboard, get_download_options
from instagram import InstagramScraper
from utils import (
    download_file,
    cleanup_temp_files,
    format_profile_info,
    create_progress_bar,
    format_size
)
from exceptions import *

# تنظیمات اولیه
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize
bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()
instagram = InstagramScraper()

# States
class UserStates(StatesGroup):
    waiting_link = State()
    waiting_username = State()

# Handlers
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        Config.WELCOME_MESSAGE,
        reply_markup=get_main_keyboard(),
        parse_mode="MarkdownV2"
    )

@dp.message(lambda m: m.text == "📥 دانلود محتوا")
async def process_download(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.waiting_link)
    await message.answer(
        Config.DOWNLOAD_INSTRUCTION,
        reply_markup=get_back_keyboard(),
        parse_mode="MarkdownV2"
    )

@dp.message(lambda m: m.text == "👤 اطلاعات پروفایل")
async def process_profile(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.waiting_username)
    await message.answer(
        Config.PROFILE_INSTRUCTION,
        reply_markup=get_back_keyboard(),
        parse_mode="MarkdownV2"
    )

@dp.message(UserStates.waiting_link)
async def process_links(message: types.Message, state: FSMContext):
    # منطق کامل پردازش لینک‌ها
    pass

@dp.message(UserStates.waiting_username)
async def process_username(message: types.Message, state: FSMContext):
    # منطق کامل پردازش نام کاربری
    pass

async def main():
    await dp.start_polling(bot)

import os
import asyncio
from aiogram import Bot, Dispatcher

# ... بقیه کدها ...

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "bot:main",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        log_level="info"
    )
