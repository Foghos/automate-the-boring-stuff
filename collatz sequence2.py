
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        number = number // 2
        return number

    elif number % 2 == 1:
        print(3 * number + 1)
        number = 3 * number + 1
        return number


try:
    print("Enter a number: ")
    n = int(input(""))
    while n != 1:
        n = collatz(n)


except ValueError:
    print("Wrong Value.")


