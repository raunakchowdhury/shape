selection_list = [5, 4, 3, 2, 1]
insertion_list = [5, 4, 3, 2, 1]
merged_list = [5, 4, 3, 2, 1]


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
    pointer1, pointer2 = 0, 0
    merged_list = []
    while len(array1) != 0 and len(array2) != 0:
        element1, element2 = array1[pointer1], array2[pointer2]
        if array1[pointer1] < array2[pointer2]:
            merged_list.append(array1[pointer1])
            array1.pop(pointer1)
        elif array2[pointer2] < array1[pointer1]:
            merged_list.append(array2[pointer2])
            array2.pop(pointer2)
        else:
            merged_list.append(array1[pointer1])
            merged_list.append(array2[pointer2])
            array1.pop(pointer1)
            array2.pop(pointer2)
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


# def iterative_merge_sort(unsorted_list):


selection_list = selection_sort(selection_list)
insertion_list = insertion_sort(insertion_list)
merged_list = merge_sort(merged_list)

print("Selection sort: " + str(selection_list))
print("Insertion sort: " + str(insertion_list))
print("Merge sort: " + str(merged_list))
#print(merge(selection_list, insertion_list))
