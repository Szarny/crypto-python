import base64
import pyperclip

# 鍵生成アルゴリズム
def KeyGen():
    key = int(input("Key : "))
    return key

class Stream:
    def __init__(self, seed):
        self.a = seed
        self.b = 12345
        self.c = 54321

    # 乱数を返す
    def out(self):
        self.a = ((self.a * self.b + self.c) % self.c) % 256
        return self.a

# 暗号化アルゴリズム
def Enc(plain, key):
    stream = Stream(key)
    cipher = b""

    for p in plain:
        cipher += base64.b64encode((ord(p) ^ stream.out()).to_bytes(2, "little"))
    
    with open("stream.enc", "wb") as f:
        f.write(cipher)

    return cipher


# 復号アルゴリズム
def Dec(filename, key):
    stream = Stream(key)
    plain = ""

    with open(filename, "rb") as f:
        cipher = f.read()

        for i in range(0, len(cipher), 4):
            c = cipher[i:i + 4]
            plain += chr(int.from_bytes(base64.b64decode(c), "little") ^ stream.out())
        
    return plain

def main():
    while True:
        mode = input("[E]nc [D]ec e[X]it : ")

        if mode == "X":
            return

        if mode == "E":
            msg = input("Message : ")
            print(Enc(msg, KeyGen()))
        elif mode == "D":
            print(Dec("stream.enc", KeyGen()))

        print()

main()
