class Person:
    def __init__(self, name , last_name , age , gender, student: bool, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__password = password
    
    def Greeting(self, second_person):
        print("Welcome dear", second_person.name)
    
    def Goodbye(self):
        print("Bye everyone!")
    
    def Favourite_num(self, num1:int):
        return ("My favourite number is: " + str(num1))
    
    def Read_file(self, filename):
        f = open((filename + ".txt"), "r")
        print(f.read())
        
    def Set_password(self, new_password):
        self.__password = new_password
    
    def Get_password(self):
        return self.__password

person_1 = Person("Poxos", "Poxosyan", "20", "M", True, "poxospoxosyan20")
person_2 = Person("Petros", "Petrosyan", "50", "M", False, "petrospetrosyan50")
person_1.Greeting(person_2)
person_2.Goodbye()
person_1.Favourite_num(7)
person_1.Read_file("txt_file")
person_1.Get_password()
person_1.Set_password("maybe")