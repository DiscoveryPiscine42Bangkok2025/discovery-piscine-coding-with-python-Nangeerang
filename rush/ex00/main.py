from checkmate import checkmate

def main():
    board = """\
R...
.K..
..P.
....\
    """
 
    result = checkmate(board)
    print(result)

if __name__ == "__main__":
    main()