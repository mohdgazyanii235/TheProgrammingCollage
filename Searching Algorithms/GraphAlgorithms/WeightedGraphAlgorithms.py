import heapq
from WeightedGraph import WeightedGraph


'''
    Goal: Find the shortest paths between a given source vertex and all the other vertices in a weighted graph.
    Explanation:

        5
   A --------- B
 /  \           \\
3     7           8
 \   /             \\
   C ----- 2 -----   D
     \             /
       6         /
         \     /
            E   

    1) Initialise a dictionary {A: 0, B: inf, C: inf, D: inf, E: inf}.
    2) Add (0, A) to a priority queue [].
    3) dequeue the vertex with the minimum distance from the priority queue: (0, A)
    4) Update the distances of A's neighbors (B and C) in the distances dictionary and enqueue them in the priority queue:
        distances = {A: 0, B: 5, C: 3, D: inf, E: inf}
        priority_queue = [(3, C), (5, B)]
    5) dequeue the vertex with the minimum distance from the priority queue: (3, C)
    6) Update the distance of C's neighbor (E) in the distances dictionary and enqueue it in the priority queue:
        distances = {A: 0, B: 5, C: 3, D: 13, E: 9}
        priority_queue = [(9, E)]
    7) Dequeue the vertex with the minimum distance from the priority queue: (9, E)
    8) Update the distance of E's neighbor (D) in the distances dictionary and enqueue it in the priority queue:
        distances = {A: 0, B: 5, C: 3, D: 11, E: 9}
        priority_queue = []
    9) Sice priority_queue is now empty, the algorithm terminates
'''
def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph.adjacency_list}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue
        
        for neighbour, weight in graph.adjacency_list[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priority_queue, (distance, neighbour))
    
    return distances


def bellman_ford(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph.adjacency_list}
    distances[start_vertex] = 0

    for _ in range(len(graph.adjacency_list) - 1):
        for vertex in graph.adjacency_list:
            for neighbour, weight in graph.adjacency_list[vertex]:
                if distances[vertex] + weight < distances[neighbour]:
                    distances[neighbour] = distances[vertex] + weight

    for vertex in graph.adjacency_list:
        for neighbour, weight in graph.adjacency_list[vertex]:
            if distances[vertex] + weight < distances[neighbour]:
                print("Negative cycle detected")
                return None

    return distances



adjaency_list = {'a': [('b', 1), ('e', 2)],
                 'b': [('a', 1), ('c', 1), ('e', 2)],
                 'c': [('b', 1), ('d', 2)],
                 'd': [('c', 2)],
                 'e': [('a', 2), ('b', 2), ('f', 3)],
                 'f': [('e', 3)]}

graph = WeightedGraph(adjaency_list)

print(dijkstra(graph, 'a'))
print(bellman_ford(graph, 'a'))
