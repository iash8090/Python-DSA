
# Method 1
def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    unknown_words=[]
    l=text.split(" ")
    for i in l:
        if "." in i:
            i=i.replace(".","")
        if i not in vocabulary:
            unknown_words.append(i)
    if len(unknown_words) == 0:
        return -1
    return unknown_words

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)


# Method 2
'''
def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    unknown_words=[]
    l=text.split(" ")
    for i in l:
        if i not in vocabulary:
            if "." in i:
                i=i.replace(".","")
            unknown_words.append(i)
    if len(unknown_words) == 0:
        return -1
    return set(unknown_words)
'''