# Q1: Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for l in word:
        if l in vowels:
            count += 1
    return count

# print("Vowels in Apple: ", count_vowels("Apple"))

# Q2: Iterate through the following list of animals and print each one in all caps.

animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

# Q3: Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for i in range(1, 21):
    if i % 2 == 0:
        print(i, " is even.")
    else:
        print(i, " is odd.")

# Q4: Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

def sum_of_integers(a, b):
    return a + b

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print(f"The sum of {a} and {b} is {sum_of_integers(a, b)}")