from aiogram import types
from loader import dp


@dp.message_handler(text='123')
async def one_two_three(message: types.Message):
    await message.answer(text="Вы написали 123")
