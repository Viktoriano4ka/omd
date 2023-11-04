- Для запуска тестов - выполнить в терминале:
~~~
python -m pytest -q .\Homework5\Issue5\what_is_year_now.py --cov
~~~
- Для формирования отчета - выполнить в терминале:
~~~
python -m pytest -q .\Homework5\Issue5\what_is_year_now.py --cov --cov-report=html:homework5\issue5\reports\html
~~~
- Отчет формируется в reports\html\index.html