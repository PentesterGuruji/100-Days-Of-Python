# ######use link to search for python modules  https://askpython.com

######https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
import random
# #####we can import different python file just like that  import guruji.py ( in the same dir)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() # different float number between 0 and 1

print(random_float)

#####generating random float numbers between 1 and 5

random_float1 = random.uniform(1, 5) # through ask.python
random_float2 = random.random()*5
print(random_float1)
print(random_float2)


### seed is some random numbers ( ex time, keystorkes), this will help to generate more complex numbers.

## illegal application of psedo random numbers to crack a lottery 
#https://www.nytimes.com/interactive/2018/05/03/magazine/money-issue-iowa-lottery-fraud-mystery.html?action=click&module=MagazineModule&pgtype=Article&contentCollection=Magazine&region=Header&mtrref=www.nytimes.com&gwh=B16E6A9DDBACCBA7B56D46F6D80DE2FA&gwt=pay&assetType=PAYWALL

##### random module uses computer current time as a seed default  to change that 

random.seed(123)

# ##same seed same random number
# ###different seed different random number


########### python lists

### you can store any data types in lists
### more items in one variable
### order can be maintained
# ##syntax is []

# ##fruits = ["Cheery" , "Apple"]

states_of_america = ["Delaware", "NewYork", "bla"]

# order 1

print(states_of_america[0])

## or we could save in another variable
## ex --> state = states_of_america[1]

### changing lists

states_of_america[2] = "Blabla"
print(states_of_america)

## add a item at a end of the list

states_of_america.append("Guruji")
print(states_of_america)

#### more things to do https://docs.python.org/3/tutorial/datastructures.html

states_of_america.extend(["wow" , "bete" , "moz", "kardi"])

print(states_of_america)


#### when we want length we must subtract 1 from it .. coz len starts from 1 ,, and indexing value starts from 0

################################
# example new 

mix = [ "strawberies" , "potato", "mango" , "onion", "cabbage", "watermelon"]

### now how do we separate fruits and vegetables from it 

## 1 way is make two lists named fruits and vegetables .

## 2 way  list ke andar list is called nested list

fruits = [ "mango"]
vegetables = ["onion"]

mix = [ fruits, vegetables]
# this is how you can insert one list into another
