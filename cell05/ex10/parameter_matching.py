import sys

def main():

    if len(sys.argv) == 1:
        print("none")
    else:
        param = sys.argv[1]
        check = input("What was the parameter? ")
        if param == check:
            print("Good job!")
        else:
            print("Nope, sorry...")

main()