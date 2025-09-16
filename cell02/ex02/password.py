'''cell02 ex02'''
def main():
    '''password'''
    password = "Python is awesome"
    type_Password = input("Enter password : ")
    if type_Password == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
main()