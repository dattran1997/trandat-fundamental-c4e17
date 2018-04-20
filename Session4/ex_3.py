from random import *
words = ['runs', 'experience', 'comments', 'freedom', 'permit']
r_word = choice(words)
character = list(r_word)
count = 1
loop = True
while loop:
    shuffle(character) #ham khong tra ve nen ko duoc gan'
    print(*character,sep=" ")
    guess = input("guess a words: ")
    if (guess == r_word):
        print("congrat my due !")
        option = input("do you want to continue y/n: ")
        if(option == "y"):
            r_word = choice(words)
        elif(option == "n"):
            loop = False
        else:
            print("invalid function !")
    else:
        count = count + 1
        if (count > 3):
            option = input("do you want to continue y/n: ")
            if(option == "y"):
                r_word = choice(words)
            elif(option == "n"):
                loop = False
            else:
                print("invalid function !")
        else:
            print("wrong word")
