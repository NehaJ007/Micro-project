print "*******************************************************************"
print "                  ROCK PAPER SCISSORS GAME                         "
print "*******************************************************************"
import random                                                                          #RANDOM FUNC-TO GENERATE RANDOM VARIABLES
while True:                                         
 print "-----MENU----- \n1.ROCK\n2.PAPER\n3.SCISSORS\n"                                #PRINT THE MENU OF THE GAME
 choice1=input("Enter your choice:")                                                   #FOR INPUTTING THE USERS CHOICE
 if(choice1==1):
	user_choice="rock"
 elif(choice1==2):
	user_choice="paper"
 elif(choice1==3):
	user_choice="scissors"
 print "Your choice is : ",user_choice
 choice2=random.randint(1,3)                                                           #RANDOMLY GENERATES NUMBERS 1,2,3 
 if(choice2==1):                                                                       #COMPUTER'S CHOICE IS ASSIGNED
	comp_choice="rock"
 elif(choice2==2):
	comp_choice="paper"
 elif(choice2==3):
	comp_choice="scissors"
 print "Computers choice is : ",comp_choice
 if((choice1==1 and choice2==2) or (choice1==2 and choice2==1)):                       #FOR CHECKING WHICH WINS WHETHER ROCK OR PAPER OR SCISSORS 
	result="paper"
 elif((choice1==2 and choice2==3) or (choice1==3 and choice2==2)):
	result="scissors"
 elif((choice1==1 and choice2==3) or (choice1==3 and choice2==1)):
	result="rock"
 else:
	result="tie"
 if(result==user_choice):                                                             #FOR DISPLAYING WHO WINNED THE GAME USER OR COMPUTER OR WHETHER IT IS A TIE
	print"YOU HAVE WON"
 elif(result==comp_choice):
        print"COMPUTER WINS"
 else:
        print "ITS A TIE"
 reply=raw_input("Enter n/N if you want to continue : ")                              #ASK USER TO WHETHER CONTINUE IN GAME OR NOT
 if(reply=='n' or reply=='N'):
        break                                                                         #COMES OUT OF THE WHILE LOOP
print "Thanks for playing"


