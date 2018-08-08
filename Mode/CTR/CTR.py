def SubKeyGen(master_key, n_round=16):
    sub_key = master_key

    for i in range(n_round):
        sub_key = (sub_key * 2 + 1) % 65535
        yield sub_key


def Enc_CTR(plain, key, ctr):
    cipher = bytearray([ctr // 256, ctr % 256])

    for i in range(0, len(plain), 2):
        ctr = (ctr + 1) % 65535

        for sub_key in SubKeyGen(key):
            ctr = ctr ^ sub_key

        c = (ord(plain[i]) * 256 + ord(plain[i + 1])) ^ ctr

        cipher.append(c // 256)
        cipher.append(c % 256)

    with open("cipher.enc", "wb") as fout:
        fout.write(cipher)


def Dec_CTR(key):
    plain = ""

    with open("cipher.enc", "rb") as fin:
        cipher = fin.read()

        ctr = int.from_bytes(cipher[0:2], "big")

        for i in range(2, len(cipher), 2):
            ctr = (ctr + 1) % 65535

            for sub_key in SubKeyGen(key):
                ctr ^= sub_key

            p = ctr ^ int.from_bytes(cipher[i:i + 2], "big")

            plain += chr(p // 256)
            plain += chr(p % 256)

    return "[*] plaintext is \"{}\"".format(plain)
