class Stack:
    def __init__(self):
        self.list = [] 
    
    def get_length(self):
        print(len(self.list))
        
    def push(self, elem):
        self.list.insert(0, elem)
        print(self.list)
    
    def pop(self):
        print(self.list.pop(0))
              
    def print_curr_elems(self):
        print(self.list)
        
new = Stack()
new.push(1)
new.push(2)
new.push(3)
new.pop()
new.print_curr_elems()
