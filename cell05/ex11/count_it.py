
import sys

def main():
    if len(sys.argv) == 1:
        print("none")
    else:
        for arg in sys.argv[1:]:
            print(f"{arg}: {len(arg)}")

main()