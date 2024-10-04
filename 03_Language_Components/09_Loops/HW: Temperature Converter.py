user_input = input("Enter input: ").strip()

if user_input[-1].upper() == 'C':
    celsius = float(user_input[:-1])
    fahrenheit = (celsius * 9/5) + 32
    print(f"Output: {fahrenheit:.2f}F")
elif user_input[-1].upper() == 'F':
    fahrenheit = float(user_input[:-1])
    celsius = (fahrenheit - 32) * 5/9
    print(f"Output: {celsius:.2f}C")
else:
    print("Invalid input")
