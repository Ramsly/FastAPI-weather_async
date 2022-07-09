# FastAPI. Async getting weather

## Описание

Получение погоды на FastAPI с помощью async/aiohttp. 
[API](https://www.weatherbit.io/api/weather-current) из которого получаю погоду

## Endpoints

**/{city}** - Вместо *city* вписываем название города

## Настройка

Склонируйте проект
```
https://github.com/Ramil2003/FastAPI-weather_async.git
```

Создайте виртуальное окружение

```
python3 -m venv venv
```

Установите зависимости

```
pip install -r req.txt
```

Запустите приложение

```
uvicorn main:app --reload
```
