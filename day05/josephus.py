from queue import Queue

def josephus(n,k):
    queue = Queue()
    for each in range(1, n+1):
        queue.enque(each)
    while queue.length() != 1:
        for time in range(k-1):
            queue.enque(queue.deque())
        queue.deque() #permanenently take the element after the step out
    return queue.deque()

if __name__ == '__main__':
    numbers_people = [2,3,4,5,6,7,8,9,10]
    list_steps = [2,3,4,5]
    for number_people in numbers_people:
        for step in list_steps:
            print("Running Josephus length", number_people, "with", step, "step:", josephus(number_people,step))
