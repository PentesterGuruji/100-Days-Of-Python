# Dictionaries in python

#is a form of table

#key and their respective value

#syntax for dictionaries

#{key:value}

programming_dictionary = {
    "Bug":"An error in a program",
    "Function":"A piece of code that you can easily call over and over again.",
}

##Retreiving items from dictionary

# print(programming_dictionary)


##Adding new items in dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."

## creating an empty dictionary

empty_dictionary = {}

## Wiping an existing Dictionary

#programming_dictionary = {}


## Editing an item in a dictionary

programming_dictionary["Bug"] = "A moth in your computer."

## loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



## Nesting

# In dictionary nesting another dictionary and list into it

# {
#     key: [List],
#     key2:{Dict},
# }


# Nesting a list into dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany": [ "Berlin", "Hamburg" , "Stuttgart"]
}

## You can also nest list into list in dictionary

[ "A", "B", ["C","D"] ]


##Nesting a dictionary in dictionary


travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visit" : 12},
    "Germany": [ "Berlin", "Hamburg" , "Stuttgart"]
}

web_enumeration = {
    "Scanning" : {"nmap" : "http-enum" "http-methods", "total_scripts" : 2}
}

## Nesting a dictionary into list

travel_log = [
    
    {
    "country":"france",
    "cities_visited": ["Paris" , "Litti" , "idk"],"total_visit" :5
    }
]


## python tutor .com good for debugging.....