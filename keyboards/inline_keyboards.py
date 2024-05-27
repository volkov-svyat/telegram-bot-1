from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_inline_cat():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton("Посмотреть", url="https://www.purina.ru/cats/breed-library")
    # but_inline2 = InlineKeyboardButton("Посмотреть", url="https://www.purina.ru/cats/breed-library")
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_inline_dog():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=1)
    but_inline1_2 = InlineKeyboardButton("Посмотреть", url="https://www.lapkins.ru/dog/")
    keyboard_inline_2.add(but_inline1_2)
    return keyboard_inline_2