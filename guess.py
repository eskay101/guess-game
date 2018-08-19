# program that allow the user to guess a particular number:
import random
number = random.randrange ( 1 , 100)
print ( ' randomNumber ' ,number )
user = int ( input ( ' enter your guess number : '))
while   user==number : 
    print ( ' congrat !! ' , ' you are correct ' )
if (user < number ):
    print ( ' you are close !! ' , ' try again later ') 
elif (user > number) :
    print ( ' you are not close !! ' , ' try again later ' )
    print ( ' end of guessing ' )