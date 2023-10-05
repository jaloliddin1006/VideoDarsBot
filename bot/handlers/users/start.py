from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.api import *
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from keyboards.default.defoult_btn import get_book_category_btn, menu_btn
import requests


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = message.from_user
    username = user.username if user.username else " "
    first_name = user.first_name if user.first_name else " "
    last_name = user.last_name if user.last_name else " "
    is_active = True
    create_user(telegram_id=message.from_user.id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                is_active = True)
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!", reply_markup=menu_btn)
    

@dp.message_handler(text = "✍️ Xabar yozish")
async def bot_start(message: types.Message, state=FSMContext):
    await message.answer("Xabar yuboring", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("feedback")
    

@dp.message_handler(state="feedback")
async def input_password(message: types.Message, state: FSMContext):
    feedback(message.from_user.id, message.text)
    await message.answer("Xabaringiz qabul qilindi", reply_markup=menu_btn)
    await state.finish()
    
    
@dp.message_handler(text = "📚 Online darslar")
async def bot_start(message: types.Message, state=FSMContext):
    books_category = category_info()
    if books_category:
        await message.answer("Bo'limni tanlang", reply_markup=get_book_category_btn(books_category))
        await state.set_state("category")
    else:
        await message.answer("Bo'lim mavjud emas")
    
    
@dp.message_handler(text = "🔙 Ortga", state="category") 
async def bot_start(message: types.Message, state=FSMContext):
    await message.answer("Bo'limni tanlang", reply_markup=menu_btn)
    await state.finish()


    
@dp.message_handler(state="category")
async def input_password(message: types.Message, state: FSMContext):
    category = message.text
    books_category = category_info(category)
    if books_category:
        await state.update_data({
            "category":category})
        await message.answer("Bo'limni tanlang.....", reply_markup=get_book_category_btn(books_category))
        await state.set_state("book_subcategory")
    else:
        await message.answer("Bo'lim mavjud emas")
    

@dp.message_handler(text = "🔙 Ortga", state="book_subcategory")
async def asgdsg(message: types.Message, state=FSMContext):
    books_category = category_info()
    await message.answer("Bo'limni tanlang", reply_markup=get_book_category_btn(books_category))
    await state.set_state("category")

@dp.message_handler(state="book_subcategory")
async def subcategory_func(message: types.Message, state=FSMContext):
    data = await state.get_data()
    category = data['category']
    subcategory = message.text
    sources = get_source_list(subcategory)
    if sources:
        for i in sources:
            text = f"{i['name']}\n\n"
            text += f"{i['source']}"
            await message.answer(text)
    else:
        await message.answer("Hozirda darslar yo'q")
