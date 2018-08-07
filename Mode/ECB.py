def Enc_ECB(plain, key):
    cipher = bytearray([])

    for p in plain:
        cipher.append(ord(p) ^ key)

    with open("cipher.enc", "wb") as fout:
        fout.write(cipher)

def Dec_ECB(key):
    plain = ""

    with open("cipher.enc", "rb") as fin:
        cipher = fin.read()

        for i in range(len(cipher)):
            c = cipher[i]
            p = c ^ key
            plain += chr(p)
        
    return "[*] plaintext is \"{}\"".format(plain)