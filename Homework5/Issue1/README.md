### Issue-01
Для запуска тестов:
Выполнить команду в терминале:\
python -m doctest -o ELLIPSIS -v .\Homework5\Issue1\morse.py

#### DoD:
1. Директива\
\# doctest: +NORMALIZE_WHITESPACE\
Тест игнорирует лишние пробелы
2. Флаг\
-o ELLIPSIS - использование ...
3. Исклечение (Exception)\
Если на вход программе будут поданы строчные буквы, то код выведет ошибку: KeyError\
Проигнорировать её в тесте можно с помощью исклечения следующего вида:\
    \>>> encode('lowercase')\
    Traceback (most recent call last):\
        ...\
    KeyError: ...