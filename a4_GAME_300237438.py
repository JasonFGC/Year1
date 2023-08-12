# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]
     for i in range(0,26):
         other.append(deck[i])
     for i in range(26,51):
         dealer.append(deck[i])
     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    counter=0
    no_pairs=[]
    l.sort()
    for i in l: 
        for j in l:
            if i[0] == j[0] and i!=j and counter==0:
                l.remove(j)
                counter=1
        if counter==1:
            l.remove(i)
            counter=0
    for i in l: 
        for j in l:
            if i[0] == j[0] and i!=j and counter==0:
                l.remove(j)
                counter=1
        if counter==1:
            l.remove(i)
            counter=0
    for k in l:
        no_pairs.append(k)
            
        
        
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    x=""
    for i in range (0,len(deck)):
        x=x+deck[i]+" "
    print(x)
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     y=False
     x=int(input("Give me an integer between 1 and "+str(n)+": "))
    
     if x<1 or x>n:
        y=False
     else:
        y=True
     while y==False:
         x=int(input("Invalid number. Please enter an integer between 1 and "+str(n)+": "))
         if x<1 or x>n:
             y=False
         elif x>1 and x<n:
             y=True
     return x
     
     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
        
def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)
     turn=1
     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     while len(human)>0 and len(dealer)>0:
         if turn==1:
             print("***********************************************************")
             print("Your turn.")
             print("")
             print("Your current deck of cards is:")
             print_deck(human)
             print("I have "+str(len(dealer))+" cards. If 1 stands for my first card and")
             print(str(len(dealer))+" for my second card, which of my cards would you like?")
             choice=(get_valid_input((len(dealer))))
             if choice==1:
                print("You asked for my 1st card.")
                print("Here it is. It is "+dealer[choice-1])
                print("With "+dealer[choice-1]+" added, your current deck of cards is:")
                human.append(dealer[choice-1])
                dealer.pop(choice-1)
                print_deck(human)
             elif choice==2:
                print("You asked for my 2nd card.")
                print("Here it is. It is "+dealer[choice-1])
                print("With "+dealer[choice-1]+" added, your current deck of cards is:")
                human.append(dealer[choice-1])
                dealer.pop(choice-1)
                print_deck(human)
             elif choice==3:
                print("You asked for my 3rd card.")
                print("Here it is. It is "+dealer[choice-1])
                print("With "+dealer[choice-1]+" added, your current deck of cards is:")
                human.append(dealer[choice-1])
                dealer.pop(choice-1)
                print_deck(human)
             else:
                print("You asked for my "+str(choice)+"th card.")
                print("Here it is. It is "+dealer[choice-1])
                print("With "+dealer[choice-1]+" added, your current deck of cards is:")
                human.append(dealer[choice-1])
                dealer.pop(choice-1)
                print_deck(human)
             human=remove_pairs(human)
             print("And after discarding pairs and shuffling, your deck is:")
             print_deck(human)
             turn=2
             wait_for_player()
         elif turn==2:
             print("***********************************************************")
             print("My turn.")
             print("")
             pick=random.randint(1,len(human))
             if pick==1:
                 print("I took your 1st card")
             elif pick==2:
                 print("I took your 2nd card")
             elif pick==3:
                 print("I took your 3rd card")
             else:
                 print("I took your "+str(pick)+"th card")
             dealer.append(human[pick-1])
             human.pop(pick-1)
             dealer=remove_pairs(dealer)
             turn=1
             wait_for_player()       
     if len(human)==0:
         print("***********************************************************")
         print("Ups. You do not have any more cards.")
         print("Congratulations! You, human, win!")
     elif len(dealer)==0:
         print("Ups. I ran out of cards.")
         print("You lost! I, robot, win.")
                    
# main
play_game()
