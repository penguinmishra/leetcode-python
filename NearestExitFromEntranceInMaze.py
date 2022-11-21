# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

def nearestExit(maze, entrance):
    queue = []
    directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    rows = len(maze)
    columns = len(maze[0])
    ans = 0

    # offer and mark visited
    queue.append(entrance)
    maze[entrance[0]][entrance[1]] = '+'

    while queue:
        size = len(queue)
        ans += 1
        while size > 0:
            size -= 1
            position = queue.pop(0)
            x = position[0]
            y = position[1]
            
            for dir in directions:
                newX = x + dir[0]
                newY = y + dir[1]

                if newX < 0 or newY < 0 or newX > rows - 1 or newY > columns - 1 or maze[newX][newY] == '+':
                    continue
                elif newX == 0 or newY == 0 or newX == rows - 1 or newY == columns - 1:
                    return ans
                
                # offer and mark visited
                queue.append([newX, newY])
                maze[newX][newY] = '+'
    return -1



maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]
print(nearestExit(maze, entrance))