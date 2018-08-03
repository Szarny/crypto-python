# Vigenere Cipher

# ヴィジュネル表生成アルゴリズム
def TableGen():
    table = []

    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        table.append(text)
        text = text[1:] + text[0]

    return table

# 鍵生成アルゴリズム
def KeyGen():
    key = input("Key : ")
    return key

# 暗号化アルゴリズム
def Enc(plain, key, table):
    cipher = ""
    text_l = "abcdefghijklmnopqrstuvwxyz"
    text_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i,p in enumerate(plain):
        cipher += table[text_u.index(key[i % len(key)])][text_l.index(p)]

    return cipher

# 復号アルゴリズム
def Dec(cipher, key, table):
    plain = ""
    text_l = "abcdefghijklmnopqrstuvwxyz"
    text_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i,c in enumerate(cipher):
        plain += text_l[table[text_u.index(key[i % len(key)])].index(c)]

    return plain

def main():
    while True:
        mode = input("[E]nc [D]ec e[X]it : ")

        if mode == "X":
            return

        msg = input("Message : ")

        if mode == "E":
            print(Enc(msg, KeyGen(), TableGen()))
        elif mode == "D":
            print(Dec(msg, KeyGen(), TableGen()))

        print()

main()
