#Name: Jason Lam
#Course: ITI1120
#Assignment: Assignment 3 part 2

import math
def sum_odd_divisors(n):
    '''
    int->int
    Finds the sum of all positive odd divisors of the given number.
    Preconditions: Must be an integer.
    '''
    z=0
    if n==0:
        return
    else: 
        if n<0:
            n=n*(-1)
        for i in range(1,n+1,2):
            if n%i==0:
                z=z+i
        return z

def series_sum():
    '''
    int->int
    Calculates the following series if the input is positive. 1000+(1/1^2)+(1/2^2)+...(1/n^2)
    if the input is negative, it returns none.
    Preconditions: Must be integer.
    '''
    x=int(input("Please enter a non-negative integer: "))
    y=0
    z=0
    if x<0:
        return
    elif x==0:
        y=1000
        return(y)
    else:
        for i in range(1,x+1,1):
            z=z+1/(i**2)
        y=1000+z
        return (y)
    
def pell(n):
    '''
    int->int
    Calculates pell's number for the given number
    Preconditions: Must be integer.
    '''    
    x=0
    y=1
    z=0
    for i in range(1,n):
        z=((2*y)+x)
        x=y
        y=z
    if n>=0:
        return z
    else:
        return

    

    

    
def countMembers(s):
    '''
    Str->int
    Counts the amount of "Extraordinary" characters.
    No preconditions.
    ''' 
    counter=0
    for char in s:
        if (char>="e" and char<="j") or (char>="F" and char<="X") or (char>="2" and char<="6") or char=="!" or char=="," or char=="\\":
            counter=counter+1
    return counter


def casual_number(s):
    '''
    Str-> Int
    Takes the given string and takes out the commas. If there are non numbers, such as letters, the function returns none.
    Preconditions: Can only input numbers,letters and commas. Commas are in meaningful places.
    '''
    counter=0
    neg=0
    dig=0
    y=""
    x=s
    z=x[0]
    if z=="-":
        x=s[1:len(s)]
        neg=neg+1
    x=x.split(",")
    for char in x:
        if char.isdigit()==False:
            counter=counter+1
        elif char.isdigit()==True:
            y=y+char
            dig=dig+1
    if neg>=2:
        return
    elif counter>0:
        return
    elif dig==0:
        return
    elif neg==1:
        y=int(y)
        return (y*(-1))
    else:
        y=int(y)
        return (y)

def alienNumbers(s):
    '''
    Str->int
    Takes the alien symbol language and finds the value of all the symbols added up.
    Preconditions: Only the symbols T,y,!,a,N and U are acceptable.
    '''
    x=s.count("T")
    y=s.count("y")
    z=s.count("!")
    a=s.count("a")
    b=s.count("N")
    c=s.count("U")
    total=(x*1024)+(y*598)+(z*121)+(a*42)+(b*6)+(c)
    return total


def alienNumbersAgain(s):
    '''
    Str->int
    Same as the above, but without string methods.
    Takes the alien symbol language and finds the value of all the symbols added up.
    Preconditions: Only the symbols T,y,!,a,N and U are acceptable.
    '''
    countT=0
    county=0
    countex=0
    counta=0
    countN=0
    countU=0
    for char in s:
        if char in "T":
            countT=countT+1
        elif char in "y":
            county=county+1
        elif char in "!":
            countex=countex+1
        elif char in "a":
            counta=counta+1
        elif char in "N":
            countN=countN+1
        elif char in "U":
            countU=countU+1
    total=(countT*1024)+(county*598)+(countex*121)+(counta*42)+(countN*6)+(countU)
    return total

def encrypt(s):
    '''
    str->str
    Takes a string, and encrypts it.
    Precondtions: None.
    '''
    x=s[ : :-1]
    y=""
    z=0
    
    if len(s)%2==0:
        z=round(len(s)/2)
        for i in range(0,z):
            y=y+x[i]+s[i]

    elif len(s)%2>0:
        z=math.ceil((len(s)/2))
        for i in range(0,z-1):
            y=y+x[i]+s[i]
        y=y+s[z-1]
    return y


def oPify(s):
    '''
    Str->Str
    Takes a string and puts op in between the characters if they are letters. If the letters are capitalized, the o and p are capitalized depending on which letter is capitalized.
    Preconditions: none
    '''
    x=""
    for i in range(0,len(s)-1):
        if s[i].isalpha() and s[i].isupper() and s[i+1].isupper():
            x=x+s[i]+"OP"
        elif s[i].isalpha() and s[i].isupper():
            x=x+s[i]+"Op"
        elif s[i].isalpha() and s[i+1].isupper():
            x=x+s[i]+"oP"
        elif s[i].isalpha():
            x=x+s[i]+"op"
        else:
            x=x+s[i]
    x=x+s[len(s)-1]    
    return x
            
def nonrepetitive(s):
    '''
    str->bool
    Determines if the given string is a nonrepetitive string or not.
    '''
    x=""
    y=""
    for i in range(0,(len(s)//2)+1):
        for j in range(0,i):
             x=x+s[j:i+1]
             print(x)
             y=y+s[j+i:i+1]
             print(y)
             x=""
             y=""
        x=""


        
