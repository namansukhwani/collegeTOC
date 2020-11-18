# for 8-bit number
st = input("Enter a binary number:")
n = int(st, 2)
num = (255 + 1 - n)
print(num)
print(bin(num).replace("0b", ""))


# for 16-bit number
st = input("Enter a binary number:")
n = int(st, 2)
num = (65535 + 1 - n)
print(num)
print(bin(num).replace("0b", ""))
