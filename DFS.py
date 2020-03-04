# Processing sketch to demonstrate CCC Knight Hop 2008 J5

# We can't use standard recursion - if we do once we kick off the function
# it doesn't return until the answer is reached and the screen won't be 
# updated until the answer is derived.

# Instead this sketch uses it's own recursion by using a list for a stack.
# Each time the draw loop runs it trys to "call down" into the next function
# by adding a new frame to the stack. The step_seq is the order in which it
# tries to do this, with one entry for each of the knight's eight moves

# NOTES: the problem as listed is number from 1-8 so I just used the same
# values in the array and left an empty column and row at value 0
# The origin is bottom right again as the diagram is drawn.


##############
x = 8
y = 8


##############
board = [ [9999] * 9 for n in range(9) ] 
steps = 0
board[y][x]=steps
step_seq = [(2,1),(2,-1),(-2,1),(-2,-1), (1,2),(1,-2),(-1,2),(-1,-2)] # order in which knight will move
stack = [(x,y,steps,step_seq)] # we can't use standard recursion

psize = 90
px = 0
py = 0
update = False

def setup():
  frameRate(60)
  size(800,800)



def draw():
  global stack, board, update
  # print stack
  # print board
  
  current_frame = stack.pop()  
  x,y,steps,step_seq = current_frame # copy the values from the last value on stack
  
  update = False
      
  if steps == 0 and step_seq == []: # done
    stack.append(current_frame) # dump frame back onto stack
    
  elif step_seq == []: 
      # go up a level by leaving frame popped off the stack
      pass
      
  else:
      
      dx,dy = step_seq.pop()
      stack.append((x,y,steps,step_seq)) # put frame back on with one move taken off
      
      steps += 1
      if 0 < x+dx <= 8 and 0 < y+dy <= 8 and steps < board[y+dy][x+dx]:
          # recursive
          stack.append( (x+dx,y+dy,steps,[(2,1),(2,-1),(-2,1),(-2,-1), (1,2),(1,-2),(-1,2),(-1,-2)]) )
          board[y+dy][x+dx] = steps 
          update = True
  
  fill(200,200,200,40)
  rect(0,0,800,800)
      
  # draw board
  px = 0
  py = 0
  for ly in range(8,0,-1):
    for lx in range(1,9):
        
      #fill(board[y][x]*25)
      fill(0)
      #rect(px,py,psize,psize)
      if board[ly][lx] != 9999:
    
        if update and ly == dy+y and lx == dx+x:
            fill(0,0,0,50)
            rect(px,py,100,100)
        fill(0)
        text(str(int(board[ly][lx])),px+psize/2,py+psize/2)
      px += psize
    
    py += psize
    px = 0
    
    
    
