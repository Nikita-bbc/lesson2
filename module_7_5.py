import os
import time

for root, dirs, files in os.walk(r'C:\Users\Nikita\PycharmProjects\pythonProject\operative_system'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y.%H:%M", time.localtime(filetime))
        file_size = os.path.getsize(file)
        parent_dir = os.path.basename(root)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}'
            f', Родительская директория: {parent_dir}')
