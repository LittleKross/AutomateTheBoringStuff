import random
numberOfStreaks = 0
for experimentNumber in range(1):
    data = []
    currentStreak = True
    currentStreakLength = 0
    numberOfStreaksThisTime = 0
    for i in range(100):
        data.append(random.randint(0,1))
        if currentStreak != data[i]:
            currentStreak = not currentStreak
            currentStreakLength = 0
        else:
            currentStreakLength += 1
        if currentStreakLength == 6:
            numberOfStreaks += 1
            numberOfStreaksThisTime += 1
        elif currentStreakLength > 6:
            currentStreakLength += 1
    print(data)
    print(numberOfStreaksThisTime)
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))