class Bubble():
        
    def __init__(self):
        '''initialize pointers, user control attributes'''
        self.i = 0 # pointer for bubble sort, the biggest element, outside loop pointer
        self.j = 0 # second pointer for bubble sort, inside loop pointer
        self.heightl = [] # the list to be created for sorting
    
        self.number = 20 # number of rects I want to sort, modifiable by the user, width of each rect is dependent on this number
        self.heightrect = 800 // self.number - 2 # width of each rect diplayed
    
        self.proceed = False # allow user to control each step of swap, if proceed, then perform swap
        self.fast = False # animation, sorting wihtout user control, intialize not animation
        self.reset = False # reset button
    
        # append all natural numbers in the list, in the range of the number of elements wanted to be sorted
        for i in range(self.number):
            self.heightl.append(random(1, 600 - 200)) # append a random number as the height of the rect
            # this is a unsorted list
            
    def buttons(self):
        # bubble sort text
        textSize(30)
        fill(250, 235, 250)
        textMode(CENTER)
        text("Bubble Sort", 800 // 2 - 70, 150)
    
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
        
    def bubbleSort(self):
        '''bubble sort function, parameter fast determines whether the function will proceed automatically (animation mode) or step-by-step (user control mode)'''
        # doing one step of the loop, this is sorting the 600l frame by frame
        # initially, i and j are both set to be 0
        if self.heightl[self.j] >= self.heightl[self.j + 1]: # when i is 0, if two consecutive elements are out of order, switch them
            self.heightl[self.j], self.heightl[self.j + 1] = self.heightl[self.j + 1], self.heightl[self.j]
        
            if not self.fast: # if the parameter passed in is False, means user control mode
                self.proceed = False # set back to False after each step
                
        if self.i < len(self.heightl): # as long as outside loop pointer is smaller than the max number of elements
            self.j += 1 # increment j and compare the next pair
            
            if not self.fast: # user control mode
                self.proceed = False # stop execution
    
            if self.j >= len(self.heightl) - self.i - 1: # if all inside loop comparisons are done
                self.j = 0 # set inside loop pointer back to 0
                self.i += 1 # increment i
        
                if not self.fast: # user control mode
                    self.proceed = False # stop execution
                    
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
        
        self.proceed = False
        self.fast = False
        self.i = 0 # pointer for bubble sort, the biggest element, outside loop pointer
        self.j = 0 # second pointer for bubble sort, inside loop pointer
                
    def run(self):
        '''main method to run bubble sort step by step'''
        if self.reset:
            Bubble.reSet(self)    
            self.reset = False
            
            if self.fast: # if animation mode
                Bubble.bubbleSort(self) # pass in True, animated sorting 
            
            else: # if user control mode
                if self.proceed: # if user presses to proceed
                    Bubble.bubbleSort(self) # pass in False, setp-by-step sorting
            
        if self.fast: # if animation mode
            Bubble.bubbleSort(self) # pass in True, animated sorting 
            
            
        else: # if user control mode
            if self.proceed: # if user presses to proceed
                Bubble.bubbleSort(self) # pass in False, setp-by-step sorting
        
    def display(self):
        # draw the rects, visualization    
        for n in range(self.number):
            if n == self.j: # color the two elements being compared green and blue
                fill(0, 255, 0)
            elif n == self.j + 1:
                fill(0, 0, 255)
            else: # the rest rects are white
                fill(255)
            
            stroke(255, 0, 0)
            rectMode(CORNER)
            rect(n + n * self.heightrect, 600 - self.heightl[n], self.heightrect, self.heightl[n]) # draw all the rects
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
