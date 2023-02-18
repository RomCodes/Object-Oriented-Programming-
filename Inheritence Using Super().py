import pandas as pd
from datetime import datetime
import datetime as dt

class Person:
    gender = 'Male'

    def __init__(self, f_name: str , l_name : str, gender: str, age: int, country: str) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.age = age
        self.country = country


    def Intro(self):
        return 'My full name is: ' + f"{self.f_name} {self.l_name}"



class PersonDetails(Person):

    #init method of the child class needs to have all required attributes
    def __init__(self, f_name: str , l_name : str, gender: str, age: int, country: str, birth_date, birth_country, immigrated_date, immi_via) ->None:


        #super __init__ method only needs to have the attributes to be inherited from the parent class
        super().__init__(f_name, l_name, gender, age, country)
                
        self.birth_date = birth_date
        self.birth_country = birth_country
        self.immigrated_date = immigrated_date
        self.immi_via = immi_via


    def FullIntro(self):
        return f"My name is : {self.f_name} {self.l_name}.\nHello!\nMy birth day is on the {self.birth_date} which makes me, and I like to be very precise, {pd.to_datetime('today') - pd.to_datetime(self.birth_date)} old !\nI am a {self.gender}\nBorn in a country called {self.birth_country}"
    
    @classmethod #when calling this, the global var gender will replace any variable provided by the user
    def call_class_method(cls):
        return cls.gender





intro = PersonDetails(f_name= 'Romish', l_name= 'Shrestha',  gender='FeMale', age = 39, birth_country= 'Nepal',country= 'Australia', birth_date= 1984, immigrated_date= '2005', immi_via= 'Singapore')

print(intro.FullIntro())

intro_clsmethod = PersonDetails(f_name= 'Romish', l_name= 'Shrestha',  gender='FeMale', age = 39, birth_country= 'Nepal',country= 'Australia', birth_date= 1984, immigrated_date= '2005', immi_via= 'Singapore')
print(intro_clsmethod.call_class_method())