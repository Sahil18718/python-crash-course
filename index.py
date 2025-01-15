# Imports
import math
import random
import os

# Line 1: Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Line 2-6: Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Line 7-10: Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Line 11-15: Generate a list of prime numbers
def prime_numbers(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]

# Line 16-20: Calculate the Fibonacci sequence
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Line 21-25: Write data to a file
def write_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

# Line 26-30: Read data from a file
def read_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f.read()
    return "File does not exist!"

# Line 31-35: Sort a list of numbers
def sort_numbers(numbers):
    return sorted(numbers)

# Line 36-40: Shuffle a list of numbers
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# Line 41-45: Check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Line 46-50: Generate a random password
def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(length))

# Line 51-55: Calculate the sum of numbers in a list
def sum_of_list(lst):
    return sum(lst)

# Line 56-60: Find the maximum number in a list
def max_in_list(lst):
    return max(lst)

# Line 61-65: Simple linear search
def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

# Line 66-70: Binary search
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Line 71-75: Calculate GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Line 76-80: Generate random numbers
def random_numbers(count, start, end):
    return [random.randint(start, end) for _ in range(count)]

# Line 81-85: Find unique elements in a list
def unique_elements(lst):
    return list(set(lst))

# Line 86-90: Count the frequency of elements in a list
def element_frequency(lst):
    frequency = {}
    for element in lst:
        frequency[element] = frequency.get(element, 0) + 1
    return frequency

# Line 91-95: Find the common elements between two lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Line 96-100: Main function to demonstrate usage
def main():
    print("Reversed String:", reverse_string("Hello"))
    print("Factorial of 5:", factorial(5))
    print("Prime Numbers up to 20:", prime_numbers(20))
    print("First 10 Fibonacci Numbers:", fibonacci(10))
    print("Random Password:", generate_password(12))

if __name__ == "__main__":
    main()
