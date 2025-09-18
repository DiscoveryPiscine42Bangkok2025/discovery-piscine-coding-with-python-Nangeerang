import sys

def main():
    if len(sys.argv) > 2:
        print('\n'.join(reversed(sys.argv[1:])))
    else:
        print("none")

main()