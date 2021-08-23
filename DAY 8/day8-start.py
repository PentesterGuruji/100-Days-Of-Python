
### Create a function called greet()
# ###write 3 print statements inside the function.
### Call the greet() function and run the code

##Function with input

# def greet():
#     print("Hello")
#     print("Welcome, we're glad you are here")
#     print("Chillx")


# greet()

##Function with input

# def greet_name(name):
#     print(f"Hello {name}")
#     print(f"How you do {name} ?")


# greet_name("Pentester Guruji")

# parameter is the name of the data that's being passed in

# argument is the actual value of the data

# example :- in function greet_name (name) that name is parameter
# and we specify pentester guruji as a argument


###Function with more than one input

# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"Glad to have you on board from {location}")
 


# greet_with("PentesterGuruji","INDIA")


###POSITIONAL ARGUMENTS


## keyword arguments


# my_function(a=1, b=2, c=3)

# if we here changed the position if doesn't matter 



def greet_with(name,location):
    print(f"Hello {name}")
    print(f"Glad to have you on board from {location}")
 


greet_with(location= "Delhi", name = "Pentesterguruji")