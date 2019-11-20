def fread(nazwa):
    file = open(nazwa, 'r')
    list = file.readlines()
    file.close()
    return list

def read(name):
    list = []
    i = 0
    j = 0
    file = open(name,'r')
    for line in file:
        list.append([])
        for letter in line:
            list[i].append([])
            if letter == ' ': pass
            else:
                list[i][j].append(letter)
            j+=1
        i+=1
    print(list)
    file.close()


def fwrite(name, list):
    file = open(name, 'w')
    for i in range(len(list)):
        for j in range(len(list[i])):
            for n in range(len(list[i][j])):
                file.write(str(list[i][j][n]))
                if n == len(list[i][j]) - 1:
                    file.write(" ")
            if j == len(list[i]) - 1:
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
                    encrypted[i].append(conv_to_sys(ord(list_encrypt[i][j]), sys))

                else:
                    encrypted[i].append(conv_to_sys(ord(list_encrypt[i][j]), 2))
    #print(encrypted)
    fwrite("input\\szyfr.txt", encrypted)


def conv_to_sys(number, system):
    converted = []
    n = number
    s = system
    while n > 0:
        converted.append(n % s)
        n = int(n / s)
    converted.reverse()
    return converted


def conv_from_sys(number, sys):
    sum = 0
    print(number)
    number.reverse()
    if sys == 2:
        for i in number:
            if i == '1': sum += 2 ^ i
    return sum


def decrypt(list):
    decrypted = []
    print(list)
    print(decrypted)
    # print(conv_from_sys(list[0],2))


encrypt(fread("input\\tekst.txt"))
#decrypt(fread("input\\szyfr.txt"))
read("input\\szyfr.txt")