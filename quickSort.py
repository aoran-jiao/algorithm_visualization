'''actual quick sort algorithm
def quickSort(l, starti, endi):
    if starti >= endi: # if start index is smaller than end index
        return # end the function
    
    index = partition(l, starti, endi)
    delay(100)
    quickSort(l, starti, index - 1) # recursive sort list before the pivot
    quickSort(l, index + 1, endi) # recursive sort list after the pivot
  
def partition(l, starti, endi):
    # partition function to recursively apply to quicksort
    pivotIndex = starti # choose a pivot, initialize the pivot index to be 0
    pivotValue = l[endi] # choose the pivot to be the last element of the list
    
    for i in range(starti, endi): # loop through the start to end and increment pivotIndex
        if l[i] < pivotValue: # if a specific element in the list is smaller than the pivot value
            l[i], l[pivotIndex] = l[pivotIndex], l[i]
            pivotIndex += 1
            
    l[pivotIndex], l[endi] = l[endi], l[pivotIndex] # swap the pivotValue to its rightful place
    return pivotIndex # return the index of the pivot for divide and conquer in recursion
'''
