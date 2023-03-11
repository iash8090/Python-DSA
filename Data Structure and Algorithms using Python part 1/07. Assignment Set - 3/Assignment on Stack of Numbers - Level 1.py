
class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        if (self.__top == self.__max_size - 1):
            return True
        return False

    def is_empty(self):
        if (self.__top == -1):
            return True
        return False

    def push(self, data):
        if (self.is_full()):
            print("The stack is full!!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if (self.is_empty()):
            print("The stack is empty!!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if (self.is_empty()):
            print("The stack is empty")
        else:
            index = self.__top
            while (index >= 0):
                print(self.__elements[index])
                index -= 1

    def get_max_size(self):
        return self.__max_size

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__top
        while (index >= 0):
            msg.append((str)(self.__elements[index]))
            index -= 1
        msg = " ".join(msg)
        msg = "Stack data(Top to Bottom): " + msg
        return msg

# Method 1
def change_smallest_value(number_stack):
    # write your logic here
    l=[]
    while not number_stack.is_empty():
        l.append(number_stack.pop())
    x=min(l)
    for i in l:
        if i == x:
            number_stack.push(i)
            l.remove(i)
    for i in l[::-1]:
            number_stack.push(i)
    return number_stack


# Add different values to the stack and test your program
number_stack = Stack(8)
number_stack.push(154)
number_stack.push(12)
number_stack.push(121)
number_stack.push(12)
number_stack.push(128)
number_stack.push(12)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()




# Method 2
'''
def change_smallest_value(number_stack):
    # write your logic here
    l=[]
    while not number_stack.is_empty():
        l.append(number_stack.pop())
    x=min(l)
    y=l.count(x)
    for i in range(y):
        number_stack.push(x)
        l.remove(x)
    print(l)
    for i in reversed(l):
            number_stack.push(i)
    return number_stack
'''


# Method 3
'''
def change_smallest_value(number_stack):
    l=[]
    while(not number_stack.is_empty()):
        l.append(number_stack.pop())
    mini = min(l)
    counter = l.count(min(l))
    for i in range(counter):
        number_stack.push(mini)
    for element in l[::-1]:
        if element!=mini:
            number_stack.push(element)
    return number_stack 
'''