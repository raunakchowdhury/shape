import heapq as hq

selection_list = [5, 4, 3, 2, 1]
insertion_list = [5, 4, 3, 2, 1]
merged_list = [5, 4, 3, 2, 1]
quick_list = [5, 4, 3, 2, 1]
heap_list = [5, 4, 3, 2, 1]


def selection_sort(unsorted_list):
    minimum = unsorted_list[0]
    index_of_min = 0
    returned_list = []
    while len(unsorted_list) != 0:
        for number in range(len(unsorted_list)):
            current_element = unsorted_list[number]
            if minimum > current_element:
                minimum = current_element
                index_of_min = number
        returned_list.append(minimum)
        unsorted_list.pop(index_of_min)
        index_of_min = 0
        if len(unsorted_list) != 0:
            minimum = unsorted_list[0]
    return returned_list


def insertion_sort(unsorted_list):
    partition = 0
    while partition != len(unsorted_list):
        if partition == 0:
            if unsorted_list[1] < unsorted_list[0]:
                unsorted_list[1], unsorted_list[0] = unsorted_list[0], unsorted_list[1]
        else:
            index = partition
            bubbling_index = index - 1
            while bubbling_index != -1:
                if unsorted_list[index] < unsorted_list[bubbling_index]:
                    unsorted_list[index], unsorted_list[bubbling_index] = unsorted_list[bubbling_index], unsorted_list[index]
                else:
                    break
                bubbling_index -= 1
                index -= 1
        partition += 1
    return unsorted_list  # list is now sorted


def merge(array1, array2):
    merged_list = []
    while len(array1) != 0 and len(array2) != 0:
        element1, element2 = array1[0], array2[0]
        if array1[0] < array2[0]:
            merged_list.append(array1[0])
            array1.pop(0)
        elif array2[0] < array1[0]:
            merged_list.append(array2[0])
            array2.pop(0)
        else:
            merged_list.append(array1[0])
            merged_list.append(array2[0])
            array1.pop(0)
            array2.pop(0)
    if len(array1) == 0:
        merged_list += array2
    if len(array2) == 0:
        merged_list += array1
    return merged_list


def merge_sort(unsorted_list):
    if len(unsorted_list) != 1:
        left_list = unsorted_list[:len(unsorted_list) // 2]
        right_list = unsorted_list[len(unsorted_list) // 2:]
        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)
        unsorted_list = merge(left_list, right_list)
    return unsorted_list


def median(num1, num2, num3):
    if num1 < num2 < num3 or num3 < num2 < num1:
        return num2
    elif num2 < num1 < num3 or num3 < num1 < num2:
        return num1
    else:
        return num3

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def heap_sort(unsorted_list):
    hq.heapify(unsorted_list)
    sorted_list = []
    while(len(unsorted_list) != 0):
        sorted_list.append(hq.heappop(unsorted_list))
    return sorted_list
'''
def partition(input_list,start,end):
    pivot = median(input_list[start], input_list[(start + end) // 2], input_list[end])
    pivot_pointer = input_list.index(pivot)
    input_list[pivot_pointer], input_list[end] = input_list[end], input_list[pivot_pointer]
    #beginning_pointer = start
    ending_pointer = end - 1  # pivot will be placed at end of list
    beginning_pointer = start
    while beginning_pointer != ending_pointer:
        #print(input_list[beginning_pointer])
        #print(pivot)
        #break
        while input_list[beginning_pointer] < pivot and beginning_pointer != ending_pointer:
            beginning_pointer += 1
        while input_list[ending_pointer] > pivot and beginning_pointer != ending_pointer:
            ending_pointer -= 1
        if input_list[ending_pointer] <= pivot and input_list[beginning_pointer] >= pivot:
            input_list[beginning_pointer], input_list[ending_pointer] = input_list[ending_pointer], input_list[beginning_pointer]

    input_list[end], input_list[ending_pointer+1] = input_list[ending_pointer+1], input_list[end]
    return ending_pointer + 1'''

print(partition([4,2,1,5,4],0,4))

def quick_sort(unsorted_list):
    return quick_sort_helper(unsorted_list,0,len(unsorted_list)-1)

def quick_sort_helper(unsorted_list, start, end):
    if start < end:
        pivot_pos = partition(unsorted_list,start,end)
        print(unsorted_list)
        quick_sort_helper(unsorted_list,start,pivot_pos-1)
        quick_sort_helper(unsorted_list,pivot_pos+1,end)
    print(unsorted_list)
    return unsorted_list

    # def iterative_merge_sort(unsorted_list):

if __name__ == '__main__':
    selection_list = selection_sort(selection_list)
    insertion_list = insertion_sort(insertion_list)
    merged_list = merge_sort(merged_list)
    quick_list = quick_sort(quick_list)
    heap_list = heap_sort(heap_list)

    print("Selection sort: " + str(selection_list))
    print("Insertion sort: " + str(insertion_list))
    print("Merge sort: " + str(merged_list))
    print("Quick sort:", quick_list)
    print("Heap sort:", heap_list)
