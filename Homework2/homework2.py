import csv
import re


def get_data_from_csv(name_file: str) -> list:
    """Get data from csv file."""
    df = list()
    with open(name_file, newline='', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            df.append(row)
    df = df[1:]
    return df


def get_department_structure(source_rows: list) -> dict:
    """Get department structure."""
    output = dict()
    for i in set([el[1] for el in source_rows]):
        output[i] = set([el[2] for el in source_rows if el[1] == i])
    return output


def get_department_report(source_rows: list) -> dict:
    """Get department report."""
    output = dict()
    for i in set([el[1] for el in source_rows]):
        department_data = list()
        headcount = [el[0] for el in source_rows if el[1] == i]
        salary = [int(el[5]) for el in source_rows if el[1] == i]
        department_data.append(f'численность департамента - {len(headcount)}')
        department_data.append(f'зарплата от {min(salary)} руб.')
        department_data.append(f'зарплата до {max(salary)} руб.')
        department_data.append(f'средняя зарплата {int(sum(salary)/len(salary))} руб.')
        output[i] = department_data
    return output


def print_fancy_dict(source_dict: dict) -> None:
    """Print dictionary in the appropriate form."""
    for i in source_dict.keys():
        print(f'- {i}')
        for j in source_dict[i]:
            print(f'  - {j}')
    return


def save_department_report(source_dict: dict) -> None:
    """Save department report into csv file."""
    re_digits = re.compile(r"\b\d+\b")
    with open('Department_Report.csv', 'w', newline='', encoding="utf8") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';')
        filewriter.writerow(['Department', 'Number_of_employees', 'Min_salary', 'Max_salary', 'Avg_salary'])
        for i in source_dict.keys():
            data_list = list()
            data_list.append(i)
            for j in source_dict[i]:
                data_list.append(*re_digits.findall(j))
            filewriter.writerow(data_list)
    return


if __name__ == '__main__':
    print("""Что необходимо сделать: 
1. Вывести иерархию команд;
2. Вывести сводный отчёт по департаментам;
3. Сохранить сводный отчёт в виде csv-файла.""")
    answer = input()
    source_file = get_data_from_csv('Corp_Summary.csv')
    if answer == '1':
        print('Иерархия команд:')
        structure_dict = get_department_structure(source_file)
        print_fancy_dict(structure_dict)
    elif answer == '2':
        print('Сводный отчёт по департаментам:')
        report_dict = get_department_report(source_file)
        print_fancy_dict(report_dict)
    elif answer == '3':
        print("""Сохранение сводного отчёта по департаментам...
Сохранено""")
        report_dict = get_department_report(source_file)
        save_department_report(report_dict)
