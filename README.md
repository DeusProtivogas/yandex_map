# yandex_map

## Цель
Проект для визуализации информации про различные места в Москве

## Установка
* Скопировать к себе репозиторий

* Проект использует `python` версии `3.9`

* Создать и активировать виртуальное окружение

```
python3 -m venv env

source env/bin/activate
```

* Удостовериться, что установлена последняя версия pip — программы, которую мы используем для установки Django.

```
python -m pip install --upgrade pip
```

* Установить зависимости

```
pip install -r requirements.txt
```

* Создать в корне файл ``.env``

* Разместить в нем: 

```
SECRET_KEY='DJANGO_KEY'
DEBUG=False
```
, где:

SECRET_KEY - Секретный ключ для установки Django; используется для обеспечения криптографической подписи и 
должен быть установлен на уникальное, непредсказуемое значение;

DEBUG - указание, заупскать или нет сервер в режиме отладки (значение по умолчанию - False)

* Применить миграции базы данных

```
python manage.py migrate
```

Как пользоваться:

* Запуск локального сервера:
```
python manage.py runserver
```

[Ссылка на сайт](https://deusprotivogas.pythonanywhere.com/)





