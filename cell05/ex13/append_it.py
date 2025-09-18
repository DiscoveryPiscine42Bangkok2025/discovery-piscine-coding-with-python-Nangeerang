import sys
import re

def main():
    """Modifying Strings"""
    if len(sys.argv) == 1:
        print("none")
        return

    for arg in sys.argv[1:]:
        if arg.endswith("ism"):
            continue
        print(arg + "ism")


main()