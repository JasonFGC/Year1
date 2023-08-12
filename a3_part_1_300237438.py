def split_tester(N, d):
    # Your code for split_tester function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    '''
    str,str->bool
    takes a string of numbers and splits them up depending on what d is. It then returns true if the numbers are in ascending order and false if not.
    Preconditions: d must be a divisor of N, N and d must be made of numbers.
    '''
    x=""
    y=len(N)
    z=""
    a=int(d)
    b=0
    c=""
    counter=True
    for i in range(y):
        if i==a:
            
            b=int(x)
            z=z+x+","
            a=a+int(d)
            x=""
            x=x+(N[i])
            
            
            
        elif i<=a:
            x=x+(N[i])
        if b>(int(x)) and len(x)==int(d):
            counter=False

        
    x=""
    for i in range(y-int(d),y):
        x=(N[i])
        z=z+x
    print (z)
    return counter
    

# you can add more function definitions here if you like       


            
# main
# Your code for the welcome message goes here, instead of name="Vida"

aaaa="Welcome to my increasing-splits tester"
print(5*"*"+len(aaaa)*"*"+5*"*")
print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
print("*  "+2*"_"+aaaa+2*"_"+"  *")
print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
print(5*"*"+len(aaaa)*"*"+5*"*")
name=input(str("What is your name? "))
name=name.strip()


flag=True
while flag:
    question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        aaaa="Good bye "+name+"!"
        print(5*"*"+len(aaaa)*"*"+5*"*")
        print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
        print("*  "+2*"_"+aaaa+2*"_"+"  *")
        print("*"+4*" "+len(aaaa)*" "+4*" "+"*")
        print(5*"*"+len(aaaa)*"*"+5*"*")
        flag=False
    #YOUR CODE GOES HERE. The next line should be elif or else.
    elif question=="yes":
            print("Good choice!")
            x=str(input("Enter a positive integer: "))
            x=x.strip()
            digx=0
            digy=0
            for char in x:
                if char.isalpha()==True:
                    digx=digx+1
            if digx>=1:
                print("The input can only contain digits. Try again.")
                digx=0
            elif int(x)>=0:
                y=str(input("Input the split. The split has to divide the length of "+str(x)+" i.e "+str(len(x))+" "))
                for char in str(y):
                    if char.isalpha()==True:
                        digy=digy+1
                if digy>=1:
                    print("The input can only contain digits. Try again.")
                elif int(y)>=1:
                    if len(x)%int(y)==0:
                        z=split_tester(x,y)
                        if z==True:
                            print("The sequence is increasing.")
                        elif z==False:
                            print("The sequence is not incereasing.")
                    if len(x)%int(y)!=0:
                        print(str(y)+" does not divide "+str(len(x))+". Try again.")
                elif int(y)<=0:
                    print("The input has to be positive and not zero. Try again.")
            elif int(x)<0:
                print("The input has to be a positive. Try again.")
    elif question!="yes" or question!="no":
            print("Please enter yes or no. Try again.")
        
#finally your code goes here too.
