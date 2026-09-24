#1
n = input("Введите число:")
while len(n)%3 != 0:
    n = "0" + n
he = ""
for i in range(0,len(n),3):
    group = n[i:i+3]
    he += str(int(n,2))
print(he)
#2
binary = input("Введите двоичное число: ").strip()
alphabet = "0123456789ABCDEF"

while len(binary) % 4 != 0:
    binary = "0" + binary

hex_number = ""
for i in range(0, len(binary), 4):
    group = binary[i:i+4]
    hex_number += alphabet[int(group, 2)]

print("Шестнадцатеричное представление:", hex_number)
#3
hex_number = input("Введите восьмеричное число: ").upper()
alphabet = "0123456789ABCDEF"

binary = ""
for ch in hex_number:
    binary += format(alphabet.index(ch), "03b")

print("Двоичное представление:", binary)
#4
hexx = input("Введите шестнадцатеричное число: ").upper()
alphabet = "0123456789ABCDEF"

binary = ""
for ch in hexx:
    binary += format(alphabet.index(ch), "04b")

print("Двоичное представление:", binary)
#5
hexx = input("Введите восьмеричное число: ")
alphabet = "0123456789ABCDEF"

binary = ""
for ch in hexx:
    binary += format(alphabet.index(ch), "03b")

print("Двоичное представление:", binary)


alphabet = "0123456789ABCDEF"

while len(binary) % 4 != 0:
    binary = "0" + binary

hexxs = ""
for i in range(0, len(binary), 4):
    group = binary[i:i+4]
    hexxs += alphabet[int(group, 2)]

print("Шестнадцатеричное представление:", hexxs)
#6
hexx = input("Введите шестнадцатеричное число:").upper()
alph = '0123456789ABCDEF'
bina = ''
for ch in hexx:
    bina += format(alph.index(ch), '04b')

print('Двоичное представление:', bina)

while len(bina)%3 != 0:
    bina = '0' + bina

octal = ''
for i in range(0,len(bina),3):
    octal += str(int(bina[i:i+3],2))

octal = int(octal)
print('Восьмеричное:', octal)

#7 ведущие нули влияют на разбиение числа по 3 или 4 символам для преобразования из 2^n СС
#8 Прямой перевод экономит время, ресурсы ПК и исключает доп. преобразование в 10 СС
#9
import random

ch = '01'
bina = [random.choice(ch) for k in range(4, 100)]
binar = '1'+''.join(bina)

print('Двоичное представление:', binar)
binar = binar.strip()
alphabet = "0123456789ABCDEF"

while len(binar) % 4 != 0:
    binar = "0" + binar

hex_number = ""
for i in range(0, len(binar), 4):
    group = binar[i:i+4]
    hex_number += alphabet[int(group, 2)]

print("Шестнадцатеричное представление:", hex_number)

while len(binar) % 3 != 0:
    binar = "0" + binar

hexx_number = ""
for i in range(0, len(binar), 3):
    group = binar[i:i+3]
    hexx_number += alphabet[int(group, 2)]

print("Восьмеричное представление:", hexx_number)

#10 Явное: кратность степени двойки, количество разрядов, четность/нечетностб
#Неявные: знак числа, десятичное значение, простое или составное число
#Представление в СС 2^k является сжимающим к двоичной СС по количеству символов.
