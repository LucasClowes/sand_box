"""Lucas Clowes"""


def main():
    name = input("Enter your name: ")
    while not name:
        print('Entry must not be blank')
        name = input("Enter your name: ")
    length = len(name)
    for i in range(1, length, 2):
        print(name[i])


main()
