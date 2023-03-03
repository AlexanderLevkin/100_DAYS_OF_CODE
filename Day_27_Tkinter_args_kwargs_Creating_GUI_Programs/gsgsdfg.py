import random
import string
import json
import tkinter as tk


def generate_password(length):
    """
    Генерирует случайный пароль указанной длины.
    """
    # Создаем строку из всех возможных символов, которые могут использоваться в пароле
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем случайный пароль из заданной длины
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def save_password():
    # Запрашиваем у пользователя длину пароля, который он хочет получить
    password_length = int(entry_length.get())

    # Генерируем пароль и сохраняем его в JSON-файле
    password = generate_password(password_length)
    with open('passwords.json', 'w') as f:
        json.dump({'password': password}, f)

    # Выводим сообщение об успешной генерации пароля
    label_message.config(text="Пароль успешно сгенерирован и сохранен в файле passwords.json.")


# Создаем окно приложения
window = tk.Tk()
window.title("Генератор паролей")

# Создаем элементы пользовательского интерфейса
label_title = tk.Label(window, text="Введите длину пароля:")
label_title.pack()

entry_length = tk.Entry(window)
entry_length.pack()

button_generate = tk.Button(window, text="Сгенерировать пароль", command=save_password)
button_generate.pack()

label_message = tk.Label(window, text="")
label_message.pack()

# Запускаем главный цикл приложения
window.mainloop()