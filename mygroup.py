def print_students(students):
    a = int(input())
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(45), u"Оценки".ljust(20))
    for student in students:
        if sum(list(map(int, student["marks"])))/len(student["exams"]) >= a:
            print(student["name"].ljust(15), student["surname"].ljust(15), str(student["exams"]).ljust(45), str(student["marks"]).ljust(20))


groupmates = [
    {
        "name":"Александр",
        "surname":"Кузнецов",
        "exams":["ЭВМ","История","Высшая математика"],
        "marks":["5","4","3"]
    },
    {
        "name":"Андрей",
        "surname":"Чекулаев",
        "exams":["АИГ", "АиГ", "Философия"],
        "marks":["4", "4", "4"]
    },
    {
        "name":"Дмитрий",
        "surname":"Пушкин",
        "exams":["ЭВМ","История","Высшая математика"],
        "marks":["3", "2", "4"]
    },
    {
        "name":"Сергей",
        "surname":"Карамушкин",
        "exams":["АИГ", "АиГ", "Философия"],
        "marks":["5", "5", "5"]
    },
    {
        "name":"Артем",
        "surname":"Хорев",
        "exams":["ЭВМ","История","Высшая математика"],
        "marks":["3", "3", "3"]
    },
    {
        "name":"Олег",
        "surname":"Новиков",
        "exams":["АИГ", "АиГ", "Философия"],
        "marks":["3", "5", "5"]
    },
]

print_students(groupmates)