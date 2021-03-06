def print_students(students, sr_ball):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        sr_oc = float(sum(student["marks"]) / len(student["marks"]))
        if sr_oc > sr_ball:
            print(student["name"].ljust(15), student["surname"].ljust(10),
                str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


groupmates = [
    {
        "name": "Матвей",
        "surname": "Еременков",
        "exams": ["Философия", "АиГ", "ВМ"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Иван",
        "surname": "Михайлов",
        "exams": ["Философия", "АиГ", "ВМ"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Лев",
        "surname": "Петров",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 5, 5]
    },
    {	
        "name": "Никита",
        "surname": "Корнеев",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Артемий",
        "surname": "Пробатов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 3, 3]
    }
]

sr = float(input("Средний балл: "))
print_students(groupmates, sr)
