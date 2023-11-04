### Для запуска теста
- Импортировать unittest
- Написать класс TestFitTransform(unittest.TestCase) с функциями для тестов
- Выполнить в терминале:\
 python -m unittest .\Homework5\Issue3\one_hot_encoder.py

### DoD
1. Метод проверки assertEqual\
self.assertEqual(actual, expected)
2. Метод проверки assertNotIn\
self.assertNotIn(not_expected, actual)
3. Метод проверки assertIsInstance\
self.assertIsInstance(actual, list)
4. Метод проверки assertRaises\
self.assertRaises(TypeError, fit_transform)