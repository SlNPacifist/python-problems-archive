#!/bin/bash

# Клонирование репозитория
git clone https://github.com/SlNPacifist/python-problems-archive.git

# Переход в директорию проекта
cd python-problems-archive

# Создание виртуального окружения
python3 -m venv venv

# Активация виртуального окружения (для bash)
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Вывод сообщения об успешном завершении
echo "Настройка успешно завершена!"
echo "Для активации виртуального окружения в будущем используйте:"
echo "cd python-problems-archive"
echo "source venv/bin/activate" 