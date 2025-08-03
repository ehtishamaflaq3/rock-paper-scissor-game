import random
# -------------------------------------SIMPLE LOGIC FOR ONE GAME----------------------------
#1.User Input Function:-
#   Ask the user to type Rock, Paper, or Scissors
#   Make sure the input is valid
def play():
    def inpfunc():
        print("Enter The Rock,Paper,Scissor:- ")
        choice=input("You Choose:- ").lower()
        while choice not in ["rock","paper","scissor"]:
            choice=input("INVALID!! PLEASE AGAIN CHECK IT ").lower()
        return choice
#2.Computer Choice Function:-
#   Use random module to choose Rock, Paper, or Scissors for the computer
    def comfunc():
        return random.choice(["rock","paper","scissor"])
#3.Winner Logic:-
#   Use if-elif-else to decide who wins
    def winnerlogic(user,comp):
        if user == comp:
            return("it's Tie")
        elif (user=="rock" and comp=="scissor") or\
            (user=="paper" and comp=="rock") or \
            (user =="scissor" and comp=="paper"):
            return("YOU WIN")
        else:
            return("COMPUTER WINS")
#4.Main Game Loop:-
#   Let the player play multiple rounds
# Ask: “Play again? (yes/no)”
    while True:
        user=inpfunc()
        comp=comfunc()
        print(f"YOU ENTER {user}")
        print(f"COMPUTER CHOICE {comp}")
        print(winnerlogic(user,comp))
        again=input("YOU PLAY AGAIN(Y/N):- ")
        if again!= "Y":
            print("THANKS FOR PLAYING")
            break
# ------------------------------------TOURNAMENT------------------------------------------
def tournament():
    def inpfunc():
        print("Enter The Rock,Paper,Scissor:- ")
        choice=input("You Choose:- ").lower()
        while choice not in ["rock","paper","scissor"]:
            choice=input("INVALID!! PLEASE AGAIN CHECK IT ").lower()
        return choice
    
    def comfunc():
        return random.choice(["rock","paper","scissor"])
    
    def winnerlogic(user,comp):
        if user == comp:
            return("it's Tie")
        elif (user=="rock" and comp=="scissor") or\
            (user=="paper" and comp=="rock") or \
            (user =="scissor" and comp=="paper"):
            return(">>>>>YOU WIN<<<<<")
        else:
            return(">>>>>COMPUTER WINS<<<<<")
    
    rounds=int(input("HOW MANY ROUNDS YOU WANT:- "))
    userscore=0
    compscore=0
    for i in range(1,rounds+1):    
        user=inpfunc()
        comp=comfunc()
        print(f"ROUND NO:- {i}")
        # print(f"YOU ENTER {user}")
        print(f"COMPUTER CHOICE {comp}")
        print(winnerlogic(user,comp))
        result=winnerlogic(user,comp)
        if ">>>>>YOU WIN<<<<<" in result:
            userscore=userscore+1
        elif ">>>>>COMPUTER WINS<<<<<" in result:
            compscore=compscore+1
        else:
            pass
    print("\n🎉 TOURNAMENT OVER 🎉")
    print(f"Your Score: {userscore}")
    print(f"Computer Score: {compscore}")
    if userscore>compscore:
        print("YAHOO!!!!YOU WIN THE TOURNAMENT")
    elif compscore>userscore:
        print("NOT BAD!!!!COMPUTER WIN THE TOURNAMENT")
    else:
        print("TOURNAMENT IS TIE")
# ----------------------------------------------------------------------------
def main():
    while True:
        print("=======WELLCOME TO THE GAME=======")
        print("1.PLAY")
        print("2.TOURNAMENT")
        print("3.EXIT")
        choice=int(input("YOUR CHOICE(1-3):- "))
        match choice:
            case 1:
                play()
            case 2:
                tournament()
            case 3:
                break
            case _:
                print("INVALID CHOICE")
main()
