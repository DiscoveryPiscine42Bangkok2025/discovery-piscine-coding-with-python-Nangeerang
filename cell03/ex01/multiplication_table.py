'''cell03 ex01'''

def main():

    '''multiplication_table'''
    number = int(input("Enter a number : "))
    for i in range(0,13):
        print(f"{i} x {number} = {i*number}")

main()