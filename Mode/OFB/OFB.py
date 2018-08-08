def SubKeyGen(master_key, n_round=16):
    sub_key = master_key

    for i in range(n_round):
        sub_key = (sub_key * 2 + 1) % 65535
        yield sub_key


def Enc_OFB():
    pass


def Dec_OFB():
    pass
