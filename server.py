def fread(nazwa):
    file = open(nazwa, 'r')
    list = file.readlines()
    file.close()
    return list


def fwrite(name, list):
    file = open(name, 'w')
    for i in range(len(list)):
        for j in range(len(list[i])):
            for n in range(len(list[i][j])):
                file.write(str(list[i][j][n]))
                if n==len(list[i][j])-1:
                    file.write(" ")
            if j==len(list[i])-1:
                file.write('\n')
    file.close()


def encrypt(list_encrypt):
    encrypted = []
    for i in range(len(list_encrypt)):
        encrypted.append([])
        for j in range(len(list_encrypt[i])):
            if list_encrypt[i][j] != '\n':
                if j != 0:
                    sys = (ord(list_encrypt[i][j - 1]) % 8) + 2
                    encrypted[i].append(conversion(ord(list_encrypt[i][j]), sys))

                else:
                    encrypted[i].append(conversion(ord(list_encrypt[i][j]), 2))
    print(encrypted)
    fwrite("input\\szyfr.txt", encrypted)


def conversion(number, system):
    converted = []
    n = number
    s = system
    while n > 0:
        converted.append(n % s)
        n = int(n / s)
    converted.reverse()
    return converted


def decrypt(list):
    decrypted = []



encrypt(fread("input\\tekst.txt"))
decrypt(fread("input\\szyfr.txt"))

