
def find_matches(country_name):
    #Remove pass and write your logic here
    l=[]
    for i in match_list:
        if country_name == i.split(':')[0]:
            l.append(i)
    return l

def max_wins():
    #Remove pass and write your logic here
    d={}
    for i in match_list:
        if i.split(':')[1] not in d.keys():
            d[i.split(':')[1]]=None
        if d[i.split(':')[1]] == None:
            d[i.split(':')[1]] = int(i.split(':')[3])
        elif d[i.split(':')[1]] >= 0:
            if d[i.split(':')[1]] < int(i.split(':')[3]):
                d[i.split(':')[1]] = int(i.split(':')[3])
    temp=d.copy()
    for key,value in d.items():
        d[key]=[]
    print(d)
    for i in match_list:
        if temp[i.split(':')[1]] == int(i.split(':')[3]) :
            d[i.split(':')[1]].append(i.split(':')[0])
    return d


def find_winner(country1,country2):
    #Remove pass and write your logic here
    count1=0
    count2=0
    l=[]
    for i in match_list:
        if country1 == i.split(':')[0]:
            count1 += int(i.split(':')[3])

    for i in match_list:
        if country2 == i.split(':')[0]:
            count2 += int(i.split(':')[3])
    if count1==count2:
        return "Tie"
    else:
        return country1 if count1>count2 else country2



#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()

print("Details of matches played by given country: ")
print(find_matches("AUS"))

print("\nChampionship and countries which won those:")
print(max_wins())


print("\nCountry which won max No. of matches in all formats:")
print(find_winner("AUS","IND"))
print(find_winner("PAK","SA"))
