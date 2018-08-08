def SubKeyGen(master_key, n_round):
    sub_key = master_key

    for i in range(n_round):
        sub_key = (sub_key * 2 + 1) % 65535
        yield sub_key

def Enc_ECB(plain, key):
    cipher = bytearray([])

    for i in range(0, len(plain), 2):
        c = ord(plain[i]) * 256 + ord(plain[i + 1])

        for sub_key in SubKeyGen(key, 16):
            c = c ^ sub_key

        cipher.append(c // 256)
        cipher.append(c % 256)
    
    print(cipher)

    with open("cipher.enc", "wb") as fout:
        fout.write(cipher)

def Dec_ECB(key):
    plain = ""

    with open("cipher.enc", "rb") as fin:
        cipher = fin.read()

        for i in range(0, len(cipher), 2):
            c = int.from_bytes(cipher[i:i + 2], "big")
            p = c
            
            for sub_key in SubKeyGen(key, 16):
                p ^= sub_key

            plain += chr(p // 256)
            plain += chr(p % 256)
        
    return "[*] plaintext is \"{}\"".format(plain)
    