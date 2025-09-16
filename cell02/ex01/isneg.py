def main():
    
    number = int(input("Type for Number : "))
    if number == 0:
        print("This number is both positive and negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is negative.")
main()