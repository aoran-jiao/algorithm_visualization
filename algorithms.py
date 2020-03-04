class algorithm():
    '''a user reference template for original algorithms'''
    def bubbleSort(self, l):
        '''for loop in for loop directly'''
        for n in range(len(l) - 1): # keep doing the iteration
            for i in range(len(l) - 1 - n): # one short of the length of the list, "- n" excludes the last largest elements already sorted
                if l[i] > l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i] # fancy python swapping
                    # print(l) # show the result of each iteration

        return l
    
    def selectionSort(self, l):
        '''find the largest element --> selection sort --> for loop within a for loop'''
        for i in range(len(l) - 1, 0, -1): # start at the last element and move backward, can stop at the first element because the first one must be in order 

        # find the largest element within range i
  
            indexlargest = 0 # initialize the index of the largest element to be 0, update later
  
            for k in range(i + 1):
                if l[k] > l[indexlargest]: # if there is a larger element
                    indexlargest = k

            l[indexlargest], l[i] = l[i], l[indexlargest] # swap the largest element and the edge element

            # print(l) # print the result of each iteration

        return l 
        
    def insertionSort(self, l):
        # while loop within for loop --> insertion sort
        for i in range(0, len(l) - 1):
            check = l[i + 1] # the next element in the list to check
            while i >= 0 and check < l[i]: # check is smaller than the previous element
                l[i], l[i + 1] = l[i + 1], l[i] # swap the two adjacent elements
                i -= 1 # decrement i by 1

                # print(l) # print out the result of each step 

        return l # return the final result
    
    def shellSort(self, alist):
        sublistcount = len(alist)//2 # initialize the number of sublists to be half of the length of the list
        while sublistcount > 0:

            for startposition in range(sublistcount):
                gapInsertionSort(alist,startposition,sublistcount)
                # sort each sublist using insertion sort with a gap

            # print("gapsize:",sublistcount, "state of list:",alist)

            sublistcount = sublistcount // 2 # really important step, decrease the number of sublists by 2
    
    def gapInsertionSort(self, alist, start, gap):
        # basically an insertion sort with gaps
        # while loop within a for loop --> insertion sort
        for i in range(start+gap,len(alist),gap):

            currentvalue = alist[i]
            position = i

            while position>=gap and alist[position-gap]>currentvalue:
                alist[position]=alist[position-gap]
                position = position-gap

            alist[position]=currentvalue
            
    def mergeSort(self, alist):
        # basecase   
        if len(alist) < 2: # unsplittable length of 1 or 2
            return # halt the function and return to its calling function
  
        # split lists
        lefthalf = alist[: len(alist) // 2]
        righthalf = alist[len(alist)// 2: ]

        # recursive steps
        print("left", lefthalf) # print out the current result of the left list
        mergeSort(lefthalf)

        print("right", righthalf) # print out the current result of the right list
        mergeSort(righthalf)

        # merge Step 
        i = 0 # index in the original list
        ri, li = 0, 0 # right-index; left-index, pointers on the right and left list

        while li < len(lefthalf) and ri < len(righthalf):
            if lefthalf[li] < righthalf[ri]:
                alist[i]=lefthalf[li]
                li = li + 1
            else:
                alist[i]=righthalf[ri]
                ri = ri + 1
    
            i = i + 1 # increment the pointer of the original list by 1
    
        while li < len(lefthalf):
            alist[i]=lefthalf[li]
            li = li + 1
            i = i + 1

        while ri < len(righthalf):
            alist[i]=righthalf[ri]
            ri = ri + 1
            i = i + 1
  
        print("Merging ",alist)
        
    def quickSort(self, l, starti, endi):
        if starti >= endi: # if start index is smaller than end index
            return # end the function
    
        index = partition(l, starti, endi)
        delay(100)
        quickSort(l, starti, index - 1) # recursive sort list before the pivot
        quickSort(l, index + 1, endi) # recursive sort list after the pivot
  
    def partition(self, l, starti, endi):
        # partition function to recursively apply to quicksort
        pivotIndex = starti # choose a pivot, initialize the pivot index to be 0
        pivotValue = l[endi] # choose the pivot to be the last element of the list
    
        for i in range(starti, endi): # loop through the start to end and increment pivotIndex
            if l[i] < pivotValue: # if a specific element in the list is smaller than the pivot value
                l[i], l[pivotIndex] = l[pivotIndex], l[i]
                pivotIndex += 1
            
        l[pivotIndex], l[endi] = l[endi], l[pivotIndex] # swap the pivotValue to its rightful place
        return pivotIndex # return the index of the pivot for divide and conquer in recursion
        
    def binarySearch(self, l):
        # binary search function using left, right pointers
        first = 0 # left pointer is index 0
        last = len(l) - 1 # last pointer is index 1
        found = False # initialize, has not found the target 
        counter = 0 # record how many times midpoints are checked

        while first <= last and found == False: # if first pointer is to the right of the last pointer, or the value is found, break the while loop
            midpoint = (first + last) // 2 # middle value (round down)
            counter += 1

            if l[midpoint] == target: # if the target is found
                found = True
                return [midpoint, counter]  # return its index and the number of iterations

            elif l[midpoint] > target: # middle element is bigger than target, target is in the previous list
                last = midpoint - 1 # move the last pointer to the left of the midpoint

            elif l[midpoint] < target: # middle element is smaller than target, target is in the following list
                first = midpoint + 1 # move the first pointer to the right of the midpoint

        return [-1, counter] # return not found if target is not in the list

        
