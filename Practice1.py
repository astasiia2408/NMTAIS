from typing import Optional

# Task 1: Check if an argument is a number and return if it's even or odd
def check_even_odd(arg: any) -> str:
    if isinstance(arg, (int, float)):
        return "even" if arg % 2 == 0 else "odd"
    return ""

# Task 2: Find the sum of the first five prime numbers
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_first_five_primes() -> int:
    primes = []
    num = 1
    while len(primes) < 5:
        if is_prime(num):
            primes.append(num)
        num += 1
    return sum(primes)

# Task 3: Sum of a series of numbers with increasing ones
def sum_of_series(n: int) -> int:
    total_sum = 0
    current_number = 0
    for i in range(n):
        current_number = current_number * 10 + 1
        total_sum += current_number
    return total_sum

# Task 4: Find the nth Fibonacci number
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Task 5: Reverse a string
def reverse_string(s: str) -> str:
    return s[::-1]

# Task 6: Calculate the factorial of a number
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Task 7: Frequency analysis of characters in a string
def frequency_analysis(s: str) -> dict[str, int]:
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

# Task 8: Find the minimum element in a list
def find_minimum(lst: list[int]) -> Optional[int]:
    if not lst:
        return None
    return min(lst)

# Task 9: Check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Task 10: Caesar Cipher
def caesar_cipher(s: str, shift: int) -> str:
    result = []
    for char in s:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result.append(chr((ord(char) - offset + shift) % 26 + offset))
        else:
            result.append(char)
    return ''.join(result)