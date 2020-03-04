'''actual binary search algorithm
def binarySearch(l, target):
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
'''

class Binary():
    def __init__(self):
        '''initialize pointers, user control attributes'''
        
        self.heightl = [] # the list to be created for searching
    
        self.number = 100 # size of the list
        self.heightrect = 800 // self.number - 1.1 # width of each rect diplayed
    
        self.proceed = False # allow user to control each step of swap, if proceed, then perform swap
        self.fast = False # animation, sorting wihtout user control, intialize not animation
        self.reset = False # reset button
    
        # append all natural numbers in the list, in the range of the number of elements wanted to be sorted
        for i in range(self.number):
            self.heightl.append(int(random(1, 600 - 200))) # append a random number as the height of the rect
            # this is a unsorted list
            
        self.heightl.sort() # sort the height list before performing binary search
        self.targetindex = int(random(0, len(self.heightl) - 1)) # randomize a target
        self.target = self.heightl[self.targetindex]
        
        self.counter = 0 # initialize counter to be 0
        self.found = False # have not found the target
        
        self.left = 0 # left pointer is initialized to be 0
        self.right = len(self.heightl) - 1 # right pointer is initialized to be last element of the list
        self.midpoint = (self.left + self.right) // 2 # midpoint
            
    def buttons(self):
        # binary search text
        strokeWeight(0.5)
        textSize(30)
        fill(250, 235, 250)
        textMode(CENTER)
        text("Binary Search", 800 // 2 - 70, 150)
        
        fill(3, 232, 255) # show what the target is 
        text("Target: " + str(self.target), 400 - 70, 200)
        
        fill(0, 255, 0) # record the number of steps taken to reach the target
        text("Steps taken: " + str(self.counter), 400 - 70, 250)
        
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
        
    def display(self):
         # draw the rects, visualization    
        for n in range(self.number):
            if n == self.left or n == self.right: # color the left and right pointers green
                fill(0, 255, 0)
                
            elif n == self.targetindex:
                fill(3, 232, 255) # color the target blue
                
            elif n == self.midpoint:
                fill(255, 0, 0) # color the midpoint red
                
            else: # the rest rects are white
                fill(255)
            
            stroke(255, 0, 0)
            rectMode(CORNER)
            rect(n + n * self.heightrect, 600 - self.heightl[n], self.heightrect, self.heightl[n]) # draw all the rects
            
    def binarySearch(self):
        if self.left <= self.right and not self.found:
            self.midpoint = (self.left + self.right) // 2
            
            if self.heightl[self.midpoint] == self.target: # if the midpoint is the target, found it
                # return self.midpoint
                self.found = True # found it!
                self.counter += 1
                textMode(CORNER)
                textSize(40)
                fill(255)
                text("Finished", 50, 50)
                
            elif self.heightl[self.midpoint] < self.target: # if the midpoint is smaller than target, means target is in the right list
                self.counter += 1 # increment counter
                self.left = self.midpoint + 1 # move left pointer to the right of the midpoint
                self.midpoint = (self.left + self.right) // 2 # recalculate midpoint
                
                if not self.fast: # user control mode
                    self.proceed = False # stop execution
            
            elif self.heightl[self.midpoint] > self.target: # if the midpoint is bigger than target, means target is in the left list
                self.counter += 1 # increment counter
                self.right = self.midpoint - 1 # move right pointer to the left of the midpoint
                self.midpoint = (self.left + self.right) // 2 # recalculate midpoint
                
                if not self.fast: # user control mode
                    self.proceed = False # stop execution
        else:
            textMode(CORNER)
            textSize(40)
            fill(255)
            text("Finished", 50, 50)
            
            
    def run(self):
        '''main method to run bubble sort step by step'''
        if self.reset:
            Binary.reSet(self)    
            self.reset = False
            
            if self.fast: # if animation mode
                Binary.binarySearch(self) # pass in True, animated sorting 
            
            else: # if user control mode
                if self.proceed: # if user presses to proceed
                    Binary.binarySearch(self) # pass in False, setp-by-step sorting
            
        if self.fast: # if animation mode
            Binary.binarySearch(self) # pass in True, animated sorting 
            
            
        else: # if user control mode
            if self.proceed: # if user presses to proceed
                Binary.binarySearch(self) # pass in False, setp-by-step sorting
        
    def reSet(self):
        '''reset the entire list and start the program over'''
       
        self.heightl = [] # clear the content of the list
        # append all natural numbers in the list, in the range of the number of elements wanted to be sorted
        for i in range(self.number):
            self.heightl.append(random(1, 600 - 200)) # append a random number as the 600 of the rect
            # this is a new unsorted list
        
        self.heightl.sort()
        self.targetindex = int(random(0, len(self.heightl) - 1)) # randomize a target
        self.target = self.heightl[self.targetindex]
        
        self.counter = 0 # initialize counter to be 0
        self.found = False # have not found the target
        
        self.left = 0 # left pointer is initialized to be 0
        self.right = len(self.heightl) - 1 # right pointer is initialized to be last element of the list
        self.midpoint = (self.left + self.right) // 2 # midpoint
        
        self.proceed = False
        self.fast = False
    
    
    
    
    
