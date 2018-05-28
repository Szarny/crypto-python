# Substitution Cipher

# 鍵生成アルゴリズム
def KeyGen():
    key = {
        "src": "abcdefghijklmnopqrstuvwxyz",
        "dst": "KWJHUBVGTXLZIDQYSMFRNCPAEO"
    }
    return key

# 暗号化アルゴリズム
def Enc(plain, key):
    cipher = ""

    for p in plain:
        if p in key["src"]:
            loc = key["src"].index(p)
            cipher += key["dst"][loc]
        else:
            cipher += p

    return cipher

# 復号アルゴリズム
def Dec(cipher, key):
    plain = ""

    for c in cipher:
        if c in key["dst"]:
            loc = key["dst"].index(c)
            plain += key["src"][loc]
        else:
            plain += c

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
