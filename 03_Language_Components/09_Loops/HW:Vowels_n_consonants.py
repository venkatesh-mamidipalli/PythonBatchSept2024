# input
letter = input("Enter a character: ").lower()

if len(letter) == 1 and letter.isalpha():
    # Check if the letter is a vowel
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
else:
    print("Please enter an alphabet")
