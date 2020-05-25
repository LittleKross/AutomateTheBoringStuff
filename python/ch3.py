def collatz(number):
    if number == 1:
        return
    elif (number % 2) == 0:
        calculated = number // 2
        print(calculated)
        return collatz(calculated)
    else:
        calculated = 3 * number + 1
        print(calculated)
        return collatz(calculated)

def run():
    print('Enter a number:')
    try:
        value = int(input())
        collatz(value)
    except ValueError:
        print('Please enter an integer value.')


def main():
    run()

main()