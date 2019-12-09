import matplotlib.pyplot as plt
import glob

systems ={}


def fread(nazwa):
    path = nazwa
    files = glob.glob(path)
    i = 0
    list = []
    for name in files:
        list.append([])
        with open(name, 'r') as f:
            list[i] = f.readlines()
            f.close()
        i+=1
    print(list)
    return list

def read(name):
    list = []
    path = name
    files = glob.glob(path)
    word = ''
    i = 0
    j = 0
    # file = open(name, 'r')
    for n in files:
        list.append([])
        with open(n, 'r') as f:
            for line in f:
                list[j].append([])
                for letter in line:
                    if letter == ' ':
                        list[j][i].append(word)
                        word = ''
                    elif letter=="\n": pass
                    else:
                        word+=letter
                i += 1
            f.close()
        i = 0
        j += 1
    # file.close()
    return list


def fwrite(name, list):
    for c in range(len(list)):
        path = name
        path = path + str(c) + '.txt'
        file = open(path, 'w')
        for i in range(len(list[c])):
            for j in range(len(list[c][i])):
                for n in range(len(list[c][i][j])):
                    file.write(str(list[c][i][j][n]))
                    if n == len(list[c][i][j]) - 1:
                        file.write(" ")
                if j == len(list[c][i]) - 1:
                    file.write('\n')
        file.close()



def write(name, list):
    # file = open(name, 'w')
    for i in range(len(list)):
        path = name
        path = path + str(i) + '.txt'
        file = open(path, 'w')
        for item in list[i]:
            file.write(item +'\n')
        file.close()

def encrypt(list_encrypt):
    encrypted = []
    for c in range(len(list_encrypt)):
        encrypted.append([])
        for i in range(len(list_encrypt[c])):
            encrypted[c].append([])
            for j in range(len(list_encrypt[c][i])):
                if list_encrypt[c][i][j] != '\n':
                    if j != 0:
                        sys = (ord(list_encrypt[c][i][j - 1]) % 8) + 2
                        if sys not in systems: systems.update({sys: 1})
                        else: systems[sys]+=1
                        encrypted[c][i].append(conv_to_sys(ord(list_encrypt[c][i][j]), sys))

                    else:
                        if 2 not in systems: systems.update({2: 1})
                        else: systems[2] += 1
                        encrypted[c][i].append(conv_to_sys(ord(list_encrypt[c][i][j]), 2))
    fwrite("output/szyfr", encrypted)


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
    for c in range(len(list)):
        decrypted.append([])
        for i in range(len(list[c])):
            for j in range(len(list[c][i])):
                if j==0: sys=2
                letter = conv_from_sys(list[c][i][j], sys)
                word+=chr(letter)
                sys = (letter%8)+2
            decrypted[c].append(word)
            word =''
    write("output/odszyfrowane",decrypted)

def plot():
    fig, ax = plt.subplots()
    plt.bar(systems.keys(),systems.values(),color="forestgreen")
    plt.title("Ilość wystąpień danego systemu liczbowego" )
    plt.xlabel("Rodzaj systemu")
    plt.ylabel("Ilość wystąpień")
    plt.savefig("images/plot.png",dpi=100)



encrypt(fread("input/*.txt"))
decrypt(read("output/*.txt"))
plot()




