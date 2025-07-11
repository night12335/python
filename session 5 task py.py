#Defining a Class

class Car:
    brand = "Toyota"  # Attribute
    def start(self):  # Method
        print("The car has started.")
#Creating an Object

my_car = Car()  # Create an object from the Car class
print(my_car.brand)  # Access the attribute: Output -> Toyota
my_car.start()  # Call the method: Output -> The car has started.
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Assign values to attributes
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} has started.")

# Create an object with specific values
my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # Output -> Toyota
print(my_car.model)  # Output -> Corolla
my_car.start()  # Output -> Toyota Corolla has started.

#class we named employee

class employee :
    def __init__(self , name , age , department , is_manager):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager


# object we created
  #from employee import employee


employee1 = employee("omar" , 21 , "cs" , True)
employee2 = employee("ahmed" , 20 , "is" , False)

print(employee1.age , employee2.is_manager)
# class

class employee :
    def __init__(self , name , age , department , is_manager , rating):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
        self.rating = rating

    def is_excellent(self):
            if self.rating >= 5 :
                return True
            else :
                return False

# objects

#afrom employee import employee

employee1 = employee("omar" , 21 , "cs" , True , 5)
employee2 = employee("ahmed" , 20 , "is" , False , 4.5)

print( employee1.is_excellent())
print( employee2.is_excellent())
# Syntax for Inheritance
