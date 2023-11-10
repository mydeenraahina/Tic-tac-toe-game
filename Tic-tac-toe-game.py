import random
print("============ Tic-Tac-Toe Game ============")                          
def main_block():
    list=["_" for i in range(0,10)]
    print(list[0],list[1],list[3])
    print(list[4],list[5],list[6])
    print(list[7],list[8],list[9])
    class tictactoe:
        x=0
        o=0
        def conditions_for_user_won(self):
            if list[0]==list[1]==list[2]=="x":
                print("user won the game")
                tictactoe.x+=1
            elif list[3]==list[4]==list[5]=="x":
                print("user won the game")
                tictactoe.x+=1
            elif list[6]==list[7]==list[8]=="x":
                print("user won the game")
                tictactoe.x+=1
            elif list[0]==list[3]==list[6]=="x":
                print("user won the game")
                tictactoe.x+=1
            elif  list[1]==list[4]==list[7]=="x":
                print("user won the game")
                tictactoe.x+=1
            elif  list[2]==list[5]==list[8]=="x":
                print("user won the game")
                tictactoe.x+=1
            elif  list[0]==list[4]==list[8]=="x":
                print("user won the game")
                tictactoe.x+=1
            elif  list[2]==list[4]==list[6]=="x":
                print("user won the game")
                tictactoe.x+=1
            else:
                pass
            
        def conditions_for_computer_won(self):
            if list[0]==list[1]==list[2]=="o":
                print("computer won the game")
                tictactoe.o+=1
            elif list[3]==list[4]==list[5]=="o":
                print("computer  won the game")
                tictactoe.o+=1
            elif list[6]==list[7]==list[8]=="o":
                print("computer  won the game")
                tictactoe.o+=1
            elif list[0]==list[3]==list[6]=="o":
                print("computer  won the game")
                tictactoe.o+=1
            elif  list[1]==list[4]==list[7]=="o":
                print("computer  won the game")
                tictactoe.o+=1
            elif  list[2]==list[5]==list[8]=="o":
                 print("computer won the game")
                 tictactoe.o+=1 
            elif  list[0]==list[4]==list[8]=="o":
                 print("computer  won the game")
                 tictactoe.o+=1 
            elif  list[2]==list[4]==list[6]=="o":
                 print("computer  won the game")
                 tictactoe.o+=1 
        def player1_user(self):
            print("your choice")
            user_choice=int(input("Enter the value \"x\" in the position[0-8] :"))
            try:
               if list[user_choice]=="_":
                   list[user_choice]="x"
                   print(list[0],list[1],list[2])
                   print(list[3],list[4],list[5])
                   print(list[6],list[7],list[8])
                   obj.conditions_for_user_won()
               else:
                   print(f"{user_choice} position is not empty")
                   obj.player1_user()
            except IndexError:
                print(f"{user_choice} is not a valid position")
                obj.player1_user()
        def player2_computer(self):
            print("computer choice")
            computer_choice=random.randint(0,9)
            try:
                if list[computer_choice]=="_":
                    list[computer_choice]="o"
                    print(list[0],list[1],list[2])
                    print(list[3],list[4],list[5])
                    print(list[6],list[7],list[8])
                    obj.conditions_for_computer_won()
                else:
                    print(f"{computer_choice} position is not empty")
                    obj.player2_computer()
            except IndexError:
                print(f"{computer_choice}it is not a valid position")
                obj.player2_computer()
    while True:
        obj=tictactoe()
        obj.player1_user()
        if tictactoe.x==1:
            break
        obj.player2_computer()
        if tictactoe.o==1:
            break
        elif  list[0]!="|" "_" "|" and list[1]!="_"and list[2]!="_"and list[3]!="_"and list[4]!="_"and list[5]!="_"and list[6]!="_"and list[7]!="_"and list[8]!="_"and tictactoe.x==tictactoe.o==0:
            print("game tied")
            break
play=input(f"Do you want to play this game[ yes/no]  :")
if play=="yes":
    main_block()
    while True:
        play1=input(f"do u continue this game[yes/no] ")
        if play1=="yes":
            main_block()
        else:
            print("EXITED!")
            break
else:
    print("Exit!")

    





