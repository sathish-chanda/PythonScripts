from priority_queue import PriorityQueue
from maze_reader import readMaze
from helper import directions, isValidCell, getPath

def heuristicDistance(start,goal):
    x1,y1 = start
    x2,y2 = goal
    return abs(x1-x2) + abs(y1-y2)

def a_star(maze,start,goal):
    predessor = {start: None}
    pq = PriorityQueue()
    pq.put(start,0)
    g_values = {start:0}

    while not pq.isEmpty():
        current = pq.get()
        if current == goal:
           return getPath(predessor,start,goal)
        else:
            for direction in ["up","right","down","left"]:
                x,y = directions[direction]
                gValue = g_values[current] + 1
                nextCell = (current[0] + x, current[1] + y)
                if isValidCell(maze,nextCell) and nextCell not in g_values:
                   predessor[nextCell] = current
                   g_values[nextCell] = gValue
                   hValue = heuristicDistance(nextCell,goal)
                   fValue = gValue + hValue
                   pq.put(nextCell,fValue)
    return None

if __name__ == '__main__':
   # Test 1
   maze = [[0] * 3 for row in range(3)]
   start = (0,0)
   goal = (2,2)
   result = a_star(maze,start,goal)
   print(result)
   assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
   
   maze = readMaze('mazes/mini_maze_bfs.txt')
   start = (0,0)
   goal = (2,2)
   result = a_star(maze,start,goal)
   print(result)
   assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
   
   print(a_star(readMaze('mazes/diagonal_23x23.txt'),(1,1),(9,14)))

   print(a_star(readMaze('mazes/dfs_bfs_a_star_challenge.txt'),(0,0),(3,3)))