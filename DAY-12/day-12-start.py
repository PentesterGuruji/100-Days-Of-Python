################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# ## Local scope

# def drink_portion():
#     portion_strenth = 2
#     print(portion_strenth)

# drink_portion()
# print(portion_strength)


# # global scope

# player_health = 10

# def drink_portion():
#     portion_strenth = 2
#     print(player_health)

# drink_portion()

## There is no block scope 

# game_level = 3

# enemies = [ "hi", "bye"]

# if game_level < 5:
#     new_enemy = enumerate[0]

# print(new_enemy)

## if variable is creating in function .. it will only be accessible in that function


############### Modifying global variable


# it's not recommended to change global variable in function
## it will create un necesary problems and bug instead use return
# guruji = 0

# def test():
#     global guruji
#     guruji += 1
#     print(guruji)

# test()

# guruji = 0

# def test():
#     print("hi")
#     return guruji + 1


# guruji = test()

# print(guruji)


#### Global constant

PI = 3.45
URL = "https://guruji.com"

def calc():
    print(PI)

calc()