# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, members=[], classes=[], subjects=[]):
        self.members = list(members)
        self.classes = list(classes)
        self.subjects = list(subjects)

    def addMember(self, person):
        self.members.append(person)

    def addClass(self, *args):
        self.classes.append(*args)

    def addSubject(self, subj_name):
        self.subjects.append(subj_name)

    def showAllClasses(self):
        for cl in self.classes:
            print (cl)

    def showAllMembers(self):
        for member in self.members:
            print(member)

    def __str__(self):
        return '[Subjects: {}, Classes: {}, Members: {}]'.\
            format(self.subjects, self.classes, self.members)

class SchoolClass:
    def __init__(self, class_name, subjects=[], teachers=[], students=[]):
        self.class_name=class_name
        self.subjects=list(subjects)
        self.teachers=list(teachers)
        self.students=list(students)

    def addStudent(self, student):
        self.students.append(student)

    def studentsList(self):
        for student in self.students:
            print(student)

    def __str__(self):
        return '[Class: {}, subjects: {}, teachers: {}, students: {}]'.\
            format(self.class_name, self.subjects, self.teachers, self.students)

class Subject:
    def __init__(self, subj_name):
        self.subj_name = subj_name

class Person:
    def __init__(self, name, surname, job=None):
        self.name = name
        self.surname = surname
        self.job = job

    def __str__(self):
        return '[Person: {}, {}]'.format(self.name, self.job)

class Teacher(Person):
    def __init__(self, name, surname, teach_classes):
        Person.__init__(self, name, 'teacher')
        self.teach_classes = teach_classes

    # def convert_class(self, class_room):
    #     return {'class_num': int(class_room.split()[0]),
    #             'class_char': class_room.split()[1]}

    def __str__(self):
        return str(self.person)

class Student(Person):
    def __init__(self, name, surname, class_room):
        Person.__init__(self, name, surname)
        self._class_room = {'class_num': int(class_room.split()[0]),
                           'class_char': class_room.split()[1]}

class Parent(Person):
    pass

if __name__ == '__main__':
    sch1 = School()
    class1A = SchoolClass('5 A')
    class1B = SchoolClass('5 B')
    sch1.addClass(class1A)
    sch1.addClass(class1B)
    bob = Teacher('Bob', 'Daniels', '5 A')
    sch1.addMember(bob)
    popov = Student('Анатолий', 'Попов', '5 A')
    sch1.addMember(popov)
    print(sch1.showAllClasses())