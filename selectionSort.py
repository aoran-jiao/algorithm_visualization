''' # actual selection sort
def selectionSort(l):
  # find the largest element --> selection sort --> for loop within a for loop
  for i in range(len(l) - 1, 0, -1): # start at the last element and move backward, can stop at the first element because the first one must be in order 

    # find the largest element within range i
  
    indexlargest = 0 # initialize the index of the largest element to be 0, update later
  
    for k in range(i + 1):
      if l[k] > l[indexlargest]: # if there is a larger element
        indexlargest = k

    l[indexlargest], l[i] = l[i], l[indexlargest] # swap the largest element and the edge element

    print(l) # print the result of each iteration

  return l 
'''

class Selection():
        
    def __init__(self):
        '''initialize pointers, user control attributes'''
        
        self.heightl = [] # the list to be created for sorting
        self.number = 20 # number of rects I want to sort, modifiable by the user, 800 of each rect is dependent on this number
        self.heightrect = 800 // self.number - 2 # 800 of each rect diplayed
    
        self.proceed = False # allow user to control each step of swap, if proceed, then perform swap
        self.fast = False # animation, sorting wihtout user control, intialize not animation
        self.reset = False # reset button
    
        # append all natural numbers in the list, in the range of the number of elements wanted to be sorted
        for i in range(self.number):
            self.heightl.append(random(1, 600 - 200)) # append a random number as the 600 of the rect
            # this is a unsorted list
         
        self.i = len(self.heightl) - 1 # outside loop pointer, start from the last element and moving forward
        self.indexlargest = 0 # find the largest index within the range of i
        self.k = 0 # the pointer of the inside loop, find the largest element
        
    def buttons(self):
        # selection sort text
        textSize(30)
        fill(250, 235, 250)
        textMode(CENTER)
        text("Selection Sort", 800 // 2 - 70, 150)
    
        # buttons
        fill(255)
        stroke(100) 
        triangle(800 // 2 + 50, 50, 800 // 2 + 50, 80, 800 // 2 + 80, 65) # forward button
        triangle(800 // 2 - 50, 50, 800 // 2 - 50, 80, 800 // 2 - 80, 65) # backward button
    
        # this is animation button, directly finishes the sorting without user interference
        noStroke()
        triangle(800 // 2 + 120, 50, 800 // 2 + 120, 80, 800 // 2 + 135, 65)
        triangle(800 // 2 + 130, 50, 800 // 2 + 130, 80, 800 // 2 + 145, 65)
    
        # this is a pause button
        rectMode(CENTER)
        if not self.fast:
            fill(255, 0, 0)
        rect(800 // 2, 65, 30, 30)
        
        # this is a reset button
        fill(255)
        rectMode(CENTER)
        rect(800 - 100, 65, 60, 40, 5)
        
        textSize(16)
        textMode(CENTER)
        fill(0)
        text("RESET", 800 - 123, 70)
        
        # this is a back button
        fill(255)
        rectMode(CENTER)
        rect(100, 85, 60, 40, 30)
        fill(0)
        textSize(16)
        textMode(CENTER)
        text("BACK", 80, 90)
        
    def selectionSort(self):
        '''selection sort function, parameter fast determines whether the function will proceed automatically (animation mode) or step-by-step (user control mode)'''
        # doing one step of the loop, this is sorting the heightl frame by frame
        # i = outer loop pointer, decrementing; k = inner loop poiner, looking for largest value, incrementing
        
        if self.k <= self.i: # as long as k is within the range of i
            if self.heightl[self.k] > self.heightl[self.indexlargest]: # find a larger element than the current largest
                self.indexlargest = self.k # update the current largest number
            
            self.k += 1 # increment k to search for larger value
            
        if self.k > self.i: # if k is bigger than i, means finished searching for the sublist within i, signal to swap elements, the current largest element to the top of the list
            self.heightl[self.indexlargest], self.heightl[self.i] = self.heightl[self.i], self.heightl[self.indexlargest]
            
            if not self.fast: # user control mode
                    self.proceed = False # stop execution every time the swap is performed
                           
            if self.i > 0: # as long as i is still in the list
                self.i -= 1 # decrement i
                self.k = 0 # reinitialize k and indexlargest to 0 for next iteration
                self.indexlargest = 0 
            
        if self.i <= 0: # i goes to the start of the list, means the list is sorted
            textMode(CORNER)
            textSize(40)
            fill(255)
            text("Finished", 50, 50)
            # noLoop()
        
    def reSet(self):
        '''reset the entire list and start the program over'''
       
        self.heightl = [] # clear the content of the list
        # append all natural numbers in the list, in the range of the number of elements wanted to be sorted
        for i in range(self.number):
            self.heightl.append(random(1, 600 - 200)) # append a random number as the 600 of the rect
            # this is a new unsorted list
                
        self.i = len(self.heightl) - 1 # outside loop pointer, start from the last element and moving forward
        self.indexlargest = 0 # find the largest index within the range of i
        self.k = 0 # the pointer of the inside loop, find the largest element
        
        self.proceed = False
        self.fast = False
        
    def run(self):
        '''main method to run selection sort step by step'''
        if self.reset:
            Selection.reSet(self)    
            self.reset = False
            
            if self.fast: # if animation mode
                Selection.selectionSort(self) # pass in True, animated sorting 
            
            else: # if user control mode
                if self.proceed: # if user presses to proceed
                    Selection.selection(self) # pass in False, setp-by-step sorting
            
        if self.fast: # if animation mode
            Selection.selectionSort(self) # pass in True, animated sorting 
            
            
        else: # if user control mode
            if self.proceed: # if user presses to proceed
                Selection.selectionSort(self) # pass in False, setp-by-step sorting
        
    def display(self):
        # draw the rects, visualization    
        for n in range(self.number):
            if n == self.i : # outer loop pointer yellow
                fill(255, 255, 0)
                
            elif n == self.k: # inner loop pointer green
                fill(0, 255, 0)
                
            else: # the rest rects are white
                fill(255)
            
            stroke(255, 0, 0)
            rectMode(CORNER)
            rect(n + n * self.heightrect, 600 - self.heightl[n], self.heightrect, self.heightl[n]) # draw all the rects
        
