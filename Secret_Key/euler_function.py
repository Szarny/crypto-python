def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def euler_function(k):
    n_prime = 0

    for v in range(1, k):
        if gcd(k, v) == 1:
            n_prime += 1

    return n_prime


def main():
    k = int(input("k > "))
    print(euler_function(k))


main()