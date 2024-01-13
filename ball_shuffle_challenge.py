mylist=[" ","O"," "]
from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess=" "
    while guess not in ["0","1","2"]:
        guess=input("PLEASE GUESS THE  CUP UNDER WHICH BALL MAY PRESENT,EITHER 0,1 OR 2 ")
    guess=int(guess)
    return guess
def check_():
    if shuffled_list[index]=="O":
        print("YAY! YOU GUESSED IT RIGHT")
    else:
        print("BETTER LUCK NEXT TIME")
      
    print(shuffled_list)
#START SHUFFLING
shuffled_list=shuffle_list(mylist)
#GUESSING THE CUP NUMBER
index=player_guess()
#CHECKING AND FINAL RESULT
check_()
