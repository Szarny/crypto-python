from Crypto.Cipher import DES
import random

def KeyGenAuto():
    letters = "abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?#$%&<>"
    key = ""

    for i in range(8):
        key += random.choice(letters)

    print("Key >> {}".format(key))
    return key

# 鍵生成アルゴリズム
def KeyGen():
    return input("Key : ")

# 暗号化アルゴリズム
def Enc(plain, key):
    des = DES.new(key, DES.MODE_ECB)
    cipher = des.encrypt(plain)

    with open("des.enc", "wb") as f:
        f.write(cipher)

    return cipher

# 復号アルゴリズム
def Dec(filename, key):
    des = DES.new(key, DES.MODE_ECB)

    with open("des.enc", "rb") as f:
        cipher = f.read()
        plain = des.decrypt(cipher)
    
    return plain

def main():
    while True:
        mode = input("[E]nc [D]ec e[X]it : ")

        if mode == "X":
            return

        if mode == "E":
            msg = input("Message (8x): ")
            print(Enc(msg, KeyGenAuto()))
        elif mode == "D":
            print(Dec("des.enc", KeyGen()))

        print()

main()
