
print("Love Calculator")

name1 = input("What's your name? ")
name2 = input("Whats's your partner name? ")
####### using lower function to combine the output in lower chars  to use this add .lower() in the end of the string

### how to use f strings in variable
## f""

# stringname.count("word") is the function used to get occurance of the word

combine = (name1 + name2).lower()

chk_true = combine.count("t") + combine.count("r") + combine.count("u") + combine.count("e")

chk_love = combine.count("l") + combine.count("o") + combine.count("v") + combine.count("e")

## print(chk_true)
## print(chk_love)
##print(type(chk_love))


# score = f"{chk_true}{chk_love}"
# score = int(score)

########### another way of concatinate integers and then converting them back to interger

score = int(f"{chk_true}{chk_love}")
# score = int(str(chk_true) + str(chk_love))



if (score <10) or (score >90):
    print(f'Your score is {score}, you go together like coke and mentos.')

elif (score>40) and (score<50):
    print(f'Your score is {score}, you are alright together.')

else:
    print(f'Your score is {score}')


