# Feistel構造
def feistel(m, ks, is_enc):
    """
    is_encがTrueなら，Feistel構造に従って，平文mをサブ鍵ksを用いて，暗号文を生成する．
    is_encがFalseなら，暗号文mをサブ鍵ksを逆順にしたものを用いて，平文を復号する．
    """

    def xor(bin_a, bin_b):
        """
        2進数列bin_aとbin_bの排他的論理和をとる
        """
        result = ""
        for a, b in zip(bin_a, bin_b):
            result += str((int(a) + int(b)) % 2)

        return result

    def f(subkey, R):
        """
        ラウンド関数
        subkeyの数字分，Rに対して右循環シフトを行う
        """
        for i in range(subkey):
            R = R[-1] + R[:-1]

        return R

    # 復号ならサブ鍵を逆順にする
    if not is_enc:
        ks.reverse()

    # メッセージ長が奇数なら0を付加する
    if len(m) % 2 != 0:
        m += "0"

    # mを左部分Lと右部分Rに分割する
    middle = len(m)//2
    L = m[:middle]
    R = m[middle:]

    # Feistel構造に従って，データを暗号化
    for i in range(len(ks)):
        print("[ROUND {}] {} | {}".format(i, L, R))
        L_next = R
        R_next = xor(L, f(ks[i], R))

        L = L_next
        R = R_next

    print("[ROUND {}] {} | {}\n".format(len(ks), R, L))
    return R + L

def ascii_to_bin(text):
    """
    ASCII文字列textを7桁の2進数表記に変換する
    """
    binary = ""

    for letter in text:
        # "0b"の除去
        tmp_b = str(bin(ord(letter)))[2:]

        # 7桁に満たない場合は，先頭をゼロ埋めする
        if len(tmp_b) < 7:
            tmp_b = ("0" * (7 - len(tmp_b))) + tmp_b

        binary += tmp_b

    return binary

def bin_to_ascii(binary):
    """
    2進数列binaryをASCII文字列に変換する
    """
    text = ""
    idx = 0

    # ASCII文字列への変換を7桁ごとに行う
    while idx + 7 < len(binary):
        text += chr(int(binary[idx:idx+7], base=2))
        idx += 7

    return text


def main():
    while True:
        mode = input("[E]nc [D]ec e[X]it >> ")

        if mode == "X":
            return

        msg = input("[Message] >> ")
        subkeys = list(map(int, input("[subkeys] >> ").split()))
        print()

        # 暗号化(クリップボードに暗号文のバイナリがコピーされる)
        if mode == "E":
            msg_code = ascii_to_bin(msg)
            cipher_code = feistel(msg_code, subkeys, True)
            cipher = bin_to_ascii(cipher_code)

            print("[Ciphertext Raw] {}".format(cipher_code))
            print("[Ciphertext] {}\n".format(cipher))

        # 復号
        elif mode == "D":
            plain_code = feistel(msg, subkeys, False)
            plain = bin_to_ascii(plain_code)

            print("[Plaintext Raw] {}".format(plain_code))
            print("[Plaintext] {}\n".format(plain))

main()
