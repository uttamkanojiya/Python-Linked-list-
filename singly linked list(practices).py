#undersTANDING THE CONCEPT of linkedlist
class Node():
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist():
    def __init__(self):
        self.head = None

    def printll(self):
        if self.head is not None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                #if self.head is None:
                #   print("Null")
                n=n.ref

    def add_begin(self,data):
        new_node = Node(self)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(self)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node

    #def add_at_index(self):
        
            
LL=Linkedlist()
LL.add_begin(100)
LL.add_end(200)
LL.add_begin(300)
LL.add_end(400)
LL.printll()
            
