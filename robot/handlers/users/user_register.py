import random
from datetime import datetime

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, Contact

from keyboards.builders import share_phone, inline_kb
from lang import languages
from utils.db.models import User, CheckPhone
from utils.services import send_sms
from utils.states import UserState

router = Router()


@router.callback_query(F.data == 'register')
async def register_user(callback: CallbackQuery, state: FSMContext):
    lang = (await state.get_data()).get("lang", "uz")
    await state.set_state(UserState.full_name)
    await callback.message.answer(
        languages["ask_full_name"][lang],
    )


@router.message(UserState.full_name)
async def get_full_name(message: Message, state: FSMContext):
    lang = (await state.get_data()).get("lang", "uz")
    full_name = message.text
    await state.update_data(full_name=full_name)
    print(languages["ask_phone_number"][lang])
    await message.answer(
        text=languages["ask_phone_number"][lang],
        reply_markup=share_phone(languages["share_phone"][lang])
    )
    await state.set_state(UserState.phone_number)


@router.message(UserState.phone_number, F.contact)
async def get_phone_number(message: Contact, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    phone_number = message.contact.phone_number

    resend = await inline_kb(
        languages["resend_sms_btn"][lang], "resend")
    await User.filter(id=message.from_user.id).update(
        full_name=data.get('full_name'),
        lang=lang,
        phone_number=phone_number
    )
    code = random.randint(100000, 999999)
    await send_sms(phone_number, code)
    await CheckPhone.get_or_create(
        user_id=message.from_user.id,
        defaults={
            "code": 123456,
        }
    )
    await state.set_state(UserState.code)
    await message.answer(
        text=languages["send_sms"][lang],
        reply_markup=resend
    )


@router.callback_query(F.data == 'resend')
async def resend_sms(callback: CallbackQuery, state: FSMContext, bot: Bot):
    lang = (await state.get_data()).get("lang", "uz")

    message_timestamp = callback.message.date.timestamp()
    current_timestamp = datetime.now().timestamp()
    time_difference_seconds = current_timestamp - message_timestamp
    print("Time difference in seconds:", time_difference_seconds)

    if time_difference_seconds < 60:
        remaining_time = int(60 - time_difference_seconds)
        await callback.answer(
            text=languages["fail_sms_servie"][lang].replace("60", str(remaining_time)),
            show_alert=True
        )
        return

    if time_difference_seconds > 300:
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)
        return
    user = await User.get(id=callback.from_user.id)
    code = random.randint(100000, 999999)

    await send_sms(user.phone_number, code)
    await CheckPhone.update_or_create(
        user_id=callback.from_user.id,
        defaults={
            "code": 123456,
        }
    )
    await state.set_state(UserState.code)
    await callback.answer(
        text=languages["send_sms"][lang],
        show_alert=True
    )


@router.message(UserState.code)
async def get_code(message: Message, state: FSMContext):
    lang = (await state.get_data()).get("lang", "uz")
    code = message.text
    user = await CheckPhone.get_or_none(user_id=message.from_user.id, code=code)
    if not user:
        await message.answer(languages["sms_code_error"][lang])
        return
    if user:
        await User.filter(id=message.from_user.id).update(is_active=True)
        await CheckPhone.filter(user_id=message.from_user.id).delete()
        await message.answer(languages["success_register"][lang])
