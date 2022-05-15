

def add(a, b):
    sum = a + b
    return  sum


def main():
    a = input("Enter 1st Number : ")
    b = input("Enter 2nd Number : ")
    a = int(a)
    b = int(b)
    c = add(a, b)
    print(c)

main()