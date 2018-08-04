import random

# 鍵生成アルゴリズム
def KeyGen():
    return int(input("Key : "))

# 暗号化アルゴリズム
def Enc(plain, R):
  alphabets = "abcdefghijklmnopqrstuvwxyz"
  c = ""

  for start_idx in range(R):
    c += plain[start_idx::R]

    for i in range(R - len(plain[start_idx::R])):
      c += random.choice(alphabets)

  return c

# 復号アルゴリズム 
def Dec(cipher, R): 
  p = ""
  
  for start_idx in range(R):
    p += cipher[start_idx::R]
  
  return p
  
def Attack(msg):
    for key in range(1, len(msg)):
        if len(msg) % key == 0:
            print("Key={} : {}".format(key, Dec(msg, key)))

def main():
    while True:
        mode = input("[E]nc [D]ec [A]ttack e[X]it : ")

        if mode == "X":
            return

        msg = input("Message : ")

        if mode == "E":
            print(Enc(msg, KeyGen()))
        elif mode == "D":
            print(Dec(msg, KeyGen()))
        elif mode == "A":
            Attack(msg)

        print("")

main()
