
def make_change(denomination_list, amount):
    '''Remove pass and implement the Greedy approach to make the change for the amount using the currencies in the denomination list.
    The function should return the total number of notes needed to make the change. If change cannot be obtained for the given amount, then return -1. Return 1 if the amount is equal to one of the currencies available in the denomination list.  '''
    global coins
    coins=[]
    denomination_list.sort(reverse=True)
    if amount in denomination_list:
        coins.append(amount)
        return 1
    else:
#        while sum(coins)!=amount:
        for coin in denomination_list:
            while amount>=coin:
                coins.append(coin)
                amount-=coin
            if amount==0:
                break
        if amount!=0:
            return -1
        return len(coins)


#Pass different values to the function and test your program
amount= 15
denomination_list = [10,1,3]
print("no. of coins needed- ",make_change(denomination_list, amount))
print("value of coins- ",coins)
