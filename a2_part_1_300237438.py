import math
import random


def elementary_school_quiz(flag, n):
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2
    q=n
    counter=0
    qNum=1
    while q>0:
        print("Question "+str(qNum))
        if flag==1:
            x=random.randint(1,10)
            y=2**x
            z=int(input("What is the result of 2^"+str(x)+"?"))
            if z==y:
                counter=counter+1  

        elif flag==0:
            x=random.randint(1,10)
            y=2**x
            z=int(input("2 to what is "+str(y)+" i.e. what is the result of log2 ("+str(y)+")?"))
            if (z==x):
                  counter=counter+1 
        qNum=qNum+1            
        q=q-1
    return(counter)  


def high_school_quiz(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    real=True
    inside=b**2-(4*a*c)
    if inside<=0:
        real=False
        inside=inside*(-1)
    if real==True:
        xi=(b*(-1)+math.sqrt(inside))/(2*a)
        xii=(b*(-1)-math.sqrt(inside))/(2*a)
        print("The quadratic equation "+str(a)+"*x^2 + "+str(b)+"*x + "+str(c)+" = 0\nhas the following real roots:")
        print(str(xi)+" and "+str(xii))
    elif real==False:
        x=((b**2)*(-1))/(4*a)
        ima=(math.sqrt(inside))/(2*a)
        print("The quadratic equation "+str(a)+"*x^2 + "+str(b)+"*x + "+str(c)+" = 0\nhas the following complex roots:")
        print(str(x)+" + i " + str(ima)+"\nand")
        print(str(x)+" - i " + str(ima))

# main

# your code for the welcome tmessage goes here
aaaa="Welcome to my math quiz-generator"
print(5*"*"+len(aaaa)*"*"+5*"*")
print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
print("*  "+2*"_"+aaaa+2*"_"+"  *")
print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
print(5*"*"+len(aaaa)*"*"+5*"*")
    
name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    aaaa=name+", welcome to my quiz-generator for elementary school students."
    print(5*"*"+len(aaaa)*"*"+5*"*")
    print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
    print("*  "+2*"_"+aaaa+2*"_"+"  *")
    print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
    print(5*"*"+len(aaaa)*"*"+5*"*")
    choice2=0
    choice=int(input(name+", what would you like to practice? Enter\n0 for inverse of exponentiation.\n1 for exponentiation.\n"))

    if (choice!=1 and choice!=0):
        print("Invalid choice. Only 0 or 1 is accepted")
    if (choice==1 or choice==0):
        choice2= int(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))
    if (choice2!=1 and choice2!=2 and choice2!=0 and (choice==1 or choice==0)):
        print("Only 0, 1, or 2 are valid choices for the number of questions.")
        
    elif choice2==0 and (choice==1 or choice==0):
        print("Zero questions. Ok. Good bye.")
        
    elif (choice==0 and choice2==1):
        print(name+", here is your question.")
        x=elementary_school_quiz(0, 1)
        if x==1:
            print("Congratulations "+name+"! You'll probably get an A tomorrow.")
        else:
            print("I think you need some more practice "+name+". Good bye "+name+"!")
                  
    elif (choice==1 and choice2==1):
        print(name+", here is your question.")
        x=elementary_school_quiz(0, 1)
        if x==1:
            print("Congratulations "+name+"! You'll probably get an A tomorrow.")
        else:
            print("I think you need some more practice "+name+". Good bye "+name+"!")


    elif (choice==0 and choice2==2):
        print(name+", here is your question.")
        print("Question 1:")
        x=elementary_school_quiz(0, 2)

        if x==2:
            print("Congratulations "+name+"! You'll probably get an A tomorrow.")
        elif x==1:
            print("You did ok "+name+", but I know you can do better.")
        else:
            print("I think you need some more practice "+name+". Good bye "+name+"!")

    elif (choice==1 and choice2==2):
        print(name+", here is your question.")
        x=elementary_school_quiz(1, 2)
        if x==2:
            print("Congratulations "+name+"! You'll probably get an A tomorrow.")
        elif x==1:
            print("You did ok "+name+", but I know you can do better.")
        else:
            print("I think you need some more practice "+name+". Good bye "+name+"!")
    # your code goes here
    pass

elif status=='2':
    aaaa="quadratic equation, a*x^2 + b*x + c = 0, solver for "+name
    print(5*"*"+len(aaaa)*"*"+5*"*")
    print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
    print("*  "+2*"_"+aaaa+2*"_"+"  *")
    print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
    print(5*"*"+len(aaaa)*"*"+5*"*")
    # your code for welcome message
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here

        if question!="yes" and question!="Yes" and question!="yEs" and question!="yeS" and question!="YEs" and question!="YeS" and question!="yES" and question!="YES":
            flag=False
        else:
            print("Good choice!")
            a=int(input("Enter a number the coefficient a: "))
            b=int(input("Enter a number the coefficient b: "))
            c=int(input("Enter a number the coefficient c: "))
            high_school_quiz(a,b,c)
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
 
else:
    # your code goes here
    print("Ah.\n")
    print(name+" you are not the target audience for this software.")

print("Good bye "+name+"!")
