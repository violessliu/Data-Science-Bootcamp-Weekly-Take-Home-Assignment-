# 1. Write a program that takes a word as an input and print the number of vowels in the word.

word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print(f"Number of vowels in '{word}': {count}")

# 2. Iterate through the following list of animals and print each one in all caps.

animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())

# 3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# 4. Write a program to check if a string is a palindrome or not.

text = input("Enter a string: ")
if text == text[::-1]:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")

# 5. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

def sum_of_integers(a, b):
    return a + b

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
result = sum_of_integers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")
