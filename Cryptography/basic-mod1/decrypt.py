import sys

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"

with open(sys.path[0] + "/message.txt", "r") as f:
    split_message = f.read().split(" ")

    print("picoCTF{", end='')
    for i in split_message:
        print(alphabet[int(i) % 37], end='')
    print("}")

