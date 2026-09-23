#1 и 2 задания
message = "101011"
ones = message.count("1")
p = ones % 2
codeword = message + str(p)

received = list(codeword)
received[1] = "0" if received[1] == "1" else "1"
received[3] = "0" if received[3] == "1" else "1"
received = "".join(received)

check = received.count("1") % 2

print("Сообщение:", message)
print("Кодовое слово:", codeword)
print("Принято:", received)
print("Контроль чётности:", check)
print("Ошибка обнаружена" if check == 1 else "Ошибка не обнаружена")

#3
a = "101011001"
b = "100101011"

d = sum(x != y for x, y in zip(a, b))

print("Слово 1:", a)
print("Слово 2:", b)
print("Расстояние Хэмминга:", d)

#4 и 5

mess = "01101"
encoded = ''.join("111" if b == "1" else "000" for b in mess)
print("Объем: ",len(encoded))

# ошибка в первой тройке: меняем второй бит
broken = list(encoded)
broken[3] = "0" if broken[1] == "1" else "1"
broken = "".join(broken)

def maojortrp(br: str) -> str:
    return "1" if br.count("1")>1 else "0"

decoded = ''.join(maojortrp(broken[i:i+3]) for i in range(0, len(broken), 3))

print("Исходное сообщение:", mess)
print("Троированный код:", encoded)
print("Принято с ошибкой:", broken)
print("Декодировано:", decoded)

#6, 7 и 8 задания
mess = '1110'
def hamm74_encode(data_bits: str) -> str:
    d1, d2, d3, d4 = (int(x) for x in data_bits)
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p4 = d2 ^ d3 ^ d4
    code = [p1, p2, d1, p4, d2, d3, d4]
    return ''.join(str(x) for x in code)

code = hamm74_encode(mess)
print("Кодирование хэмминга:",code)

def hamm74_syndrome(cod: str) -> int:
    b = [int(x) for x in cod]
    s1 = b[0] ^ b[2] ^ b[4] ^ b[6]
    s2 = b[1] ^ b[2] ^ b[5] ^ b[6]
    s4 = b[3] ^ b[4] ^ b[5] ^ b[6]
    return s1 * 1 + s2 * 2 + s4 * 4

def hamm74_correct(cod: str) -> str:
    b = [int(x) for x in cod]
    pos = hamm74_syndrome(cod)
    if pos != 0:
        b[pos - 1] ^= 1
    return ''.join(str(x) for x in b)
broken = list(code)
broken [2] = "0" if broken[2] == "1" else "1"
broken = ''.join(broken)
print("Принято с ошибкой:", broken)
print("Синдром хэмминга:", hamm74_syndrome(broken))
print("Исправлено:", hamm74_correct(broken))

#9 и 10

import random

chars = '01'
mess = ''.join(random.choice(chars) for _ in range(4))
print(mess)

ones = mess.count("1")
p = ones % 2
codeword = mess + str(p)

received = list(codeword)
received[1] = "0" if received[1] == "1" else "1"
received[3] = "0" if received[3] == "1" else "1"
received = "".join(received)

check = received.count("1") % 2

print("Сообщение:", mess)
print("Кодовое слово:", codeword)
print("Принято:", received)
print("Контроль чётности:", check)
print("Ошибка обнаружена" if check == 1 else "Ошибка не обнаружена")

encoded = ''.join("111" if b == "1" else "000" for b in mess)
print("Объем: ",len(encoded))

# ошибка в первой тройке: меняем второй бит
broken = list(encoded)
broken[3] = "0" if broken[1] == "1" else "1"
broken = "".join(broken)

def maojortrp(br: str) -> str:
    return "1" if br.count("1")>1 else "0"

decoded = ''.join(maojortrp(broken[i:i+3]) for i in range(0, len(broken), 3))
print()
print("Исходное сообщение:", mess)
print("Троированный код:", encoded)
print("Принято с ошибкой:", broken)
print("Декодировано:", decoded)

print()
def hamm74_encode(data_bits: str) -> str:
    d1, d2, d3, d4 = (int(x) for x in data_bits)
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p4 = d2 ^ d3 ^ d4
    code = [p1, p2, d1, p4, d2, d3, d4]
    return ''.join(str(x) for x in code)

code = hamm74_encode(mess)
print("Кодирование хэмминга:",code)

def hamm74_syndrome(cod: str) -> int:
    b = [int(x) for x in cod]
    s1 = b[0] ^ b[2] ^ b[4] ^ b[6]
    s2 = b[1] ^ b[2] ^ b[5] ^ b[6]
    s4 = b[3] ^ b[4] ^ b[5] ^ b[6]
    return s1 * 1 + s2 * 2 + s4 * 4

def hamm74_correct(cod: str) -> str:
    b = [int(x) for x in cod]
    pos = hamm74_syndrome(cod)
    if pos != 0:
        b[pos - 1] ^= 1
    return ''.join(str(x) for x in b)
broken = list(code)
broken[2] = "0" if broken[2] == "1" else "1"
broken = ''.join(broken)
print("Принято с ошибкой:", broken)
print("Синдром хэмминга:", hamm74_syndrome(broken))
print("Исправлено:", hamm74_correct(broken))