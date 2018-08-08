def SubKeyGen(master_key, n_round=16):
    sub_key = master_key

    for i in range(n_round):
        sub_key = (sub_key * 2 + 1) % 65535
        yield sub_key


def Enc_OFB(plain, key, iv):
    pre_c = iv
    cipher = bytearray([iv // 256, iv % 256])

    for i in range(0, len(plain), 2):
        c = pre_c

        for sub_key in SubKeyGen(key):
            c = c ^ sub_key

        pre_c = c
        c = c ^ ord(plain[i]) * 256 + ord(plain[i + 1])

        cipher.append(c // 256)
        cipher.append(c % 256)

    with open("cipher.enc", "wb") as fout:
        fout.write(cipher)


def Dec_OFB(key):
    plain = ""

    with open("cipher.enc", "rb") as fin:
        cipher = fin.read()
        pre_p = int.from_bytes(cipher[0:2], "big")

        for i in range(2, len(cipher), 2):
            p = pre_p

            for sub_key in SubKeyGen(key):
                p ^= sub_key

            pre_p = p
            p = p ^ int.from_bytes(cipher[i:i + 2], "big")

            plain += chr(p // 256)
            plain += chr(p % 256)

    return "[*] plaintext is \"{}\"".format(plain)
