class Graph():
    def __init__(self, size):
        self.adj_list = [[0] * size for i in range(size)]
        self.size = size
        
    def add_edge(self, origin, destination):
        if origin > self.size or destination > self.size or origin < 0 or destination < 0:
            print("Invalid Edge")
        else:
            self.adj_list[origin - 1][destination - 1] = 1
            self.adj_list[destination - 1][origin - 1] = 1
            
    def remove_edge(self, origin, destination):
        if origin > self.size or destination > self.size or origin < 0 or destination < 0:
            print("Invalid Edge")
        else:
            self.adj_list[origin - 1][destination - 1] = 0
            self.adj_list[destination - 1][origin - 1] = 0
            
    def display_adj_list(self):
        for row in self.adj_list:
            for col in row:
                print(col, end=" ")
            print()
                
graph = Graph(3)
graph.display_adj_list()
graph.add_edge(3, 5)
graph.remove_edge(7, 7)
graph.add_edge(1, 2)
graph.display_adj_list()
print()
graph.remove_edge(1, 2)
graph.display_adj_list()
