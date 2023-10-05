from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Online darslar"),
        ],
        [
            KeyboardButton(text="✍️ Xabar yozish"),
        ]
        
        ],
    resize_keyboard=True, input_field_placeholder="Menu")

def get_book_category_btn(books_category):

    books_category_btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, input_field_placeholder="Bo'limlardan birini tanlang")
    
    for i in books_category:
        books_category_btn.insert(KeyboardButton(text=f"{i['name']}"))
        
    books_category_btn.add(KeyboardButton(text=f"🔙 Ortga"))
    
    return books_category_btn
