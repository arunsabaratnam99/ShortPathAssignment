#Arun Sabaratnam 300297854
#Bob Yang 300288751

#Printing the maze 
'''
Cases to look out for:
- Maze isn't valid
- Invalid character 
- Blocked path
- Maze doesn't end/start OR multiple start and end points 
- Not a constant number of sequences
'''

from collections import deque
from typing import OrderedDict
from operator import sub

def sortPuzzle(puzzle):
  paths = [] 
  for i in range(len(puzzle)):
    x = puzzle[i]
    try:
      y = puzzle[i+1]
    except:
      break 
    
    if x[2] == y[2]:
      paths.append(x)
      paths.append(y)
      
  return paths 

n = int(input('Please input the amount of lines you would like to have\n'))
puzzle = []

for i in range(1, n+1):
  x = input('Please input line #' + str(i) + '\n')
  
  while len(x) != 16:
    print('Sorry that isnt is a valid length, it has to be 16 characters\n')
    x = input('Please input line #' + str(i) + '\n')
    
  x = list(x)
  
  puzzle.append(x)
  

#finding leftmost and rightmost
for i in range(len(puzzle)):
  if puzzle[i][0] == 'p':
    leftmost = i
    
  elif puzzle[i][15] == 'p':
    rightmost = i

#Creating a list to hold all the coordinates the algorithm attempts
thing = []

R, C = len(puzzle), len(puzzle[0])
start = (leftmost, 0)

#using bfs with queue to find shortest path
queue = deque()
queue.appendleft((start[0], start[1], 0))
#right, left, down, up
d = [[0,1],[0,-1],[1,0],[-1,0]]
visited = [[False] * C for _ in range(R)]
distance = 0
puzzle[rightmost][15] = ">"

while len(queue) != 0:
 
  coord = queue.pop()
  thing.append(coord)
  visited[coord[0]][coord[1]] = True

  if coord[0] == rightmost and coord[1] == 15:
    #returns shortest distance
    distance =  coord[2]

  for dir in d:
    #trying a new path
    nr, nc = coord[0]+dir[0], coord[1]+dir[1]
    #if path is invalid dont append to queue
    if nr < 0 or nr >= R or nc <0 or nc>= C or puzzle[nr][nc] == "#" or visited[nr][nc]:
      #puzzle[coord[0]][coord[1]] = "p"
      continue

    #append the distance as tuple to queue
    queue.appendleft((nr,nc,coord[2]+1))

 #imports
from typing import OrderedDict
from operator import sub

#Sorting the coordinates given to append all the ones with the same distance to a new list 
def sortPuzzle(puzzle):
  paths = [] 
  for i in range(len(puzzle)):
    x = puzzle[i]
    try:
      y = puzzle[i+1]
    except:
      break 
    
    if x[2] == y[2]:
      paths.append(x)
      paths.append(y)
      
  return paths 
    
#Sorting all the coordinates given
same = sortPuzzle(thing)

#Removing all duplicates
same = list(OrderedDict.fromkeys(same))

#Creating a list of indexs to hold all the indexs where theres more than 2 of the same distance
listofindexs = [] 

#Appending it all to a list
for i in same:
    listofindexs.append(i[2])
 
#Making it go from greatest to least to represent going from the ending to beginning path
listofindexs.sort(reverse = True)

#Reversing the sorted list
same.reverse()

#Creating a array to hold the correct order of things
order = []
for i in range(len(listofindexs)):
  #If index only appears once AFTER removing the duplicates add it to the correct orter
  if listofindexs.count(listofindexs[i]) == 1:
    order.append(same[i])
    
  else: 
    #Otherwise, look at the next coordinates (which have the same distance) and see which one is next to the previous coordinate
    tempcount = listofindexs.count(listofindexs[i])
    temp = []
    for j in range(tempcount):
        try:
          temp.append(listofindexs[i+j])
        except:
          break 
            
    if temp.count(temp[0]) == len(temp) and len(temp) != 1:
        for k in range(len(temp)):
          checkee = same[i+k]
          checker = same[i-1]
                
          ans = tuple(map(sub,checker,checkee))         
          listans = list(ans)
          listans = [abs(val) for val in listans]
          ans = tuple(listans)
              
          if ans == (1,0,1) or ans == (0,1,1) or ans == (1,1,1) or ans== (1,0,2) or ans == (0,1,2) or ans == (1,1,2) or ans == (1,1,0):
              order.append(checkee)
              break

#Adding all the coordinates that appeared once to the correct order than sorting it by their distance
for i in range(0,24):
    if i not in [b[2] for b in order]:  
        for j in range(len(thing)):
            x = thing[j]
            
            if x[2] == i:
                order.append(x)
        
order.sort(key = lambda x:x[2])

#get the x and y coordinates of the path and store it in a list
coords = []
for i in range(len(order)):
  x = order[i]
  temp2 = []

  temp2.append((x[0]))
  temp2.append(x[1])

  temp2 = tuple(temp2)

  coords.append(temp2)

print()

#loop through list of coordinates and update path based on the direction taken
for i in range (len(coords)-1):
  y = coords[i]
  c1 = coords[i]
  c2 = coords[i+1]
  
  #find the change in direction
  ans2 = tuple(map(sub,c1,c2))

  #changing character based on direction
  if ans2[0] == 0 and ans2[1] == 1:
      puzzle[y[0]][y[1]] = "<"
  elif ans2[0] == 0 and ans2[1] == -1:
      puzzle[y[0]][y[1]] = ">"
  elif ans2[0] == 1 and ans2[1] == 0:
      puzzle[y[0]][y[1]] = "^"
  elif ans2[0] == -1 and ans2[1] == 0:
      puzzle[y[0]][y[1]] = "v"

#output answer
for i in range(0, len(puzzle)):
  for j in range(0,16):
    print(puzzle[i][j], end = "")
    
  print()

print("The shortest distance is: ", len(coords))