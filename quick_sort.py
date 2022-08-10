# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the arr list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" arr relative to the pivot


def partition(l_index, r_index, arr):
    # Last element will be the pivot and the first element the pointer
    pivot_value = arr[r_index]
    new_p_index = l_index
    for i in range(l_index, r_index):
        if arr[i] <= pivot_value:
            # Swapping values smaller than the pivot to the front
            arr[i], arr[new_p_index] = arr[new_p_index], arr[i]
            new_p_index += 1
    # Finally swapping the last element with the pointer indexed number
    arr[new_p_index], arr[r_index] = arr[r_index], arr[new_p_index]
    return new_p_index
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.


def quicksort(l_index, r_index, arr):
    if len(arr) == 1:  # Terminating Condition for recursion. VERY IMPORTANT
        return arr
    if l_index < r_index:
        p_index = partition(l_index, r_index, arr)
        quicksort(l_index, p_index-1, arr)  # Recursively sorting the left
        quicksort(p_index+1, r_index, arr)  # Recursively sorting the right
    return arr
 
 
example = [4, 5, 1, 2, 3]
result = [1, 2, 3, 4, 5]
print(quicksort(0, len(example)-1, example))
 
example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
result = [1, 2, 2, 4, 4, 5, 6, 6, 7, 8]
# As you can see, it works for duplicates too
print(quicksort(0, len(example)-1, example))




