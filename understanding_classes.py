class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

    def add_n_to_age(self, n):
        self.age = self.age + n

    def new_func(self, n):
        self.age = self.age + n**2 + n
        

def main():
    student_1 = Student("Isika Ram", 22) # student_1 is an object
    student_2 = Student("Anubhab Chakraborty", 35) # student 2 is also an object

    
    student_1.new_func(10)
    print(student_1.age)


if __name__ == '__main__':
    main()