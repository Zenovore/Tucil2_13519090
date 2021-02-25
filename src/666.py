#!/usr/bin/python3

def open_file(namafile):
    kata = ""
    cek = True
    lista = []
    listi = []
    with open(namafile,'r') as f:
        lines = f.read()
        lines = lines.replace(" ","\n")
        # lines = lines.append

    for line in lines :
        # print(line)
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
            # print(kata)
    return listi

    #     line = line.replace(",","\n")
    #     line = line.replace(" ","")
    #     line = line.replace("\n","")
    #     if '.' in line:
    #         line = line.replace(".","")
    #     print
    #     lista.append(line)
    #     print(lista)
    #     # line = line.rstrip(",") 
    #     print(line)

    # return char

def hapuselemen(sirsak,jambu):
    # MELAKUKAN PENGHAPUSAN JAMBU PADA LIST SIRSAK
    for i in range(len(sirsak)):
        # if len(sirsak[i]) == 0:
            # sirsak[i],sirsak[len(sirsak)-1] = sirsak[len(sirsak)-1],sirsak[i]
            # sirsak = sirsak[:-1]
        for j in range (len(sirsak[i])):
            # print (i," - ",j)
            # print (len(sirsak)," -- ",len(sirsak[i]) )
            if (sirsak[i][j] == jambu):
                sirsak[i][j] = ''
                # SWAP MENJADI ELEMEN TERAKHIR
                # sirsak[i][j],sirsak[i][len(sirsak[i])-1] = sirsak[i][len(sirsak[i])-1],sirsak[i][j]
                # # DELETE ELEMENT PADA LIST
                # sirsak[i] = sirsak[i][:-1]
    sirsak = hapuselementkosong(sirsak)
    print(sirsak)
    return sirsak

def hapuselementkosong(sirsak):
    i = 0
    j = 0
    while (i < len(sirsak)):
        if len(sirsak[i]) == 0:
            sirsak[i],sirsak[len(sirsak)-1] = sirsak[len(sirsak)-1],sirsak[i]
            sirsak = sirsak[:-1]
        if (len(sirsak[i]) == 1 and sirsak[i][0] == ''):
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
        topsort(hapuselemen(apel,apel[index][0]),durian)
    return durian



# PROGRAM UTAMA
soal = open_file("../test/soal.txt")
jawaban = []
topsort(soal,jawaban)
print(jawaban)
# print(soal)
# print(jawaban)
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
