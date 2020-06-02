# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = input("\nEnter a number:\n")

if int(number)%10 == 0:
    print("\nThis number is a multiple of 10.")
else:
    print("\nThis number is not a multiple of 10.")