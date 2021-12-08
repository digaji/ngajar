class Person:
    def __init__(self, name: str, phoneNumber: float, emailAddress: str, age=0) -> None:
        self.name = name
        self.age = age
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress

    def hasParkingPass() -> bool:
        pass

class Address:
    def __init__(self, street, city,  state, postalCode, country) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

    def validate() -> bool:
        pass


class Student(Person):
    def __init__(self, name, age, phoneNumber, emailAddress, studentNumber):
        super().__init__(name, phoneNumber, emailAddress, age)
        self.studentNumber = studentNumber

    def isEligibleToEnroll(self, student) -> bool:
        pass

    def getSeminarHistory(self) -> list:
        pass

    def takeExamination(self) -> None:
        pass


class Professor(Person):
    def __init__(self, name, age ,phoneNumber, emailAddress, listOfStudents, salary):
        super().__init__(name, phoneNumber, emailAddress, age)
        self.listOfStudents = listOfStudents
        self.salary = salary

    def applyExamination(self) -> None:
        pass
