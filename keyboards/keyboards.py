from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Отправь фото кота')
    button_2 = KeyboardButton('Перейти на следущую клавиатуру')
    keyboard.add(button_1, button_2)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1_2 = KeyboardButton('Отправь фото собаки')
    button_2_2 = KeyboardButton('Вернуться на 1 клаиватуру')
    keyboard_2.add(button_1_2, button_2_2)
    return keyboard_2