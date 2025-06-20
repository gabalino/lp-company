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


def list2str(number: int, data: list) -> str:
    list_str = [str(element) for element in data]
    result = f'#{number}\n {"\n ".join(list_str)}'
    return result


def dict2str(number: int, data: dict) -> str:
    result = f'#{number}\n '
    result += "\n ".join([f'{key}: {value}' for key, value in data.items()])
    return result


def get_name(data: dict) -> str:
    name = ''
    if 'first_name' in data and 'last_name' in data:
        name = f"{data['first_name']} {data['last_name']}"
    return name


def get_position(data: dict) -> str:
    position = ''
    if 'position' in data:
        position = data['position']
    return position


def get_salary(data: dict) -> int:
    salary = 0
    if 'salary_rub' in data:
        salary = data['salary_rub']
    return salary


def get_gender(firstname) -> str:
    result = 'unknown'
    male = ['Daniel', 'Kevin', 'Brian']
    female = ['Michelle', 'Nicole', 'Christina', 'Caitlin']
    # Мишель, Николь, Кристина и Кейтлин
    if firstname in male:
        result = 'male'
    elif firstname in female:
        result = 'female'
    return result


def get_departments(data: list[dict]) -> list:
    result = []
    for department in data:
        if 'title' in department:
            result.append(department['title'])
    return result


def get_names(data: list) -> list:
    result = []
    for department in data:
        if 'employers' in department:
            for employer in department['employers']:
                result.append(get_name(employer))
    return result


def get_names_department(data: list) -> list:
    result = []
    for department in data:
        if 'title' in department and 'employers' in department:
            for employer in department['employers']:
                record = f"{get_name(employer)}: {department['title']}"
                result.append(record)
    return result


def get_names_salary_more(data: list, salary=0) -> list:
    result = []
    for department in data:
        if 'employers' in department:
            for employer in department['employers']:
                if get_salary(employer) > salary:
                    result.append(get_name(employer))
    return result


def get_position_with_salary(data: list, salary: int, param: str) -> list:
    result = []
    for department in data:
        if 'employers' in department:
            for employer in department['employers']:
                if param == 'less':
                    if get_salary(employer) < salary:
                        result.append(get_position(employer))
                elif param == 'more':
                    if get_salary(employer) > salary:
                        result.append(get_position(employer))
    return list(set(result))


def get_salary_department(data: list) -> dict[str, int]:
    result = {}
    title = ''
    for department in data:
        if 'title' in department:
            title = department['title']
        if title and 'employers' in department:
            for employer in department['employers']:
                result[title] = result.get(title, 0) + get_salary(employer)
    return result


def get_salary_param(data: list, param: str) -> dict[str, int]:
    result = {}
    for department in data:
        title = ''
        if 'title' in department:
            title = department['title']
        if title and 'employers' in department:
            for employer in department['employers']:
                employer_salary = get_salary(employer)
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
        if 'employers' in department:
            for employer in department['employers']:
                if not gender:
                    total += get_salary(employer)
                elif get_gender(employer['first_name']) == gender:
                    total += get_salary(employer)
    result.append(total / count)
    return result


def get_lastname_ends(data: list, letters=''):
    result = []
    for department in data:
        if 'employers' in department:
            for employer in department['employers']:
                if employer['last_name'][-1] in letters:
                    result.append(employer['first_name'])
    return list(set(result))


def main():
    print(list2str(1, get_departments(departments)))
    print(list2str(2, get_names(departments)))
    print(list2str(3, get_names_department(departments)))
    print(list2str(4, get_names_salary_more(departments, 100000)))
    print(list2str(5, get_position_with_salary(departments, 80000, 'less')))
    print(dict2str(6, get_salary_department(departments)))
    print(dict2str(7, get_salary_param(departments, 'min')))
    # print(dict2str(8, get_salary_param(departments, 'all')))
    print(list2str(9, get_salary_avg(departments)))
    print(list2str(10, get_position_with_salary(departments, 90000, 'more')))
    print(list2str(11, get_salary_avg(departments, gender='female')))
    print(list2str(12, get_lastname_ends(departments, letters='aeiouy')))


# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.


if __name__ == '__main__':
    main()
