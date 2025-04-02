# Python Problems Archive

Репозиторий с коллекцией задач по программированию на Python.

## Быстрая настройка

Для быстрой настройки проекта выполните следующую команду:

```bash
curl -s https://raw.githubusercontent.com/SlNPacifist/python-problems-archive/main/setup.sh | bash
```

Эта команда:
1. Скачает скрипт настройки
2. Клонирует репозиторий
3. Создаст виртуальное окружение
4. Установит все необходимые зависимости

## Ручная настройка

Если вы предпочитаете выполнить настройку вручную:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SlNPacifist/python-problems-archive.git
   cd python-problems-archive
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # для Linux/macOS
   # или
   venv\Scripts\activate  # для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск программы

После настройки вы можете запустить программу:

```bash
python problem1.py
``` 