# avito_test_mi
Тестовое задание в юнит Market Intelligence

Run

````
$ docker-compose up -d --build
````

#### API
```
/add - возвращает id пары (запрос, регион)
{
    "text" : string, - текст запроса
    "region": string - locationId
}

/stat - возвращает счетчики и время получение счетчки в интервале (start, end)
{
    "id" : int, - id пары запроса
    "start" : int, - начало интервала
    "end" : int - конец интервала
}
```

docs: http://127.0.0.1:8000/docs#/