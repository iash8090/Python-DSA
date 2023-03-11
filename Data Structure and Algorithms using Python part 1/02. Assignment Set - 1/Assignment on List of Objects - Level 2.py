
class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

#Implement Service class here
class Service:
    def __init__(self,car_list):
        self.__car_list=car_list

    def get_car_list(self):
        return self.__car_list

    def find_cars_by_year(self,year):
        model_list=[]
        for c in self.__car_list:
            if year == int(c.get_year()):
                model_list.append(c.get_model())
        if(len(model_list)==0):
            return None
        return model_list

    def add_cars(self,new_car_list):
#        self.__car_list += new_car_list          # Method 1
        self.__car_list.extend(new_car_list)      # Method 2
        self.__car_list.sort(key=lambda x: x.get_year())

    def remove_cars_from_karnataka(self):
        temp=self.__car_list.copy()
        for c in temp:
           if c.get_registration_number()[0:2] == "KA":
              self.__car_list.remove(c)

'''    def show_cars(self, car_list):
       for c in self.__car_list:
           print(c)
'''


car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
car6=Car("i10",2012,"JA09 3648")
car7=Car("jaguar",2009,"KA05 9876")
new_car_list=[car6,car7]

#Create object of Service class, invoke the methods and test your program
ser=Service(car_list)
print(ser.find_cars_by_year(2013))
ser.add_cars(new_car_list)  # Calling Method to add new cars
#ser.show_cars(car_list)     # Showing updated Car List
print(ser.find_cars_by_year(2012))
ser.remove_cars_from_karnataka()
#ser.show_cars(car_list)     # Showing updated Car List
