
"""
 A university has a Person class with a method introduce ( ) that prints "i am a person. "
A subclass student overrides this method to print "1 am a student. " Write the Python
code demonstrating this behavior.
"""

class Person:
    def introduce(self):
        print("i am person")
        
class Student(Person):
    def introduce(self):
        print("i am student")
        

person= Person()
student = Student()

person.introduce()
student.introduce()               