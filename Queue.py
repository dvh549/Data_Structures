class Queue:
    def __init__(self):
        self.list = [] 
    
    def get_length(self):
        return self.len(list)
    
    def enqueue(self, elem):
        self.list.append(elem)
        print(self.list)
        
    def dequeue(self):
        print(self.list.pop(0))
        
    def print_curr_elems(self):
        print(self.list)
        
new = Queue()
new.enqueue(1)
new.enqueue(2)
new.enqueue(3)
new.dequeue()
new.print_curr_elems()
