class Student():
    sum = 0
    # name = 'lzh'
    # age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0
        print(self.name, age)
        # print('student')
    def grade(self, score):
        if score < 0:
            print('Error!')
        else:
            self.__score = score
 
student1 = Student('jerome', 18)
student1.__score = -1
print(student1.__score)
student1.__score = 100
print(student1.__score)
student1.grade(-2)
print(student1.__score)