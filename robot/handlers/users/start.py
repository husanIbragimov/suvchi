from aiogram import Router, types
from utils.db.models import User  
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart())
async def register_user(message: types.Message):
    user, created = await User.get_or_create(
        id=message.from_user.id,
        defaults={
            "username": message.from_user.username,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
        }
    )
    if created:
        await message.answer("✅ Siz ro‘yxatdan o‘tdingiz!")
    else:
        await message.answer("🔹 Siz allaqachon ro‘yxatdan o‘tgansiz.")
