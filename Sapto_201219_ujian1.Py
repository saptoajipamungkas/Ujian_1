#Nama        : Sapto Aji Pamungkas
#Kelas       : Data Science Batch 7
#Ujian       : Ujian Modul 1
#Tanggal     : 20-12-2019
print('\n')
print('\n')
################################################################################################
#Jawaban Soal No. 1
print('Jawaban Soal No. 1\n')
def Hashtag(string):
    katabaru=(string.split())
    if len(string)==0 or len(string)>140:
        print('False')
    else :
        z='#'
        for i in range (len(katabaru)):
            katabaru[i] = (katabaru[i].capitalize())
            z+=katabaru[i]
        print(z)
Hashtag("Hello there how are you doing")
Hashtag(" Hello     World")
Hashtag("")
print('\n')

################################################################################################
#Jawaban Soal No. 2
print('Jawaban Soal No. 2\n')
def create_phone_number(number):
    print('({}{}{})'.format(number[0],number[1],number[2])+' {}{}{}-'.format(number[3],number[4],number[5])+'{}{}{}{}'.format(number[6], number[7],number[8],number[9]))
create_phone_number([1,2,3,4,5,6,7,8,9,0])

print('\n')

################################################################################################
#Jawaban Soal No. 3
print('Jawaban Soal No. 3\n')
def sort_odd_even(num):
    ganjil=[]
    for i in range (len(num)):
        if num[i]%2!=0:
            ganjil.append(num[i])
        elif num[i]%2==0:
            ganjil.append(0)
    genap=[]
    for i in range (len(num)):
        if num[i]%2==0:
            genap.append(num[i])
        elif num[i]%2!=0:
            genap.append(0)
    for i in range(len(ganjil)-2):
        for j in (i+1, len(ganjil)-2):
            if ganjil[i]>=1 and ganjil[j]>=1 and ganjil[i]>ganjil[j]:
                tukar = ganjil[i]
                ganjil [i]=ganjil[j]
                ganjil[j] = tukar
    for i in range(len(genap)-1):
        for j in (i+1, len(genap)-1):
            if genap[i]>0 and genap[j]>0 and genap[i]<genap[j]:
                tukar = genap[i]
                genap [i]=genap[j]
                genap [j] = tukar
    z = []
    for i in range (len(num)):
        x = ganjil [i]+genap[i]
        z.append(x)
    print (z)

sort_odd_even([5,3,2,8,1,4])
print('\n')

################################################################################################
#Jawaban Soal No. 4
print('Jawaban Soal No. 4\n')

def hollowTriangle (h):
    for i in range (h):
        if i == (h-1):
            print(('#'*((h*2-1))))
        elif i< (h-1) and i !=0:
            print ('_'*((h-1)-i)+('#')+('_'*(2*i-1))+('#')+('_'*((h-1)-i) )) 
        elif i==0:
            print ('_'*((h-1)-i)+('#')+('_'*((h-1)-i)))            
                
hollowTriangle(1)
hollowTriangle(2)
hollowTriangle(3)
hollowTriangle(4)
hollowTriangle(5)
hollowTriangle(6)

print('\n')
print('Terima Kasih')