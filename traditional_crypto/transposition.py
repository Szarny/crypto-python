# Transposition Cipher

# 鍵生成アルゴリズム
def KeyGen():
    key = [3, 1, 4, 2]
    return key

# 暗号化アルゴリズム
def Enc(plain, key):
    cipher = ""

    front = 0
    rear = 4

    while front < len(plain):
        p_block = plain[front:rear]

        # ブロック内の文字が4文字に満たない場合は無視する
        if len(p_block) != 4:
            cipher += p_block
        else:
            for loc in key:
                cipher += p_block[loc-1]

        front += 4
        rear += 4

    return cipher

# 復号アルゴリズム
def Dec(cipher, key):
    plain = ""

    front = 0
    rear = 4

    while front < len(cipher):
        c_block = cipher[front:rear]

        # ブロック内の文字が4文字に満たない場合は無視する
        if len(c_block) != 4:
            plain += c_block
        else:
            for loc in key[::-1]:
                plain += c_block[loc-1]

        front += 4
        rear += 4

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
