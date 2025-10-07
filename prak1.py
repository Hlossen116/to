import random as rand
# Representasi Biner
print("Representasi Biner")
def representasiBiner(jumlahBit):
    ret = []
    for _ in range(jumlahBit):
        ret.append(rand.randint(0, 1))
    return ret

jumlahBit = 8
solusi = representasiBiner(jumlahBit)
print(solusi)



# Representasi Real
# import random as rand
print("Representasi Real")
def representasiReal(variabel):
    ret = []
    for i in range(len(variabel)):
        ret.append(rand.uniform(variabel[i][0], variabel[i][1]))
    return ret

variables = [
    [5, 7.49],
    [7.5, 12.49],
    [12.5, 15]
]

solusi = representasiReal(variables)
print(solusi)


# Representasi Permutasi
# import random as rand
print("Representasi Permutasi")
from itertools import permutations

solusi =list(permutations(range(1,4)))
indexOfRepresentation = rand.randint(0, len(solusi)-1)
print(solusi[indexOfRepresentation])

# Representasi Diskrit
# import random as rand
print("Representasi Diskrit")
def representasiDiskrit(variabeles):
    ret = []
    for i in range(len(variabeles)):
        ret.append(rand.randint(variabeles[i][0], variabeles[i][1]))
    return ret

variables = [
    [1, 5],
    [4, 8],
    [7, 15],
    [1,3]
]

solusi = representasiDiskrit(variables)
print(solusi)


# pretes
# langkah 1 & 2: buat 1 larik dengan 5 iterasi
array_1d = []
for i in range(5):
    array_1d.append(i)

# langkah 3: ulangi 2 kali dan simpan ke dalam larik 2D
array_2d = []
for j in range(2):
    array_2d.append(array_1d)

# tampilkan hasil
print(f"Larik satu dimensi: {array_1d}")
print(f"Larik dua dimensi: {array_2d}")

tupple = (1, 2, 3)
print(tupple)

set_a = {1, 2, 2, 3}
print(set_a)
