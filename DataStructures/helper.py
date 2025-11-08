directions = {
    "up": (0,-1),
    "right": (0,1),
     "down": (1,0),
    "left" : (-1,0)
}

def getPath(predessor, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predessor[current]
    path.append(start)
    path.reverse()
    return path          

def isValidCell(maze,cell):
    return 0 <= cell[0] and 0 <= cell[1] and cell[0] < len(maze) and cell[1] < len(maze[0]) and maze[cell[0]][cell[1]] != '*'

