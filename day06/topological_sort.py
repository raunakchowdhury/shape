from queue import Queue

# returns a dictionary containing the # of incoming edges for each node
def incoming_edges(dictionary):
    indegree_count = {key: 0 for key in dictionary}
    for key in dictionary.keys():
        for entry in dictionary[key]:
            indegree_count[entry] += 1
    return indegree_count


def topological_sort(dictionary):
    indegree_count = incoming_edges(dictionary)
    queue = Queue()
    returned_sort = []
    for key in indegree_count:
        if indegree_count[key] == 0:
            queue.enque(key)

    while queue.length() != 0:
        current_queue_element = queue.deque()
        for node in dictionary[current_queue_element]:
            indegree_count[node] -= 1
            if indegree_count[node] == 0:
                queue.enque(node)
        returned_sort.append(current_queue_element)
    return returned_sort



if __name__ == '__main__':
    directed_acyclic_graph = {
        'A':['B','C'],
        'B':['D','E'],
        'C':['D','E'],
        'D':['E'],
        'E': []
    }
    print(topological_sort(directed_acyclic_graph))
    #reversed graph
    directed_acyclic_graph = {
        'E':['C','D','B'],
        'D':['B','C'],
        'C':['A'],
        'B':['A'],
        'A':[]
    }
    print(topological_sort(directed_acyclic_graph))
