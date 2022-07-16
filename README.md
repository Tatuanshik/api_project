О проекте: проект API для социальной сети Yatube. Вы можете создавать посты, комментировать их, подписываться на понравившего вам автора.
Автор проекта: Марковская Татьяна


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Tatuanshik/api_final_yatube.git
```

```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env 
```
для MACOS: `python3 -m venv venv`
```
Далее активируем: source env/bin/activate
```
Для MACOS: `source venv/bin/activate`
```
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
pip install -r requirements.txt
```
pip install djoser
```
Выполнить миграции:
```
cd yatube_api
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
При удачном GET запросе на получение списка публикаций API вернет вам:

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Пример отображения созданного поста:
{
"text": "string",
"image": "string",
"group": 0
}

При некорректной отправке (код ошибки 400), пост не будет опубликован, например:
{
"text": [
"Обязательное поле."
]
}
