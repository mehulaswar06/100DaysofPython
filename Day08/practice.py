#Functions with inputs

# def greet(something):
#     print(f"Your lucky number is {1+something}")
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
    
# greet(2)

#greet_wuth_name

# def greet_with_name(name):
#     print("Hello",name)
    
# greet_with_name("Mehul")

#Functions with more than one input

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    
greet_with("Mehul","Akola")

#calling with keyword argument

greet_with(location="Nagpur",name="Mehul")

