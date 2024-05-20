def breadth_first_search(graph, start_vertex):
    visited = set()
    queue = [start_vertex]

    while queue:
        current_vertex = queue.pop(0)
        print(current_vertex, end=" ")
        
        for neighbour in graph.adjacency_list[current_vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)



def depth_first_search(graph, start_vertex):
    visited = set()
    stack = [start_vertex]

    while stack:
        current_vertex = stack.pop()
        print(current_vertex, end=" ")

        for neighbour in graph.adjacency_list[current_vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)