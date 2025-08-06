# PEDMAS or BODMAS rule
x = (10 + 3) * 3 ** 2 # Paranthesis part is executed first
print(x)

x = 10 + 3 ** 2 # Then the exponentiation (**) part
print(x)

x = 10 + 3 * 3 / 3 ** 2 # Then division or multiplication part
print(x)

x = 10 + 3 - 6 / 4 * 7 ** 2 # Then addition or subtraction part 
print(x)