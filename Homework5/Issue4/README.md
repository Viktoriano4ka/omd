### Для запуска теста
- Установить pytest:\
pip install -U pytes
- Импортировать pytest
- Написать функции для тестов
- Выполнить в терминале:\
python -m pytest .\Homework5\Issue4\one_hot_encoder.py

### DoD
1. Проверка assertEqual\
assert actual == expected
2. Проверка assertNotIn\
assert not_expected not in actual
3. Проверка assertIsInstance\
assert isinstance(actual, list)
4. Проверка assertRaises\
    with pytest.raises(TypeError):\
        fit_transform()