# ROTx

# 鍵生成アルゴリズム
def KeyGen():
    key = int(input("Key : "))
    return key

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

def Attack(msg):
    for key in range(26):
        print("[key {}] {}".format(key, Dec(msg, key)))
    return

def main():
    while True:
        mode = input("[E]nc [D]ec [A]ttack e[X]it : ")

        if mode == "X":
            return

        msg = input("Message : ")

        if mode == "E":
            print(Enc(msg, KeyGen()))
        elif mode == "D":
            print(Dec(msg, KeyGen()))
        elif mode == "A":
            Attack(msg)

        print()

main()
