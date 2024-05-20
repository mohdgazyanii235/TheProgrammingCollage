class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append((vertex2, weight))
            self.adjacency_list[vertex2].append((vertex1, weight))

    def remove_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].remove((vertex2, weight))
            self.adjacency_list[vertex2].remove((vertex1, weight))

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for neighbor, weight in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove((vertex, weight))
            del self.adjacency_list[vertex]

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex}: {self.adjacency_list[vertex]}")