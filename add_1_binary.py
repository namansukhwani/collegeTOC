bi = input("Enter a binary number: ")
n = int(bi, 2)
print("Before addition of 1 in decimal: ", n)
print("Before addition of 1 in binary: ", bi)
n += 1
bi = bin(n).replace("0b", "")
n = int(bi, 2)
print("After addition of 1 in decimal: ", n)
print("After addition of 1 in binary: ", bi)
