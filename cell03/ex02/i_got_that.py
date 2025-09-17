'''cell03 ex02'''

def main():
    """While loop"""
    txt = input("What you gotta say? : ")
    while True:
        if txt == "STOP":
            break
        else:
            txt = input("I got that! Anything else? : ")

main()