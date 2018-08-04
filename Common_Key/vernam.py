# Vernam暗号
# Dec(key, Enc(key, m)) = Dec(key, key(+)m) = key(+)key(+)m = 0(+)m = m

import random

def xor(a, b):
    return str((int(a) + int(b)) % 2)

def KeyGen(n):
    """
    nbitの共通鍵を生成する
    """

    key = ""
    while len(key) != n:
            key += random.choice(["0", "1"])
    print("[Key] {}".format(key))
    return key

def Enc(m, key):
    """
    メッセージmを鍵keyによって暗号化し，暗号文cを生成する
    """
    c = ""
    for m_bit, k_bit in zip(m, key):
        c += xor(m_bit, k_bit)
    return c

def Dec(c, key):
    """
    暗号文cを鍵keyによって復号し，平文mを導く
    """
    m = ""
    for c_bit, k_bit in zip(c, key):
        m += xor(c_bit, k_bit)
    return m

def main():
    while True:
        mode = input("[E]nc [D]ec e[X]it >> ")

        if mode == "X":
            return

        msg = input("[Message] >> ")

        if mode == "E":
            print("[Ciphertext] {}".format(Enc(msg, KeyGen(len(msg)))))
        elif mode == "D":
            key = ""
            while len(key) != len(msg):
                key = input("[Key] >> ")
            print("[Plaintext] {}".format(Dec(msg, key)))

        print()

main()
