def fopen( nazwa ):
    file = open(nazwa, 'r')
    if nazwa == "input\slowa.txt":
        ListEncrypt = file.readlines()
        print(ListEncrypt[1])
    elif nazwa == "input\szyfr.txt":
        ListDecrypt = file.readlines()
        print(ListDecrypt[1])



fopen("input\slowa.txt")