# functions with output

# def format_name(f_name,l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

 
# formated_string = format_name("pentESTER","gURUJI")

# print(formated_string)

## More than one return statement

 #returns tells the computer that is end of the function and you should now exit the function.

# def format_name(f_name,l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid input.."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"


# print(format_name(input("what is your first name?"), input("What is your last name?")))


##doc strings

# ##Docstrings are basically a way for us to create little bits of documentation as we coding along in our function. 

 
def format_name(f_name,l_name):
    """Take a first and last name and format it to return the title case version  of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid input.."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("what is your first name?"), input("What is your last name?")))

#2021-08-25-23-13-54.png