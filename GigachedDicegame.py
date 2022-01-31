#dice game LewOS test 1234
#made by gigachad
import time
import random
import sys

global p1name
global p2name
global playercounter
playercounter = 0


def account():
    loop = True
    def write():
        PlayerName = input("Enter Player Name: ")
        Password = input("Enter Password: ")
        PlayerPass = str(PlayerName+Password)
        f = open("Passwords.txt","a")
        f.write(PlayerPass+"\n")
        f.close()
    
    def read():
        Username = input("Enter Player Name: ")
        Userpassword = input("Enter Password: ")
        UserPass = str(Username+Userpassword)
        f = open("Passwords.txt","r")
        endoffile = False
        Found = False
        while endoffile == False:
            PlayerPass = f.readline().strip()
            if UserPass == PlayerPass:
                print("Username and Password Correct")
                print("")
                global playercounter
                if playercounter == 0:
                    global p1name
                    p1name = Username
                else:
                    global p2name
                    p2name = Username
                Found = True
                playercounter = playercounter + 1
                endoffile = True
            elif PlayerPass == "" and Found == False:
                print("Incorrect Username or Password")
                print("")
                endoffile = True
            else:
                pass
        f.close()
            
    def menu():
        print("Press 1 to Create an account")
        print("Press 2 to Login")
        print("Press 3 to Exit")
        print("")
    
    
    menu()
    while loop == True:
        if playercounter == 0:
            print("")
            print("Player One Login")
        elif playercounter == 1:
            print("")
            print("Player Two Login")
        else:
            loop = False
            break
        print("")
        choice = input("Pick an option: ")
        if choice.isdigit() == False:
            print("Enter a Number")
        elif int(choice) > 3 or int(choice) < 1:
            print("Pick a number between 1 and 3")
        elif int(choice) == 2:
            read()
        elif int(choice) == 1:
            write()
        elif int(choice) == 3:
            print("Play again soon")
            exit()
        else:
            print("Pick a valid option")

print("Welcome to GIgachad's DICE GAME!")
print("Made by Dimitri Checknov aka. Gigachad")
print("")
print("Create or Login to an account to play the game.")
print("")
account()
print("")
print("Now that both players have logged in...")

print("")
print("")
for letter in ("LET THE GAME COMMENCE!"):
    sys.stdout.write(letter)
    time.sleep(.05)
print("")
for letter in (p1name," VS ",p2name):
    sys.stdout.write(letter)
    time.sleep(.05)
print("")

for letter in ("Round 1"):
    sys.stdout.write(letter)
    time.sleep(.05)
print("")
for letter in (p1name," Rolling..."):
    sys.stdout.write(letter)
    time.sleep(.05)
print("")
time. sleep(random.randint(1,3))
p1d1 = random.randint(1,6)
p1d2 = random.randint(1,6)
print("")
tempscore = p1d1 + p1d2
print(p1name,"rolled a",p1d1,"and a",p1d2,"and the total is",tempscore)
if tempscore % 2  == 0:
    tempscore = tempscore * 2
    print("Because added total is even, the total is doubled, giving a score of",tempscore)
    p1score = tempscore
elif tempscore < 5:
    tempscore = 0
    print("Because added total is odd, the total has 5 subtracted, giving a score of",tempscore)
else:
    tempscore = tempscore - 5
    print("Because added total is odd, the total has 5 subtracted, giving a score of",tempscore)
time.sleep(5)
p1score = tempscore
print("")
print(p2name,"Rolling...")
time. sleep(random.randint(1,3))
p2d1 = random.randint(1,6)
p2d2 = random.randint(1,6)
print("")
tempscore = p2d1 + p2d2
print(p2name,"rolled a",p2d1,"and a",p2d2,"and the total is",tempscore)
if tempscore % 2  == 0:
    tempscore = tempscore * 2
    print("Because added total is even, the total is doubled, giving a score of",tempscore)
elif tempscore < 5:
    print("Because added total is odd, the total has 5 subtracted, giving a score of",tempscore)
else:
    tempscore = -4
    p2score = tempscore
    print("Because added total is odd, the total has 5 subtracted, giving a score of",tempscore)
time.sleep(5)
p2score = tempscore
p2score = p2score + tempscore
if p1score > p2score:
    print("After round 1",p1name,"is winning with a score of",p1score," and",p2name,"has a score of ",p2score,".")
elif p2score > p1score:
    print("After round 1",p2name,"is winning with a score of",p2score," and",p1name,"has a score of ",p1score,".")
else:
    print("Both players have a score of",p1score)
print("")


