import sys

def main():
    """Just one step away!"""
    if len(sys.argv) == 1:
        print("none")
        return
    
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    if num1 < num2:
        print(list(range(num1, num2 + 1)))
    else:
        print(list(range(num2, num1 + 1)))


main()