
letter = input("Enter any character:").strip()

if letter in "aeiou":
    print(f"{letter} is a LOWER VOWEL CHARACTER")
elif letter in "AEIOU":
    print(f"{letter} is a UPPER VOWEL CHARACTER")
else:
    print(f"{letter} may be a CONSONANT")



match letter:
    case "a" | "e" | "i" | "o" | "u":
        print(f"{letter} is a LOWER VOWEL CHARACTER")
    case "A" | "E" | "I" | "O" | "U":
        print(f"{letter} is a UPPER VOWEL CHARACTER")
    case _:
        print(f"{letter} may be a CONSONANT")


if letter.lower() in "aeiou":
    print(f"{letter} is a VOWEL CHARACTER")
else:
    print(f"{letter} may be a CONSONANT")


match letter.lower():
    case "a" | "e" | "i" | "o" | "u":  # | for OR operation
        print(f"{letter} is a VOWEL CHARACTER")
    case _:
        print(f"{letter} may be a CONSONANT")