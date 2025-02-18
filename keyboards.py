from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton
)

def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="📥 دانلود محتوا"),
        KeyboardButton(text="👤 اطلاعات پروفایل")
    )
    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="یک گزینه انتخاب کنید..."
    )

def get_back_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="🏠 بازگشت به منو",
        callback_data="main_menu"
    ))
    return builder.as_markup()

def get_download_options():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="🎬 ویدیو", callback_data="video_quality"),
        InlineKeyboardButton(text="🖼 عکس", callback_data="photo_quality"),
        InlineKeyboardButton(text="❌ لغو", callback_data="cancel")
    )
    return builder.as_markup()
