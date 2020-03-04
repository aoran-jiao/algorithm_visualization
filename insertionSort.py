''' # actual insertion sort algorithm
def insertionSort(l):
  # while loop within for loop --> insertion sort
  for i in range(0, len(l) - 1):
    check = l[i + 1] # the next element in the list to check
    while i >= 0 and check < l[i]: # check is smaller than the previous element
      l[i], l[i + 1] = l[i + 1], l[i] # swap the two adjacent elements
      i -= 1 # decrement i by 1

    print(l) # print out the result of each step 

  return l # return the final result
'''

class Insertion():
        
    def __init__(self):
        '''initialize pointers, user control attributes'''
        self.i = 0 # inner loop pointer for insertion sort, comparing down one by one
        self.j = 0 # outer loop pointer for insertion sort, the "boarder of the leading sorted sublist"
        self.heightl = [] # the list to be created for sorting
    
        self.number = 20 # number of rects I want to sort, modifiable by the user, 800 of each rect is dependent on this number
        self.heightrect = 800 // self.number - 2 # width of each rect diplayed
    
        self.proceed = False # allow user to control each step of swap, if proceed, then perform swap
        self.fast = False # animation, sorting wihtout user control, intialize not animation
        self.reset = False # reset button
    
        # append all natural numbers in the list, in the range of the number of elements wanted to be sorted
        for i in range(self.number):
            self.heightl.append(random(1, 600 - 200)) # append a random number as the height of the rect
            # this is a unsorted list
            
    def buttons(self):
        # insertion sort text
        textSize(30)
        fill(250, 235, 250)
        textMode(CENTER)
        text("Insertion Sort", 800 // 2 - 70, 150)
    
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
        
    def insertionSort(self):
        '''bubble sort function, parameter fast determines whether the function will proceed automatically (animation mode) or step-by-step (user control mode)'''
        # doing one step of the loop, this is sorting the heightl frame by frame
        # initially, i and j are both set to be 0
        
        if self.j >= 0 and self.j < len(self.heightl): # as long as j is in the list
            check = self.heightl[self.i + 1] # this is the next element to check
            
            if self.i >= 0 and check < self.heightl[self.i]: # if reverse order
                self.heightl[self.i], self.heightl[self.i + 1] = self.heightl[self.i + 1], self.heightl[self.i] # switch in position
                
                self.i -= 1 # decrement inner loop pointer
                
            else:  
                if not self.fast: # user control mode
                    self.proceed = False # stop execution
                    
                self.j += 1 # increment outer loop pointer
                self.i = self.j - 1 # the inner loop poiner is reset 
                    
        else: # previous conditions no longer satisfies, means the list is sorted
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
            
        self.i = 0 # inner loop pointer for insertion sort, comparing down one by one
        self.j = 0 # outer loop pointer for insertion sort, the "boarder of the leading sorted sublist"
        
        self.proceed = False
        self.fast = False
       
    def run(self):
        '''main method to run insertion sort step by step'''
        if self.reset:
            Insertion.reSet(self)    
            self.reset = False
            
            if self.fast: # if animation mode
                Insertion.insertionSort(self) # pass in True, animated sorting 
            
            else: # if user control mode
                if self.proceed: # if user presses to proceed
                    Insertion.insertionSort(self) # pass in False, setp-by-step sorting
            
        if self.fast: # if animation mode
            Insertion.insertionSort(self) # pass in True, animated sorting 
            
            
        else: # if user control mode
            if self.proceed: # if user presses to proceed
                Insertion.insertionSort(self) # pass in False, setp-by-step sorting
        
    def display(self):
        # draw the rects, visualization    
        for n in range(self.number):
            if n == self.i: # color inner loop pointer green
                fill(0, 255, 0)
            elif n == self.j: # color the outer loop pointer red
                fill(255, 0, 0)
            else: # the rest rects are white
                fill(255)
            
            stroke(255, 0, 0)
            rectMode(CORNER)
            rect(n + n * self.heightrect, 600 - self.heightl[n], self.heightrect, self.heightl[n]) # draw all the rects
        
