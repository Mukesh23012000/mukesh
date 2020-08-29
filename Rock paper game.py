print("Welcome TO ROCK PAPER SCISSOR GAME")
def multi():
    D=input("enter the first player name : ")
    E=input("enter the second player name: ")
    print("its",D,"turn")
    C=int(input("1.Rock 2.Paper 3.Scissor "))
    if(C!=1 or C!=2 or C!=3):
        print("please enter the valid option")
    print("its",E,"turn")
    F=int(input("1.Rock 2.Paper 3.Scissor "))
    if(F!=1 or F!=2 or F!=3):
        print("please enter the valid option")
    elif(C==F):
        print("DRAW")
    elif(C==1 and F==3):
        print("the winner is",D)
    elif(C==2 and F==1):
        print("the winner is",D)
    elif(C==3 and F==2):
        print("the winner is",D)
    else:
        print("the winner is",E)
def single():
    import random
    n=random.randint(1,3)
    D=input("enter your name")
    print("wlecome to the game ",D)
    print("its your turn",D)
    C=int(input("1.Rock 2.Paper 3.Scissor"))
    F=n
    if(C==F):
        print("DRAW")
    elif(C==1 and F==3):
        print("the winner is",D)
    elif(C==2 and F==1):
        print("the winner is",D)
    elif(C==3 and F==2):
        print("the winner is",D)
    else:
        print("the winner is me(computer)")

def start():        
    
    B=int(input("1.Multipalayer or 2.single player"))

    if(B==1):
        multi()
        end()
    
    elif(B==2):
        single()
        end()

def end():
    z=input("enter OK to replay the game OR enter NO to end the game:   ")
    if(z=="ok" or z=="OK" or z=="Ok" or z=="kO"):
        start()
    elif(z=="NO" or z=="on" or z=="On" or z=="oN" ):
       print("tankyou for playing the game")
    else:
        print("please select OK or ON")
        end()
start()

