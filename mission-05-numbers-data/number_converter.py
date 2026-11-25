decimal_input = input("Enter a positive decimal number: ")
number = int(decimal_input)

binary_value = bin(number)
hex_value = hex(number)

print("Binary:", binary_value)
print("Hexadecimal:", hex_value)