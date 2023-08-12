def longest_run(n):
    '''
    list of str - > int
    finds the longest run in the list.
    Preconditions: List is made up of numbers
    '''
    x=1
    largest=0
    before=0
    current=0
    for i in range(0,len(n)-1):
        if i<len(n)-1 and n[i]==n[i+1] and n[i]==current:
            x+=1
        elif i<len(n)-1 and n[i]==n[i+1]:
            current=n[i]
            x+=1
        elif i<len(n)-1 and n[i]!=n[i+1]:
            before=x
            if before>largest:
                largest=before
            x=1
        elif len(n)==0:
            largest=0
    return largest
raw_input = input("Please input a list of numbers separated by spaces: ").strip().split()
for i in range (0,len(raw_input)):
    raw_input[i]=float(raw_input[i])
result=longest_run(raw_input)
print(result)
