"""

Kata description: Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

Kata Level: 6 Kyu

Link: https://www.codewars.com/kata/526571aae218b8ee490006f4
"""

def count_bits(n: int ) -> int: 

    return bin(n).count("1") if n >= 0 else f"Invalid Number!"

print(count_bits(1234)) # 5
print(count_bits(-1)) # Invalid Number!
print(count_bits(450)) # 4
print(count_bits(255)) # 8