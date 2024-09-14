alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

inputi = input("Enter a sentence: ").lower()  

input_set = set(inputi)

missing_letters = alphabet-input_set

if len(missing_letters) == 0:
    print("The input is a pangram.")
else:
    print("The input is not a pangram.")
