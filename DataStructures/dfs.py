from stack import Stack
from maze_reader import readMaze
from helper import directions, isValidCell, getPath

def dfs(maze,start,goal):
    predessor = {start: None}
    stack = Stack()
    stack.push(start)

    while not stack.isEmpty():
        current = stack.pop()
        if current == goal:
           return getPath(predessor,start,goal)
        else:
            for direction in ["up","right","down","left"]:
                x,y = directions[direction]
                nextCell = (current[0] + x, current[1] + y)
                if isValidCell(maze,nextCell) and nextCell not in predessor:
                   predessor[nextCell] = current
                   stack.push(nextCell)
    return None
    
if __name__ == '__main__':
   # Test 1
   maze = [[0] * 3 for row in range(3)]
   start = (0,0)
   goal = (2,2)
   result = dfs(maze,start,goal)
   print(result)
   assert result == [(0,0),(1,0),(2,0),(2,1),(2,2)]
   
   
   maze = readMaze('mazes/mini_maze_dfs.txt')
   start = (0,0)
   goal = (2,2)
   result = dfs(maze,start,goal)
   print(result)
   assert result == [(0,0),(0,1),(1,1),(2,1),(2,2)]
   
   print(dfs(readMaze('mazes/diagonal_23x23.txt'),(1,1),(9,14)))
   
   print(dfs(readMaze('mazes/dfs_bfs_a_star_challenge.txt'),(0,0),(3,3)))