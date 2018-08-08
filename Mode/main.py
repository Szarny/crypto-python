from ECB import Enc_ECB, Dec_ECB

def KeyGen():
    key = ""

    while not key.isdigit():
        key = input("[?] Key(int) : ")

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
        return "[!] Invalid mode"

    return "[*] Cipher is stored at cipher.enc"


def Dec(key, mode):
    if mode == "ECB":
        return Dec_ECB(key)
    elif mode == "CBC":
        return Dec_CBC(key)
    elif mode == "CFB":
        return Dec_CFB(key)
    elif mode == "OFB":
        return Dec_OFB(key)
    elif mode == "CTR":
        return Dec_CTR(key)
    else:
        return "[*] Invalid mode"

def main():
    while True:
        mode = input("[?] [E]nc [D]ec e[X]it : ")

        msg = ""
        enc_mode = ""

        if mode == "X":
            return

        if mode == "E":
            while len(msg) == 0 or len(msg) % 2 != 0:
                msg = input("[?] Message(2x) : ")

            while enc_mode not in ["ECB", "CBC", "CFB", "OFB", "CTR"]:
                enc_mode = input("[?] Mode (ECB/CBC/CFB/OFB/CTR) : ")

            key = KeyGen()

            print()
            print(Enc(msg, key, enc_mode))
        elif mode == "D":
            while enc_mode not in ["ECB", "CBC", "CFB", "OFB", "CTR"]:
                enc_mode = input("[?] Mode (ECB/CBC/CFB/OFB/CTR) : ")

            key = KeyGen()

            print()
            print(Dec(key, enc_mode))

        print()

main()
