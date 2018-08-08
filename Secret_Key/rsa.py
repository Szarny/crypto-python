# RSA

import math
import random

def gcd(a, b):
    large = max(a, b)
    small = min(a, b)

    if large % small == 0:
        return small
    else:
        return gcd(small, large % small)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def euler_function(n):
    n_coprime = 0

    for i in range(1, n):
        if gcd(i, n) == 1:
            n_coprime += 1

    return n_coprime

def choose_random_prime(limit):
    primes = []

    for target in range(2, limit):
        is_prime = True

        for divisor in range(2, math.floor(math.sqrt(target))+1):
            if target % divisor == 0:
                is_prime = False

        if is_prime:
            primes.append(target)

    return random.choice(primes)

def choose_random_e(euler_N):
    while True:
        tmp_e = random.randint(2, euler_N-1)

        if gcd(tmp_e, euler_N) == 1:
            return tmp_e

def choose_d(m, n):
    r = {0: m, 1: n}
    u = {0: 1, 1: 0}
    v = {0: 0, 1: 1}
    q = {}
    i = 2

    while True:
        q[i] = math.floor(r[i-2] / r[i-1])
        r[i] = r[i-2] - (q[i] * r[i-1])

        if r[i] == 0:
            break

        u[i] = u[i-2] - (q[i] * u[i-1])
        v[i] = v[i-2] - (q[i] * v[i-1])

        i += 1

    u, v, d = u[i-1], v[i-1], r[i-1]

    return u

def RSAGen(limit):
    """
    公開鍵pkと秘密鍵skを生成する

    [手順]
    1. kbitの素数p,qを生成する
    2. N = pq とする
    3. GCD(φ(N), e) = 1 となる e(1 < e < φ(N)) をランダムに選ぶ
    4. ed = 1 (mod φ(N)) となるd(d > 0)を計算する
    5. pk = (N, e), sk = d とする
    """

    p = ""
    q = ""

    N = ""
    euler_N = ""

    e = ""
    d = ""

    pk = ""
    sk = ""

    p = choose_random_prime(limit)
    q = choose_random_prime(limit)
    N = p * q

    print("*** parameters ***")
    print("p = {}, q = {}, N = {}".format(p, q, N))

    euler_N = euler_function(N)
    print("euler_N = {}".format(euler_N))

    e = choose_random_e(euler_N)
    d = choose_d(e, euler_N)

    while d <= 0:
        d += euler_N

    print("e = {}, d = {}".format(e, d))

    pk = {"N": N, "e": e}
    sk = d

    print("******************")

    return pk, sk

def Enc(m, pk):
    """
    メッセージmを公開鍵pkによって暗号化し，暗号文cを生成する
    """

    return (m**pk["e"]) % pk["N"]

def Dec(c, sk, pk):
    """
    暗号文cを秘密鍵skによって復号し，平文mを導く
    """

    return (c**sk) % pk["N"]

def main():
    print("[Usage] Enc,Dec: [0-9]+ -> [0-9]+\n")
    while True:
        mode = input("exit? >> ")

        if mode == "y":
            return

        pk, sk = RSAGen(int(input("[Limit of p and q] >> ")))

        msg = -1
        while not (0 <= msg < pk["N"]):
            msg = int(input("[Message (0 <= msg < {})] >> ".format(pk["N"])))

        cipher = Enc(msg, pk)
        print("[Ciphertext] {}".format(cipher))

        plain = Dec(cipher, sk, pk)
        print("[Plaintext] {}".format(plain))

        print()

main()
