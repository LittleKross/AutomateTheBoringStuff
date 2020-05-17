def listElements(somelist):
    for item in range(len(somelist) - 1):
        print(somelist[item] + ', ',end='')
    print('and ',somelist[int(len(somelist)-1)])

def main():
    test = ['a','small','boy','tries','hard']
    listElements(test)

main()