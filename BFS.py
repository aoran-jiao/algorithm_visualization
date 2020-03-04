class cell: 
    '''create a cell object (vertex)'''
    def __init__(self, x = 0, y = 0, dist = 0): 
        self.x = x 
        self.y = y 
        self.dist = dist 

class bfs():        
    # checks whether given position is  
    # inside the board 
    
    def __init__(self):
        pass
        
    def buttons(self):
        pass
        
    def display(self):
        pass
        
        
    def isInside(x, y): 
        if (x >= 1 and x <= 8 and 
            y >= 1 and y <= 8):  
            return True
        return False
        
    # Method returns minimum step to reach 
    # target position; our BFS function  
    def BFS(knightpos, targetpos): 
        
        #all possible movments for the knight 
        # this is essentially adding all the vertices
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2] 
        
        queue = [] # create a queue, First In First Out (FIFO)
        
        # push starting position of knight 
        # with 0 distance 
        queue.append(cell(knightpos[0], knightpos[1], 0)) 
        # make all cell unvisited  
        visited = [[False for i in range(9)]  
                        for j in range(9)] 
        
        # visit starting state 
        visited[knightpos[0]][knightpos[1]] = True
        
        # loop untill we have one element in queue  
        while(len(queue) > 0): 
            
            t = queue[0] 
            queue.pop(0) 
            
            # if current cell is equal to target  
            # cell, return its distance  
            if(t.x == targetpos[0] and 
            t.y == targetpos[1]): 
                return t.dist 
                
            # iterate for all reachable states  
            for i in range(8): 
                
                x = t.x + dx[i] 
                y = t.y + dy[i] 
                
                if(isInside(x, y) and not visited[x][y]): 
                    visited[x][y] = True
                    queue.append(cell(x, y, t.dist + 1)) 
'''
knightpos = [int(x) for x in input().split()] 
targetpos = [int(x) for x in input().split()]
print(BFS(knightpos, targetpos)) 

'''            
            
            
