# this exercise wants me to write a program that tests whether a given letter is a vowel.


def vowel_test(letter):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    return letter in vowels


print(vowel_test(input("Enter letter: ")))
