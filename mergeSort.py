''' # actual merge sort algorithm
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
'''

class Merge():
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
