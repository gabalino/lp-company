"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


def convert_list_to_str(number: int, data: list) -> str:
    list_str = [str(element) for element in data]
    result = f'#{number}\n {"\n ".join(list_str)}'
    return result


def convert_dict_to_str(number: int, data: dict) -> str:
    result = f'#{number}\n '
    result += "\n ".join([f'{key}: {value}' for key, value in data.items()])
    return result


def get_name(data: dict) -> str:
    name = f"{data.get('first_name')} {data.get('last_name')}"
    return name


def get_gender(firstname) -> str:
    result = 'unknown'
    male = ['Daniel', 'Kevin', 'Brian']
    female = ['Michelle', 'Nicole', 'Christina', 'Caitlin']
    if firstname in male:
        result = 'male'
    elif firstname in female:
        result = 'female'
    return result


def get_departments(data: list[dict]) -> list:
    result = []
    for department in data:
        result.append(department.get('title', ''))
    return result


def get_names(data: list) -> list:
    result = []
    for department in data:
        for employer in department.get('employers'):
            result.append(get_name(employer))
    return result


def get_names_department(data: list) -> list:
    result = []
    for department in data:
        for employer in department.get('employers'):
            record = f"{get_name(employer)}: {department.get('title', '')}"
            result.append(record)
    return result


def get_names_salary_more(data: list, salary=0) -> list:
    result = []
    for department in data:
        for employer in department.get('employers'):
            if employer.get('salary_rub', 0) > salary:
                result.append(get_name(employer))
    return result


def get_position_with_salary(data: list, salary: int, param: str) -> list:
    result = []
    for department in data:
        for employer in department.get('employers'):
            if param == 'less':
                if employer.get('salary_rub', 0) < salary:
                    result.append(employer.get('position', ''))
            elif param == 'more':
                if employer.get('salary_rub', 0) > salary:
                    result.append(employer.get('position', ''))
    return list(set(result))


def get_salary_department(data: list) -> dict[str, int]:
    result = {}
    for department in data:
        title = department.get('title', '')
        for employer in department.get('employers'):
            result[title] = result.get(title, 0) + employer.get('salary_rub', 0)
    return result


def get_salary_param(data: list, param: str) -> dict[str, int]:
    result = {}
    for department in data:
        title = department.get('title', '')
        for employer in department.get('employers'):
            employer_salary = employer.get('salary_rub', 0)
            department_salary = result.get(title, 0)
            if department_salary == 0:
                result[title] = employer_salary
            elif param == 'min':
                if employer_salary < department_salary:
                    result[title] = employer_salary
            elif param == 'max':
                if employer_salary > department_salary:
                    result[title] = employer_salary
    return result


def get_salary_avg(data: list, gender: str = '') -> list:
    result = []
    count, total = 0, 0
    for department in data:
        count += len(department)
        for employer in department.get('employers'):
            if not gender:
                total += employer.get('salary_rub', 0)
            elif get_gender(employer['first_name']) == gender:
                total += employer.get('salary_rub', 0)
    result.append(total / count)
    return result


def get_lastname_ends(data: list, letters=''):
    result = []
    for department in data:
        for employer in department.get('employers'):
            if employer['last_name'][-1] in letters:
                result.append(employer['first_name'])
    return list(set(result))


def main():
    print(convert_list_to_str(1, get_departments(departments)))
    print(convert_list_to_str(2, get_names(departments)))
    print(convert_list_to_str(3, get_names_department(departments)))
    print(convert_list_to_str(4, get_names_salary_more(departments, 100000)))
    print(convert_list_to_str(5, get_position_with_salary(departments, 80000, 'less')))
    print(convert_dict_to_str(6, get_salary_department(departments)))
    print(convert_dict_to_str(7, get_salary_param(departments, 'min')))
    # print(convert_dict_to_str(8, get_salary_param(departments, 'all')))
    print(convert_list_to_str(9, get_salary_avg(departments)))
    print(convert_list_to_str(10, get_position_with_salary(departments, 90000, 'more')))
    print(convert_list_to_str(11, get_salary_avg(departments, gender='female')))
    print(convert_list_to_str(12, get_lastname_ends(departments, letters='aeiouy')))


if __name__ == '__main__':
    main()
