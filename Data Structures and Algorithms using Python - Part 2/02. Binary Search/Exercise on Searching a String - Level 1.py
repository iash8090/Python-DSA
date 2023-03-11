

# Method 1 (Best)

def pattern_search(text, pattern):
    #Remove pass and write your logic here
    M = len(pattern)
    N = len(text)
    count = 0

    # A loop to slide pattern[] one by one
    for i in range(N - M + 1):
        j = 0
        while j < M:
            if (text[i + j] != pattern[j]):
                break
            j += 1

        if (j == M):
            count += 1
            j = 0
    return count


#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
print("The given text:",text)
print("Pattern:",pattern)
print("No. of occurrences of the pattern :",result)


# Method 2
'''
    n=len(pattern)
    l=[]
    count=0
    for i in range(0,len(text),n):
        x=text[i:i+n]
        if x==pattern:
            count+=1
        l.append(x)
    print(l)
    return count
'''
