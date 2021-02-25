#!/usr/bin/python3

def open_file(namafile):
    kata = ""
    cek = True
    lista = []
    listi = []
    with open(namafile,'r') as f:
        lines = f.read()
        lines = lines.replace(" ","\n")
    for line in lines :
        if (line == ','):
            lista.append(kata)
            kata = ''
        elif (line == '\n'):
            kata = ''
        elif (line == '.'):
            lista.append(kata)
            listi.append(lista)
            lista =[]
            kata = ''
        else :
            kata += line
    return listi

def hapuselemen(sirsak,jambu):
    # MELAKUKAN PENGHAPUSAN JAMBU PADA LIST SIRSAK
    for i in range(len(sirsak)):
        for j in range (len(sirsak[i])):
            for k in range(len(jambu)):
                if (sirsak[i][j] == jambu[k]):
                    sirsak[i][j] = ''
    sirsak = hapuselementkosong(sirsak)
    # print(sirsak)
    return sirsak

def hapuselementkosong(sirsak):
    i = 0
    j = 0
    while (i < len(sirsak)):
        if len(sirsak[i]) == 0:
            sirsak[i],sirsak[len(sirsak)-1] = sirsak[len(sirsak)-1],sirsak[i]
            sirsak = sirsak[:-1]
        elif (len(sirsak[i]) == 1 and sirsak[i][0] == ''):
            sirsak[i],sirsak[len(sirsak)-1] = sirsak[len(sirsak)-1],sirsak[i]
            sirsak = sirsak[:-1]
        i += 1

    for i in range(len(sirsak)):
        j=0
        while(j <len(sirsak[i])):
            if sirsak[i][j] == '':
                sirsak[i][j],sirsak[i][len(sirsak[i])-1] = sirsak[i][len(sirsak[i])-1],sirsak[i][j]
                sirsak[i] = sirsak[i][:-1]
            j +=1

    return sirsak

def inttoroman(num):
    rom = ''
    if(num//1000 >= 1):
        num = num % 1000
        rom += 'M'
    if(num//900 >= 1):
        num = num % 900
        rom += 'CM'
    if(num//500 >= 1):
        num = num % 500
        rom += 'D'
    if(num//400 >= 1):
        num = num % 400
        rom += 'CD'
    if(num//100 >= 1):
        num = num % 100
        rom += 'C'
    if(num//90 >= 1):
        num = num % 90
        rom += 'XC'
    if(num//50 >= 1):
        num = num % 50
        rom += 'L'
    if(num//40 >= 1):
        num = num % 40
        rom += 'XL'
    if(num//10 >= 1):
        num = num % 10
        rom += 'X'
    if(num//9 >= 1):
        num = num % 9
        rom += 'IX'
    if(num//5 >= 1):
        num = num % 5
        rom += 'V'
    if(num//4 >= 1):
        num = num % 4
        rom += 'IV'
    if(num != 0 and num//1 >= 1):
        for i in range(num):
            rom += 'I'
    return rom
 

# MELAKUKAN DECREASE AND CONQUER
def topsort(apel,durian):
    nangka =[]
    index = 0
    if (len(apel) != 0):
        for i in range(len(apel)):
            if (len(apel[i]) == 1):
                nangka.append(apel[i][0])
                index = i
        durian.append(nangka)
        topsort(hapuselemen(apel,nangka),durian)
        # print(hapuselemen(apel,nangka),durian)
    return durian



# PROGRAM UTAMA
soal = open_file("../test/soal.txt")
jawaban = []
topsort(soal,jawaban)
jawaban = hapuselementkosong(jawaban)
print("JADWAL PENGAMBILAN MATKUL : ")
for i in range(len(jawaban)):
    print("Semester ",inttoroman(i+1)," \t: ", ','.join(jawaban[i]))
# print(hapuselementkosong(jawaban))
# print("------------------------------------")
# jawaban = topsort(soal,jawaban)
# print(soal)
# print(jawaban)
# print("------------------------------------")
# topsort(soal,jawaban)
# print(soal)
# print(jawaban)
# topsort(soal,jawaban)
# print(jawaban)
# topsort(soal,jawaban)
