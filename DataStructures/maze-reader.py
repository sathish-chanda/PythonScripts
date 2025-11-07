def readMaze(filename):
    try:
        with open(filename) as fh:
            maze = []
            for line in fh:
                characters = []
                for ch in line.strip():
                    characters.append(ch)
                maze.append(characters)
        cols = len(maze[0])
        for row in maze:
            if cols != len(row):
               print("The maze is not rectangular. It is invalid.")
               raise SystemExit 
        return maze    

    except OsError:
        print("There is a problem with the file you have selected")
        raise SystemExit

if __name__ == "__main__":
    maze = readMaze('mazes/modest_maze.txt')
    for row in maze:
        print(row)