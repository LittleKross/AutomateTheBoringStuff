import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    data = []
    currentStreak = True
    currentStreakLength = 0
    numberOfStreaksThisTime = 0
    for i in range(100):
        data.append(random.randint(0,1))
        #print(currentStreak,currentStreakLength)
        if currentStreak != data[i]:
            currentStreak = not currentStreak
            currentStreakLength = 0
        else:
            currentStreakLength += 1
        if currentStreakLength == 6:
            numberOfStreaks += 1
            numberOfStreaksThisTime += 1
        elif currentStreakLength > 6:
            pass
    print(data)
    print(numberOfStreaksThisTime)
print('Chance of streak: %s%%' % (numberOfStreaks / 1000000))