import functools

arr=[2, -7, -2, -2, 0]

print(str(arr)+' unsorted oneliner')

def absSortOneLiner(arr):

  """

  @param arr: int[]

  @return: int[]

  """

  return sorted(arr,key=lambda x: (abs(x),x))



print(absSortOneLiner(arr))



def compare(x,y):

  if(abs(x)<abs(y) or (abs(x)==abs(y) and x < y)):

    return -1

  elif (abs(x)>abs(y) or (abs(x)==abs(y) and x > y)):

    return 1

  else:

    return 0

print(str(arr)+' unsorted com func')

print(sorted(arr,key=functools.cmp_to_key(compare)))



def mergeSort(myList):

    sorto=[]

    if len(myList) > 1:

        mid = len(myList) // 2

        left = myList[:mid]

        right = myList[mid:]



        # Recursive call on each half

        lefto=mergeSort(left)

        righto=mergeSort(right)





        # Two iterators for traversing the two halves

        i = 0

        j = 0

        

        # Iterator for the main list

        k = 0

        

        while i < len(lefto) and j < len(righto):

            if abs(lefto[i]) < abs(righto[j]) or (abs(lefto[i]) == abs(righto[j]) and lefto[i]<righto[j]):

              # The value from the left half has been used

              sorto.append(lefto[i])

              # Move the iterator forward

              i += 1

            else:

                sorto.append(righto[j])

                j += 1

            # Move to the next slot

            k += 1



        # For all the remaining values

        while i < len(lefto):

            sorto.append(lefto[i])

            i += 1

            k += 1



        while j < len(righto):

            sorto.append(righto[j])

            j += 1

            k += 1

    else:

        sorto=myList

    return sorto

#myList = [54,26,93,17,77,31,44,55,20]

print(str(arr)+' unsorted mergeSort value')

print(mergeSort(arr))



print(str(arr)+' unsorted mergeSort ref')

    

def mergeSort(myList):

    if len(myList) > 1:

        mid = len(myList) // 2

        left = myList[:mid]

        right = myList[mid:]



        # Recursive call on each half

        mergeSort(left)

        mergeSort(right)



        # Two iterators for traversing the two halves

        i = 0

        j = 0

        

        # Iterator for the main list

        k = 0

        

        while i < len(left) and j < len(right):

            if abs(left[i]) < abs(right[j]) or (abs(left[i]) == abs(right[j]) and left[i]<right[j]):

              # The value from the left half has been used

              myList[k] = left[i]

              # Move the iterator forward

              i += 1

            else:

                myList[k] = right[j]

                j += 1

            # Move to the next slot

            k += 1



        # For all the remaining values

        while i < len(left):

            myList[k] = left[i]

            i += 1

            k += 1



        while j < len(right):

            myList[k]=right[j]

            j += 1

            k += 1



#myList = [54,26,93,17,77,31,44,55,20]

myList=arr[:]

print(str(arr)+' unsorted after ref')

mergeSort(myList)

print(myList)


print(str(arr)+' unsorted')
