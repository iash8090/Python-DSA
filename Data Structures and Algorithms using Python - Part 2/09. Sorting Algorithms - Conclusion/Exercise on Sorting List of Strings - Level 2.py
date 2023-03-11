
def arrange_tickets(tickets_list):
    #Remove pass and write your logic here
    group=[]
    for i in range(1,21):
        if 'T'+str(i) in tickets_list:
            group.append('T'+str(i))
        else:
            if i<=10:
                group.append('V')
    print(group)

    g2=group[10:]
    print(g2)
    for index,i in enumerate(group):
        if i == 'V':
            group[index]=g2.pop(0)
    return group[:10]

tickets_list = ['T5','T7','T1','T2','T8','T15','T17','T19','T6','T12','T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)


'''
    group=[]
    for i in range(1,21):
        if 'T'+str(i) in tickets_list:
            group.append('T'+str(i))
        else:
            group.append('V')
    g1=group[:10]
    g2=group[10:]
    for i in g2:
        if i=='V':
            g2.remove(i)
    print(g2)
    for index,i in enumerate(g1):
        if i == 'V':
            g1[index]=g2.pop(0)
    return g1

'''
