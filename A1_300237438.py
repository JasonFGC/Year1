# Name: Jason Lam
# Student number:  300237438
# Course: IT1 1120 
# Assignment Number 1
# year 2021

import math
import turtle
###################################################################
# Question 4
###################################################################
def safe(n):
    '''
    (number)->bool
    Finds if your number is a safe number, which does not contain a 9 or is divisible by 9.
    Preconditions: Must be a positive 2 digit number.
    '''
    y=(n<100 and n%9!=0 and n>=0) and n!= 9 and n!= 19 and n!= 29 and n!= 39 and n!= 49 and n!= 59 and n!= 69 and n!= 79 and n!= 89 and n!= 91 and n!= 92 and n!= 93 and n!= 94 and n!= 95 and n!= 96 and n!= 97 and n!= 98  
    print(y)

###################################################################
# Question 5
###################################################################
def quote_maker(quote, name, year):
    '''
    (str,str,Int)->str
    Outputs a sentence that includes the quote, name of the person who said it, and the year they said the quote.
    '''
    x=str(quote)
    y=str(name)
    z=str(year)
    last=("In "+z+", a person called "+y+' said "'+x+'"')
    return last

###################################################################
# Question 6
###################################################################
def quote_displayer():
    '''
()->str
Will ask you 3 times for a quote, name and year. They then are put into quote_maker and prints the result.
    '''
    quote=input("What is the quote? ")
    name=input("Who said the quote? ")
    year=input("When did they say the quote? ")
    result = quote_maker(quote,name,year)
    print(result)
###################################################################
# Question 7
###################################################################
def rps_winner():
    '''
    ()->str
    Asks the user for both actions from the players and checks if Player 1 wins, and if they tied. It then prints the result.
    '''
    Player1=input("What is Player 1's action? \nType one of the following options: rock, paper, scissors: ")
    Player2=input("What is Player 2's action? \nType one of the following options: rock, paper, scissors: ")
    ResultWin= (Player1=="scissors" and Player2=="paper") or (Player1=="rock" and Player2=="scissors") or (Player1=="paper" and Player2=="rock")
    ResultTie= (Player1!=Player2)
    ResultA="Player 1 wins. That is "+str(ResultWin)
    ResultB="It is a tie. That is not "+str(ResultTie)
    print (ResultA)
    print (ResultB)

###################################################################
# Question 8
###################################################################
def fun(x):
    '''
    (number) -> number
    Will take x and solve for y in the equation 10^4y=x+3. Returns the result.
    '''
    a=x+3
    b=((math.log(a))/(math.log(10)))/4
    return b
###################################################################
# Question 9
###################################################################
def ascii_name_plaque(name):
    '''
    (str )- > str
    Takes the input and puts it inside of a plaque made from Ascii art.
    '''
    z=("* __"+name+"__ *")
    x=(len(name))+10
    y=(len(name))+5
    print("*"*x)
    print("*"+"  "*y+"*")
    print(z)
    print("*"+"  "*y+"*")
    print("*"*x)
    #could not get it to look perfect consistently, got stuck
###################################################################
# Question 10
###################################################################


###################################################################
# Question 11
###################################################################
def alogical(n):
    '''
    number -> number
    Takes the input and finds how many times 2 can be divided into it until the number is less than 1.
    Preconditions : number must be equal to or bigger than 1.
    '''
    x=n%2
    y=x/2
    z=y*n
    a=z//1
    return(a)
    print(x)
    print(y)
    print(z)
    print(a)
#got stuck

###################################################################
# Question 12
###################################################################
def cad_cashier(price,payment):
    '''
    (number,number)-> number
    Takes the price and the amount paid, and gets the change for the user. Rounds the change to the nearest 5 cents.
    Preconditions: input must be positive, you cannot pay negative money.
    '''
    a=price
    b=payment
    x=b-a
    y=x//1
    findcents=round((x-y)*100)
    final=(5*round(findcents/5))/100
    change=y+final
    return(change)
    

###################################################################
# Question 13
###################################################################
def min_CAD_coins(price,payment):
    '''
    (number,number) -> number
    Takes the input and the change by using the cad_cashier function.
    Then finds the minimum amount of coins needed to get that change.
    Preconditions: input must be positive.
    '''
    a=price
    b=payment
    x=(cad_cashier(a,b))
    y=round(x*100)
    toonie=y//200
    aftert=y-(200*toonie)
    loonie=aftert//100
    afterl=aftert-(100*loonie)
    quarter=afterl//25
    afterq=afterl-(25*quarter)
    dime=afterq//10
    afterd=afterq-(10*dime)
    nickle=afterd//5
    aftern=afterd-(5*nickle)
    total="("+str(toonie)+", "+str(loonie)+", "+str(quarter)+", "+str(dime)+", "+str(nickle)+", "+")"
    return total
