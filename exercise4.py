def charcheck(arg):
    if isinstance(arg, str):
        if len(arg) <= 8:
            print('False')
        else:
            print('True')
    else:
        print('Not a string, enter a string')


charcheck(2)
charcheck('james')
charcheck('Perhaps a longer one')
