import os

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.context import FSMContext

from data.config import BASE_DIR
from keyboards.builders import inline_kb
from lang import languages
from utils.db.models import User

router = Router()


@router.callback_query(F.data.in_(['uz', 'ru', 'en']))
async def set_language(callback: CallbackQuery, state: FSMContext):
    lang = callback.data
    local_path = f"{BASE_DIR}/assets/img.png"
    register_btn = await inline_kb(languages["register"][lang], f"register")

    await state.update_data(lang=lang)
    await User.filter(id=callback.from_user.id).update(lang=lang)
    if os.path.exists(local_path):
        await callback.message.answer_photo(
            photo=FSInputFile(path=local_path),
            caption=languages["welcome"][lang],
            reply_markup=register_btn
        )
    else:
        await callback.message.answer(
            languages["welcome"][lang],
            reply_markup=register_btn
        )
