class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_head(self, data):
        self.head = Node(data, None)
        
    def add_node(self, data):
        # add next node here if head is the only node
        if self.head.next == None:
            self.head.next = Node(data, None)
        # else use while loop to look for node at the end
        else:
            curr = self.head.next
            while curr.next != None:
                curr = curr.next
            curr.next = Node(data, None)
    
    def print_all(self):
        n = self.head
        if n == None:
            print("No nodes added yet.")
        else:
            while n.next != None:
                print(n.data, end = " => ")
                n = n.next
            print(n.data)
            
    def get_last_node(self):
        n = self.head
        if n == None:
            print("No nodes added yet.")
        else:
            while n.next != None:
                n = n.next
            print(n.data)
            
ll = LinkedList()
ll.print_all()
ll.add_head(1)
ll.add_node(2)
ll.add_node(3)
ll.print_all()
ll.get_last_node()
