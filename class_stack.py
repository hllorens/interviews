class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


class Stack:
    # head is default NULL
    def __init__(self):
        self.head = None
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    # Method to add data to the stack
    # adds to the start of the stack
    def push(self,data):
        if self.isempty():
            self.head=Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    # Remove element that is the current head (start of the stack)
    def pop(self):
        if self.isempty():
            return None
        else:
            # Removes the head node and makes 
            #the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
    # Returns the head node data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    # Prints out the stack     
    def display(self):
        iternode = self.head
        if self.isempty():
            print("[]")
        else:
            while(iternode != None):
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            print(f'\n\n')
            return


s=Stack()
s.display()
s.push('1')
s.display()
print('poping: '+s.pop())
s.display()
s.push('1')
s.display()
print()
s.push('2')
s.push('3')
s.display()
