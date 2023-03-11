'''
Here is a code that implements memory compaction process. Go through the below code and observe how linked list is used for its implementation. 

Execute and observe the result. 
'''


class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    #This method is added for this tryout alone
    def set_head(self,new_node):
        self.__head=new_node

    #This method is added for this tryout alone
    def set_tail(self,new_node):
        self.__tail=new_node

    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list") 
                                        
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


def find_total_nodes(mem_block):
    temp=mem_block.get_head()
    total_nodes=0
    while(temp is not None):
        total_nodes+=1
        temp=temp.get_next()

    return total_nodes

def maximum_contiguous_free_blocks(mem_block):
    temp=mem_block.get_head()
    total_nodes=find_total_nodes(mem_block)
    free_list=[]
    free_contiguous_nodes=0
    if(temp.get_data()=="Free"):
        free_contiguous_nodes+=1
    prev_data=temp.get_data()
    temp=temp.get_next()
    while(temp is not None):
        if(temp.get_data()=="Free"):
                if(prev_data=="Free"):
                    free_contiguous_nodes+=1
                else:
                    free_list.append(free_contiguous_nodes)
                    free_contiguous_nodes=1
        else:
            free_list.append(free_contiguous_nodes)
            free_contiguous_nodes=0

        prev_data=temp.get_data()
        temp=temp.get_next()
    free_list.append(free_contiguous_nodes)
    max_free_contiguous_nodes=max(free_list)
    return((max_free_contiguous_nodes/total_nodes)*100)

def total_free_blocks(mem_block):
    temp=mem_block.get_head()
    total_blocks=find_total_nodes(mem_block)
    total_free_blocks=0
    while(temp is not None):
        if(temp.get_data()=="Free"):
            total_free_blocks+=1
        temp=temp.get_next()
    return ((total_free_blocks/total_blocks)*100)

def memory_compaction(mem_block):
    temp=mem_block.get_head()
    prev_occupied=None
    prev_free=None
    occupied=None
    free=None
    if(temp.get_data()=="Occupied"):
            occupied=temp
            prev_occupied=temp
    elif(temp.get_data()=="Free"):
            free=temp
            prev_free=temp
    temp=temp.get_next()
    while(temp is not None):
        if(temp.get_data()=="Occupied"):
            if(occupied==None):
                occupied=temp
            if(prev_occupied==None):
                prev_occupied=temp
            else:
                prev_occupied.set_next(temp)
                prev_occupied=temp
        elif(temp.get_data()=="Free"):
            if(free==None):
                free=temp
            if(prev_free==None):
                prev_free=temp
            else:
                prev_free.set_next(temp)
                prev_free=temp
        temp=temp.get_next()

    prev_occupied.set_next(free)
    prev_free.set_next(None)
    mem_block.set_head(occupied)
    mem_block.set_tail(prev_free)

mem_block=LinkedList()
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Occupied")
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Occupied")
mem_block.add("Free")
mem_block.add("Free")
mem_block.add("Free")
mem_block.add("Free")

print("Before compaction")
print("_________________")
print("Max. contiguous free blocks:", maximum_contiguous_free_blocks(mem_block),"%")
print("Total free blocks:",total_free_blocks(mem_block),"%")

memory_compaction(mem_block)

print()
print("After compaction")
print("________________")
print("Max. contiguous free blocks:", maximum_contiguous_free_blocks(mem_block),"%")
print("Total free blocks:",total_free_blocks(mem_block),"%")
