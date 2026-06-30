#Q16 Lowercase to uppercase using ord() and chr() functions

letter = input("Enter a lowercase letter: ")

#convert to ASCII
ascii_value = ord(letter)

#convert lowercase to uppercase
uppercase = chr(ascii_value - 32)

print("Uppercase Letter:", uppercase)