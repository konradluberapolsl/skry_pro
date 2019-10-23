def fread(nazwa):
    file = open(nazwa, 'r')
    list = file.readlines()
    # print(ListEncrypt[1])
    encrypt(list)
    file.close()


def fwrite(name):
    file = open(name, 'r')
    list = file.readlines()
    file.close()


def encrypt(list_encrypt):
    encrypted = []
    for i in range(len(list_encrypt)):
        encrypted.append([])
        for j in range(len(list_encrypt[i])):
            if list_encrypt[i][j] != '\n':
                if j!=0:
                    print("chuj")
                else:
                    print("chuj 1. litera")
                #print(bin(ord(list_encrypt[i][j])))
                print(list_encrypt[i][j])
                encrypted[i].append(list_encrypt[i][j])
    print(encrypted)


#def conversion(number, system):



fread("input\slowa.txt")
