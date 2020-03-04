class Seq():
    '''Sequential search'''  
    def __init__(self):
        '''initialize pointers, user control attributes'''
        self.i = 0 # pointer for sequential search, index of the list
        
        self.heightl = [] # the list to be created for sorting
    
        self.number = 100 # number of rects I want to serach from, modifiable by the user, width of each rect is dependent on this number
        self.heightrect = 800 // self.number - 1.1 # width of each rect diplayed
    
        self.proceed = False # allow user to control each step of search, if proceed, then perform search
        self.fast = False # animation, sorting wihtout user control, intialize not animation
        self.reset = False # reset button
    
        # append all natural numbers in the list, in the range of the number of elements wanted to be sorted
        for i in range(self.number):
            self.heightl.append(random(1, 600 - 200)) # append a random number as the height of the rect
            # this is a unsorted list
            
        self.targetIndex = int(random(0, len(self.heightl) - 1)) # randomized target
        self.target = self.heightl[self.targetIndex]
        self.counter = 0 # initialize counter to be 0 
        
    def buttons(self):
        # sequential search text
        textSize(20)
        fill(250, 235, 250)
        textMode(CENTER)
        text("Sequential Search", 800 // 2 - 70, 120)
        
        fill(3, 232, 255)
        text("Target: " + str(self.target), 340, 150)
        
        fill(255, 255, 0)
        text("Steps counted: " + str(self.counter), 340, 180)
        
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
        
    def seqS(self):
        '''sequential search function, parameter fast determines whether the function will proceed automatically (animation mode) or step-by-step (user control mode)'''
        
        if self.heightl[self.i] != self.target: # simple traversal through the list
            self.i += 1
            self.counter += 1
            
            if not self.fast:
                self.proceed = False
            
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
        self.i = 0 # reset pointer
        self.targetIndex = int(random(0, len(self.heightl) - 1)) # randomized target
        self.target = self.heightl[self.targetIndex]
        self.counter = 0 # initialize counter to be 0 
                
    def run(self):
        '''main method to run bubble sort step by step'''
        if self.reset:
            Seq.reSet(self)    
            self.reset = False
            
            if self.fast: # if animation mode
                Seq.seqS(self) # pass in True, animated sorting 
            
            else: # if user control mode
                if self.proceed: # if user presses to proceed
                    Seq.seqS(self) # pass in False, setp-by-step sorting
            
        if self.fast: # if animation mode
            Seq.seqS(self) # pass in True, animated sorting 
            
            
        else: # if user control mode
            if self.proceed: # if user presses to proceed
                Seq.seqS(self) # pass in False, setp-by-step sorting
        
    def display(self):
        # draw the rects, visualization    
        for n in range(self.number):
            
            if n == self.targetIndex:
                fill(3, 232, 255)
                
            elif n == self.i: # color the two elements being compared green and blue
                fill(0, 255, 0)
                
            else: # the rest rects are white
                fill(255)
            
            stroke(255, 0, 0)
            rectMode(CORNER)
            rect(n + n * self.heightrect, 600 - self.heightl[n], self.heightrect, self.heightl[n]) # draw all the rects
