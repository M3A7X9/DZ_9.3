import tkinter as tk
from tkinter import messagebox as mb
import webbrowser
import requests


def get_city_info():
    global lat, lng
    city_name = entry.get()
    if not city_name:
        mb.showerror("Ошибка!", "Введите название города...")
        return

    api_key = '1828e03833594c74ae77282ddae5ff1c'
    url = f'https://api.opencagedata.com/geocode/v1/json?q={city_name}&key={api_key}'

    try:
        response = requests.get(url)
        data = response.json()

        if data['results']:
            result = data['results'][0]
            lat = result['geometry']['lat']
            lng = result['geometry']['lng']
            currency_name = result['annotations']['currency']['name']
            country = result['components']['country']
            region = result['components'].get('state', 'Неизвестно')

            result_label.config(text=f"Координаты: {lat}, {lng}\nВалюта: {currency_name}\nСтрана: {country}\nРегион: {region}")
        else:
            mb.showerror("Ошибка!!!", "Город не найден")
    except Exception as e:
        mb.showerror("Ошибка!!!", f"Произошла ошибка: {e}")


def del_button():               # Функция кнопки для очистки результатов поиска и поля ввода
    entry.delete(0, tk.END)
    result_label.config(text="")

def show_map():
    if 'lat' in globals() and 'lng' in globals():
        map_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}"
        webbrowser.open(map_url)
    else:
        mb.showerror("Ошибка", "Сначала введите поиск города")

window = tk.Tk()
window.title("Координаты города")
window.geometry("400x300")

entry = tk.Entry()
entry.pack(pady=10)

search_button = tk.Button(text="Поиск", command=get_city_info)
search_button.pack(pady=10)

clear_button = tk.Button(text="Очистить", command=del_button)
clear_button.pack(pady=10)

map_button = tk.Button(text="Показать на карте", command=show_map)
map_button.pack(pady=10)

result_label = tk.Label(text="")
result_label.pack(pady=10)

window.mainloop()