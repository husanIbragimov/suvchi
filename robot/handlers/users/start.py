from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from keyboards import inline

from lang import languages
from utils.db.models import User
from utils.states import UserState

router = Router()

@router.message(CommandStart())
async def do_start(message: types.Message, state: FSMContext):
    await state.clear()
    await User.get_or_create(
        id=message.from_user.id,
        defaults={
            "username": message.from_user.username,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
        }
    )
    await state.set_state(UserState.lang)
    await message.reply(languages["start"], reply_markup=inline.langs_kb)
