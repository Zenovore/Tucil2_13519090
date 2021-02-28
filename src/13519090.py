#!/usr/bin/python3
import datetime 

def open_file(namafile):
    # MEMBUKA FILE.TXT DAN MENGUBAH MENJADI ADJACENCY LIST
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
    # print(listi)
    return listi

def hapuselemen(sirsak,jambu):
    # MELAKUKAN PENGUBAHAN ELEMEN LIST SIRSAK DENGAN NILAI JAMBU
    for i in range(len(sirsak)):
        for j in range (len(sirsak[i])):
            for k in range(len(jambu)):
                # PENGECEKAN JIKA ADA ELEMEN ELEMEN SIRKSA YANG SAMA DENGAN ELEMEN JAMBU
                if (sirsak[i][j] == jambu[k]):
                    # MELAKUKAN PENGUBAHAN ELEMEN SIRSAK DENGNA NILAI ''
                    sirsak[i][j] = ''
    # MENGHAPUS ELEMEN DARI SIRSAK DENGAN NILAI ''
    return hapuselementkosong(sirsak)

def hapuselementkosong(sirsak):
    # MENGHAPUS LIST YANG KOSONG (ELEMEN BERNILAI '')
    i = 0
    j = 0
    # MENGHAPUS ELEMEN LIST YANG KOSONG ATAU MEMILIKI 1 ELEMEN DENGAN NILAI ''
    while (i < len(sirsak)):
        if len(sirsak[i]) == 0:
            sirsak.remove(sirsak[i])
        elif (len(sirsak[i]) == 1 and sirsak[i][0] == ''):
            sirsak.remove(sirsak[i])
        else :
            i += 1
    # MENGHAPUS ELEMEN LIST DALAM LIST DENGAN NILAI ''
    for i in range(len(sirsak)):
        j=0
        while(j <len(sirsak[i])):
            if sirsak[i][j] == '':
                sirsak[i].remove(sirsak[i][j])
            else :
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
        # MEMASUKAN MATA KULIAH YANG SUDAH DIAMBIL TERHADAP LIST DURIAN
        durian.append(nangka)
        # MELAKUKAN REKURSI DENGAN LIST APEL TANPA MATA KULIAH YANG SUDAH DIAMBIL (SUDAH DI-DECREASE)
        topsort(hapuselemen(apel,nangka),durian)
    return durian

# PROGRAM UTAMA
soal = open_file("../test/soal8.txt")
begin_time = datetime.datetime.now()
cek = True
jawaban = []
for i in range(len(soal)):
    if (len(soal[i]) == 1):
        cek = False
        break
if (not cek):
    topsort(soal,jawaban)
    jawaban = hapuselementkosong(jawaban)
    print("JADWAL PENGAMBILAN MATKUL : ")
    for i in range(len(jawaban)):
        if (len(jawaban[i])!= 0):
            print("Semester",inttoroman(i+1),"\t: ", ', '.join(jawaban[i])+'.')
    print("WAKTU YANG DIGUNAKAN : ",datetime.datetime.now() - begin_time )
else:
    print("Mohon maaf, tidak ada mata kuliah tanpa prerequisite")