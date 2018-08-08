def SubKeyGen(master_key, n_round=16):
    sub_key = master_key

    for i in range(n_round):
        sub_key = (sub_key * 2 + 1) % 65535
        yield sub_key

def Enc_CBC(plain, key, iv):
    cipher = bytearray([iv // 256, iv % 256])

    for i in range(2, len(plain)+2, 2):
        c = ord(plain[i-2]) * 256 + ord(plain[i-1])

        c = c ^ int.from_bytes(cipher[i-2:i], "big")

        for sub_key in SubKeyGen(key):
            c = c ^ sub_key

        cipher.append(c // 256)
        cipher.append(c % 256)

    with open("cipher.enc", "wb") as fout:
        fout.write(cipher)

def Dec_CBC(key):
    plain = ""

    with open("cipher.enc", "rb") as fin:
        cipher = fin.read()

        for i in range(2, len(cipher), 2):
            p = int.from_bytes(cipher[i:i + 2], "big")
            
            for sub_key in SubKeyGen(key):
                p ^= sub_key

            p = p ^ int.from_bytes(cipher[i-2:i], "big")

            plain += chr(p // 256)
            plain += chr(p % 256)
        
    return "[*] plaintext is \"{}\"".format(plain)
