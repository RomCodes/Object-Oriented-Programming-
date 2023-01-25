#INHERITANCE IN PYTHONN CLASSES
#A CHILD CLASS CAN INHERIT THE METHODS AND ATTRIBUTES FROM A PARENT CLASS

class Person():
    def __init__(self, name, age, colour, year):
        self.name =name
        self.age =age
        self.colour = colour
        self.year = year

#method to calc year of birth
    def year_of_birth(self):
        return 2023-self.age
    
#method to calc projected age

    def project_age(self, projection_year):
        return (projection_year -self.year) + self.age



new_person = Person(name= 'Renan Shrestha', age= 6, colour = 'white', year= 2023)
print(new_person.year_of_birth())

print(new_person.project_age(projection_year= 2045))
