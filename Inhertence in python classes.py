#INHERITANCE IN PYTHONN CLASSES
#A CHILD CLASS CAN INHERIT THE METHODS AND ATTRIBUTES FROM A PARENT CLASS

class Person():

    name: str  #define dtype
    age: int
    fav_colour: str
    year: int
    human: bool =True #setting dtype and default value

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
    

    

#test

new_person = Person(name= 'Renan Shrestha', age= 6, fav_colour = 'white', year= 2023, human =True)
print(new_person.year_of_birth())

print(new_person.project_age(projection_year= 2045))

person1 = Person(name ='Romish Shrestha', age= 39, fav_colour= 'black-blue', year =2022, human =False)
print(person1.year_of_birth())

print(person1.human)