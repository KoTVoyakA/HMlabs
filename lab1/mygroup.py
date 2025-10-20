groupmates = [
    {
        "name": "Александр",
        "surname": "Котов",
        "exams": ["Информатика", "C++", "Web"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Иван",
        "surname": "Смирнов",
        "exams": ["История", "РиПН", "ДГП"],
        "marks": [4, 5, 3]
    },
    {
        "name": "Дмитрий",
        "surname": "Бобров",
        "exams": ["ГКА", "КПТС", "Астрономия"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Анастасия",
        "surname": "Медведева",  # исправлено supername → surname
        "exams": ["Русский язык", "Безопасность жизнедеятельности", "Психология"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Алиса",
        "surname": "Кудрявцева",  # исправлено supername → surname
        "exams": ["Физика", "ОСБ", "ПиТА"],
        "marks": [4, 4, 4]
    }
]


def print_students(groupmates):
    print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(50), "Оценки".ljust(20))
    print("-" * 100)
    for student in groupmates:
        print(student["name"].ljust(15),
              student["surname"].ljust(15),
              str(student["exams"]).ljust(50),
              str(student["marks"]).ljust(20))


print_students(groupmates)