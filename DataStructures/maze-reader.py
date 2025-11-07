def readMaze(filename):
    try:
        with open(filename) as fh:
            maze = []
            for line in fh:
                line = line.strip('\n')
                characters = []
                for ch in line:
                    characters.append(ch)
                maze.append(characters)
        cols = len(maze[0])
        for row in maze:
            if cols != len(row):
               print("The maze is not rectangular. It is invalid.")
               raise SystemExit 
        return maze    
    except OSError:
        print("There is a problem with the file you have selected")
        raise SystemExit

if __name__ == "__main__":
    maze = readMaze('mazes/diagonal_23x23.txt')
    for row in maze:
        print(row)