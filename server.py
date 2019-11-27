import matplotlib.pyplot as plt

systems ={}


def fread(nazwa):
    file = open(nazwa, 'r')
    list = file.readlines()
    file.close()
    return list

def read(name):
    list = []
    word = ''
    i = 0
    file = open(name, 'r')
    for line in file:
        list.append([])
        for letter in line:
            if letter == ' ':
                list[i].append(word)
                word = ''
            elif letter=="\n": pass
            else:
                word+=letter
        i += 1
    file.close()
    return list


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

def write(name, list):
    file = open(name, 'w')
    for item in list:
        file.write(item +'\n')
    file.close()

def encrypt(list_encrypt):
    encrypted = []
    for i in range(len(list_encrypt)):
        encrypted.append([])
        for j in range(len(list_encrypt[i])):
            if list_encrypt[i][j] != '\n':
                if j != 0:
                    sys = (ord(list_encrypt[i][j - 1]) % 8) + 2
                    if sys not in systems: systems.update({sys: 1})
                    else: systems[sys]+=1
                    encrypted[i].append(conv_to_sys(ord(list_encrypt[i][j]), sys))

                else:
                    if 2 not in systems: systems.update({2: 1})
                    else: systems[2] += 1
                    encrypted[i].append(conv_to_sys(ord(list_encrypt[i][j]), 2))
    fwrite("output/szyfr.txt", encrypted)


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
    num = ''.join(reversed(number))
    for i in range(len(num)):
        sum+=int(num[i]) * pow(sys,i)
    if sum>127: sum-=127
    return sum


def decrypt(list):
    decrypted = []
    sys = 0
    word=''
    letter=0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if j==0: sys=2
            letter = conv_from_sys(list[i][j], sys)
            word+=chr(letter)
            sys = (letter%8)+2
        decrypted.append(word)
        word =''
    write("output/odszyfrowane.txt",decrypted)

def plot():
    fig, ax = plt.subplots()
    plt.bar(systems.keys(),systems.values(),color="forestgreen")
    plt.title("Ilość wystąpień danego systemu liczbowego" )
    plt.xlabel("Rodzaj systemu")
    plt.ylabel("Ilość wystąpień")
    plt.savefig("images/plot.jpg",dpi=100)



encrypt(fread("input/tekst.txt"))
decrypt(read("output/szyfr.txt"))
plot()




