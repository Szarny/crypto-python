# 鍵生成アルゴリズム
def KeyGen():
    return 3

# 暗号化アルゴリズム
def Enc(plain, key):
    cipher = ""

    for p in plain:
        offset = (-32) + key
        p_sign = ord(p)
        c_sign = p_sign + offset

        if c_sign < 65:
            c_sign += 26

        c = chr(c_sign)
        cipher += c

    return cipher

# 復号アルゴリズム
def Dec(cipher, key):
    plain = ""

    for c in cipher:
        offset = 32 - key
        c_sign = ord(c)
        p_sign = c_sign + offset

        if p_sign > 122:
            p_sign -= 26

        p = chr(p_sign)
        plain += p

    return plain

def main():
    while True:
        mode = input("[E]nc [D]ec e[X]it : ")

        if mode == "X":
            return

        msg = input("Message : ")

        if mode == "E":
            print(Enc(msg, KeyGen()))
        elif mode == "D":
            print(Dec(msg, KeyGen()))

        print()

main()
