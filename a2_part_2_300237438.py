def min_enclosing_rectangle(radius, x, y):
    if radius>0:
        rx=x-radius
        ry=y-radius
        coordinates="("+str(rx)+", "+str(ry)+")"
        return coordinates
    else:
        pass

def vote_percentage(results):
    x=0
    y=0
    z=0
    for char in results:
        if char in "yY":
            x=x+1
            y=y+1
        elif char in "o":
            y=y+1

    z=x/y 
    return(z)

def vote():
    votes=input("Enter the yes, no, abstained votes one by one and then press enter:\n")
    x=vote_percentage(votes)
    if x==1:
        print("proposal passes unanimously")
    elif x>=(2/3):
        print("proposal passes with super majority")
    elif x>=(1/2):
        print("proposal passes with simple majority")
    else:
        print("proposal fails")

def l2lo(w):
    x=w//1
    o=(w-x)*16
    ans="("+str(x)+", "+str(o)+")"
    return(ans)
