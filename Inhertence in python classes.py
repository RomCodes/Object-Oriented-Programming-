#INHERITANCE IN PYTHONN CLASSES
#A CHILD CLASS CAN INHERIT THE METHODS AND ATTRIBUTES FROM A PARENT CLASS

#Parent Class
class Person():

    name: str  #define dtype
    age: int
    fav_colour: str
    year: int
    human: bool =True #setting dtype and default value so even if the attributes are set to false it wil alwys default to True

    def __init__(self, name, age, fav_colour, year, human):
        self.name =name
        self.age =age
        self.fav_colour = fav_colour
        self.year = year
        self.human = human



#method to calc year of birth
    def year_of_birth(self) ->int:
        return 2023-self.age
    
#method to calc projected age

    def project_age(self, projection_year) -> int:
        return (projection_year -self.year) + self.age
    


#child class Student inherits the attributes of the parent class using the super() init function
class Student(Person):
    def __init__(self, name, age, fav_colour, year, human, student_no):
        super().__init__(name, age, fav_colour, year, human)

        self.student_no = student_no
        
    def student_2(self):

        return self.student_no*2

    

    

#test

new_person = Person(name= 'Renan Shrestha', age= 6, fav_colour = 'white', year= 2023, human =True)
print(new_person.year_of_birth())

print(new_person.project_age(projection_year= 2045))

person1 = Person(name ='Romish Shrestha', age= 39, fav_colour= 'black-blue', year =2022, human =False)
print(person1.year_of_birth())

print(person1.human)

check_student = Student(name = 'Shraey Shrestha', age = 5, fav_colour= 'Green',year = 2019, human = False, student_no= 333)
check_child_class = check_student.student_2()
print(check_child_class)
print(Student.human)