# social_network

Запуск проекта:
1. Настройка виртуальноего окружения
```shell
python -m venv venv
```
2. Активация окружения:
```shell
venv\Scripts\activate.bat - для Windows
source venv/bin/activate - для Linux и MacOS
```
3. Установить все зависимости
```shell
pip install -r requirements.txt
```
4. Запустить проект из директории social_network
```shell
uvicorn src.main:app --reload
```