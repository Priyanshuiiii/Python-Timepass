import random
#1 for snake
#-1 for water 
#0 for gun

computer=random.choice([1,-1,0])
user=input("Enter your choice:")
User_Dict={'s':1,'w':-1,'g':0}
reverse_dict={1:"snake",-1:"water",0:"gun"}
User_num=User_Dict[user]
print(f"You choose {reverse_dict[User_num]}\ncomputer choose  {reverse_dict[computer]}")

if(computer==User_num):
    print("Its a draw!")
else:
    if(computer == 1 and User_num == -1):
        print("computer Wins")
    elif(computer == 1 and User_num == 0):
        print("You Wins")
    elif(computer == -1 and User_num == 0):
        print("computer Wins")    
    elif(computer == -1 and User_num == 1):
        print("You Wins")
    elif(computer == 0 and User_num == -1):
        print("You Wins")
    elif(computer == 0 and User_num == 1):
        print("Computer  Wins")            
    else:
        print("something went wrong")