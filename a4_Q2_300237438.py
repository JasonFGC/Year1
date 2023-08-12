def two_length_run(n):
    '''
    list of str - > int
    finds the first run of length 2, stops the program when found and returns true. otherwise, returns false.
    '''
    x=0
    i=0
    while x==0:
        if i<len(n)-1 and n[i]==n[i+1]:
             x+=1
        elif i==len(n):
             x+=2
        i+=1
    if x==1:
        return True
    else:
        return False


raw_input = input("Please input a list of numbers separated by spaces: ").strip().split()
for i in range (0,len(raw_input)):
    raw_input[i]=int(raw_input[i])
result=two_length_run(raw_input)
print(result)
