class Mode():
    def __init__(self):
        '''flashing color of title, change color when clicked, drag down selection menu'''
        
    
    def interface(self):
        stroke(0)
        
        background(0)
        textMode(CENTER)
        textSize(25)
        fill(255)
        text("Visualizing Algorithms", width/2 - 100, height/2)
        
        fill(255)
        rectMode(CORNER)
        rect(100, 80, 150, 50, 10)
        textSize(20)
        fill(0)
        text("Sorting", 140, 110)
        
        # sorting dragdown menu
        fill(255)
        rect(100, 130, 150, 305)
        
        fill(0)
        rect(105, 135, 140, 45)
        fill(255)
        textSize(20)
        text("Bubble Sort", 115, 162)
        
        fill(0)
        rect(105, 185, 140, 45)
        fill(255)
        textSize(20)
        text("Selection Sort", 112, 210)
        
        fill(0)
        rect(105, 235, 140, 45)
        fill(255)
        text("Insertion Sort", 112, 262)
        
        fill(0)
        rect(105, 285, 140, 45)
        fill(255)
        text("Shell Sort", 125, 312)
        
        fill(0)
        rect(105, 335, 140, 45)
        fill(255)
        text("Merge Sort", 125, 362)
        
        fill(0)
        rect(105, 385, 140, 45)
        fill(255)
        text("Quick Sort", 125, 412)
        
        # searching menu
        fill(255)
        rect(350, 80, 150, 50, 10)
        textSize(20)
        fill(0)
        text("Searching", 380 ,110)
        
        fill(255)
        rect(350, 130, 150, 105)
        
        fill(0)
        rect(355, 135, 140, 45)
        fill(255)
        textSize(16)
        text("Sequential Search", 358, 161)
        
        
        fill(0)
        rect(355, 185, 140, 45)
        fill(255)
        textSize(20)
        text("Binary Search", 362, 214)
        
        fill(255)
        rect(600, 80, 150, 50, 10)
        fill(0)
        textSize(20)
        text("Graph", 645, 110)
        
        fill(255)
        rect(600, 130, 150, 105)
        
        fill(0)
        rect(605, 135, 140, 45)
        fill(255)
        textSize(25)
        text("BFS", 650, 165)
        
        fill(0)
        rect(605, 185, 140, 45)
        fill(255)
        textSize(25)
        text("DFS", 650, 215)
        
        
        
        
        
