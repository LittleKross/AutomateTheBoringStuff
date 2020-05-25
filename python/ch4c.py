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
    maxWidth = 0
    maxHeight = 0
    for line in fileData:
        if len(line) > maxWidth:
            maxWidth = len(line)
    fileData.seek(0)
    for line in fileData:
        for j in range(maxWidth):
            if i == 0:
                uprightData.append([])
            try:
                uprightData[j].append(line[:-1][j])
            except IndexError:
                uprightData[j].append(' ')
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
printGrid(data)
printGrid(grid)

# add a gui type printout