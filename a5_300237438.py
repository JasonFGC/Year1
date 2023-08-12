import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
            
    # YOUR CODE GOES HERE
    totalUsers=[]
    allFriends=[]
    for i in range(1,len(friends)):
        pair=friends[i].split()
        user=int(pair[0])
        userFriend=int(pair[1])
        if user not in totalUsers:
            totalUsers.append(user)
        if userFriend not in totalUsers:
            totalUsers.append(userFriend)
    totalUsers.sort()
    for j in range(0,len(totalUsers)):
        allFriends.append([])
    for k in range(1,len(friends)):
        pair=friends[k].split()
        user=int(pair[0])
        friend=int(pair[1])
        indexUser=totalUsers.index(user)
        indexFriend=totalUsers.index(friend)
        if friend not in allFriends[indexUser]:
            allFriends[indexUser].append(friend)
        if user not in allFriends[indexFriend]:
            allFriends[indexFriend].append(user)

    for l in range(0,len(totalUsers)):
        network.append((totalUsers[l],allFriends[l]))
                
            
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]

    
        
    # YOUR CODE GOES HERE
    indexUser1=0
    indexUser2=0
    for j in range(0,len(network)):
        if network[j][0]==user1:
            indexUser1=j
    for k in range(0,len(network)):
        if network[k][0]==user2:
            indexUser2=k
    for i in range(0,len(network[indexUser1][1])):
        friend=network[indexUser1][1][i]
        if friend in network[indexUser2][1]:
            common.append(friend)
    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    recc=0
    target=0
    indexUser=0
    indexTarget=0
    indexRecc=0
    noneInCommon=0
    for j in range(0,len(network)):
        if network[j][0]==user:
            indexUser=j
    for i in range (0,len(network)):
        for l in range(0,len(network)):
            if network[l][0]==recc:
                indexRecc=l
        target=int(network[i][0])
        commonTarget=len(getCommonFriends(target,user,network))
        commonBefore=len(getCommonFriends(recc,user,network))
        for k in range(0,len(network)):
            if network[k][0]==target:
                indexTarget=k
        if commonTarget==0 or target==user:
                noneInCommon+=1
        elif (str(target) not in network[indexUser][1]) and (commonTarget > commonBefore):
            recc=target
        if noneInCommon==len(network):
            return None
    return recc

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    numUsers=0
    for i in range(0,len(network)):
        if len(network[i][1])>=k:
            numUsers+=1
    return numUsers    
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    maxi=0
    for i in range(0,len(network)):
        if len(network[i][1])>=maxi:
            maxi=len(network[i][1])
    return maxi
def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE
    maxi=maximum_num_friends(network)
    for i in range(0,len(network)):
        if len(network[i][1])==maxi:
            max_friends.append(network[i][0])
    return  max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    totalfriends=0
    for i in range(0,len(network)):
        totalfriends+=len(network[i][1])
    average=totalfriends/len(network)
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    maxi=maximum_num_friends(network)
    if maxi==len(network):
        return True
    else:
        return False
    # YOUR CODE GOES HERE


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    # YOUR CODE GOES HERE
    ans=None
    while ans==None:
        try:
            ans=int(input("Input a user ID: "))
        except ValueError:
            print("That was not an integer. Try again.")
    i=0
    flag=0
    while flag==0:
        if i==len(network):
            i=0
            print("That user does not exist. Please try again.")
            ans==None
            while ans==None:
                try:
                    ans=int(input("Input a user ID: "))
                except ValueError:
                    print("That was not an integer. Try again.")
        elif ans==network[i][0]:
            flag+=1
        else:
            i+=1
    return ans

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
