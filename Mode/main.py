from ECB import Enc_ECB, Dec_ECB

def KeyGen():
    key = ""

    while not key.isdigit():
        key = input("Key(int) : ")

    return int(key)

def Enc(plain, key, mode):
    if mode == "ECB":
        Enc_ECB(plain, key)
    elif mode == "CBC":
        Enc_CBC(plain, key)
    elif mode == "CFB":
        Enc_CFB(plain, key)
    elif mode == "OFB":
        Enc_OFB(plain, key)
    elif mode == "CTR":
        Enc_CTR(plain, key)
    else:
        return "[*] Invalid mode"

    return "[*] Cipher is stored at cipher.enc"


def Dec(key, mode):
    if mode == "ECB":
        print(Dec_ECB(key))
    elif mode == "CBC":
        print(Dnc_CBC(key))
    elif mode == "CFB":
        print(Dnc_CFB(key))
    elif mode == "OFB":
        print(Dnc_OFB(key))
    elif mode == "CTR":
        print(Dnc_CTR(key))
    else:
        return "[*] Invalid mode"

def main():
    while True:
        mode = input("[E]nc [D]ec e[X]it : ")

        if mode == "X":
            return

        if mode == "E":
            msg = input("Message : ")
            mode = input("Mode (ECB/CBC/CFB/OFB/CTR) : ")
            print(Enc(msg, KeyGen(), mode))
        elif mode == "D":
            mode = input("Mode (ECB/CBC/CFB/OFB/CTR) : ")
            print(Dec(KeyGen(), mode))

        print()

main()
