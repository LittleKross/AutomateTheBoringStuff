def printGrid(pixelMap):
    height = len(pixelMap)
    width = len(pixelMap[0])
    for x in range(width):
        for y in range(height):
            print(pixelMap[y][x],end='')
        print()

def importData(fileName):
    uprightData = []
    i = 0
    fileData = open("./"+fileName)
    
    for line in fileData:
        for j in range(len(line)-1):
            if i == 0:
                uprightData.append([])
            uprightData[j].append(line[j])
        i += 1
    
    return uprightData

def printUpright(pixelGrid):
    for x in range(len(pixelGrid)):
        for y in range(len(pixelGrid[x])):
            print(pixelGrid[x][y],end=' ')
        print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

data = importData("skull.txt")
printUpright(data)
printUpright(grid)

# add a gui type printout