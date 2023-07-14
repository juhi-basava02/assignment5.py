# implement the complete student class

class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

student = Student()


student.setName("John Doe")
student.setRollNumber(12345)


name = student.getName()
rollNumber = student.getRollNumber()

print(f"Name: {name}")
print(f"Roll Number: {rollNumber}")