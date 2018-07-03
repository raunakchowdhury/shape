from queue import Queue

def breath_first_search(graph,starting_node,ending_node):
    queue = Queue()
    queue.enque(starting_node)
    shortest_path = []
    possible_paths = {}
    # If the possible nodes that the current node travels to are unique in possible_paths, add them in to the queue and dictionary
    while queue.length() != 0:
        current_node = queue.deque()
        for destination_node in graph[current_node]:
            if not destination_node in possible_paths.keys():
                possible_paths[destination_node] = current_node
                queue.enque(destination_node)
    #Traverse backwards through the dictionary, from the ending node to the starting node
    current_node = ending_node
    while current_node != starting_node:
        shortest_path.append(current_node)
        current_node = possible_paths[current_node]
    shortest_path.append(starting_node)
    shortest_path.reverse()
    return shortest_path


if __name__ == '__main__':
    graph = {
        'A':['B','C','D'],
        'B':['D'],
        'C':['E'],
        'D':['C','F'],
        'E':['F'],
        'F':['G'],
        'G':[]
    }
    print(breath_first_search(graph,'A','G'))
