"""cell02 ex03"""
def main():
    '''mult'''
    first_Num = int(input("Enter First Number : "))
    sec_Num = int(input("Enter Second Number : "))
    result = first_Num * sec_Num
    print(f"{first_Num} x {sec_Num} = {result}")
    if result > 0 :
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")
main()