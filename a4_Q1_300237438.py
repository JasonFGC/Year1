def number_divisible(s,n):
    '''
    list of int,int
    Finds out how many ints inside the list are divisible by n.
    '''
    x=0
    for i in range(0,len(s)):
        if s[i]%n==0:
            x=x+1
    return x

raw_input = input("Please input a list of numbers separated by a space: ").strip().split(" ")
for i in range (0,len(raw_input)):
    raw_input[i]=int(raw_input[i])
divisor= int(input("Please enter an integer: "))
result=number_divisible(raw_input,divisor)
print("The number of elements divisible by "+str(divisor)+" is "+str(result))
