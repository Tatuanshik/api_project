О проекте: проект API для социальной сети Yatube. Вы можете создавать посты, комментировать их, подписываться на понравившего вам автора.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:api_final_yatube.git
```

```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env 
```
для MACOS: python3 -m venv venv 
```
Далее активируем: source env/bin/activate
```
Для MACOS: source venv/bin/activate
```
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
