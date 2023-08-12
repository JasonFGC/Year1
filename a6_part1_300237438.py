import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    file_name = None
    while file_name== None:
        try:
            file_name=input("Enter the name of the file: ").strip()
            f=open(file_name)
            f.close()
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name=None

    
    return file_name 
   

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    dictionary={}
    sentences = open(fp).read().splitlines()
    for i in range(len(sentences)):
        seperated=clean_sentence(sentences[i])
        for j in range(len(seperated)):
            word=seperated[j].lower()
            word=remove_punctuation(word)
            if (is_word(word)!=None)and (len(word)>=2):
                if word in seperated:
                            if word in dictionary:
                                dictionary[word].add(i+1)
                            else:
                                dictionary[word]={i+1}
                        
    return dictionary

def clean_sentence(x):
    '''list->list
    Takes the list given and takes away all punctuation in every word.
    Preconditions: list is made up of strings

    '''
    sentenceCleaned=[]
    x=x.split(" ")
    current=""
    for i in range(len(x)):
        current=x[i].lower()
        current=remove_punctuation(current)
        sentenceCleaned.append(current)
    return sentenceCleaned
    
    
def is_word(word):
    '''str->str or none
    Takes a string and checks if it is a word (does not contain symbols or numbers.)
    if conditions are met, returns the word. if not, returns none.
    '''
    if word.isalpha() and len(word)>=2:
        return word
    else:
        return None
def remove_punctuation(word):
    '''str->str
    Takes away all punctuation from a word.
    '''
    punct=string.punctuation
    result=""
    for char in word:
         if char not in punct:
             result=result+char
    return result
        
def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    query=query.split(" ")
    result={}
    if len(query)==1:
        try:
            return remove_punctuation(str((D[query[0]])))
        except KeyError:
            return False
    elif len(query)==2:
        try:
            return remove_punctuation(str(D[query[0]]&D[query[1]]))
        except KeyError:
            return None
    elif len(query)>1:
        try:
             result=D[query[0]]
             for i in range(1,len(query)):
                 result=result&D[query[i]]
             return remove_punctuation(str(result))
        except KeyError:
            return None


            
    
        

    

    

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=str(input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower())
query=remove_punctuation(query)
# YOUR CODE GOES HERE
while query !="q":
    lines=find_coexistance(d,query)
    if lines==None:
        print("Word "+query[0]+" not found in the file.")
    elif lines==False:
        print("Word "+query+" not found in the file.")
    else:
        print("The one or more words you entered coexisted in the following lines of the file:")
        print(lines)
    query=str(input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower())
    query=remove_punctuation(query)

