from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name:str, yob:int):
        self._name = name 
        self._yob = yob 

    def getYoB(self):
        return self._yob 
    
    @abstractmethod
    def describe(self):
        pass 


class Student(Person):
    def __init__(self, name:str, yob:int, grade:str):
        super().__init__(name=name, yob=yob)
        self._grade = grade 
    
    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Teacher(Person):
    def __init__(self, name:str, yob:int, subject:str):
        super().__init__(name=name, yob=yob)
        self.__subject = subject 

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")

class Doctor(Person):
    def __init__(self, name:str, yob:int, specialist:str):
        super().__init__(name=name, yob=yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")



class Ward: 
    def __init__(self, name:str):
        self.__name = name 
        self._list_people = list()

    def add_person(self, person:Person):
        self._list_people.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self._list_people:
            p.describe()

    def count_doctor(self):
        counter = 0 
        for p in self._list_people:
            if isinstance(p, Doctor):
                counter += 1 
    
        return counter
    
    
    def sort_age(self):
        self._list_people.sort(key=lambda x : x.getYoB(), reverse=True)

    def ave_teacher_yob(self):
        counter = 0 
        total_year = 0 
        for p in self.__listPeople:
            if isinstance(p, Teacher):
                counter += 1 
                total_year += p.getYoB()
        return total_year/counter 
    


    
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()






