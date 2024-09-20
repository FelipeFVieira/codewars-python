"""

Kata description: Create a function that takes an integer
as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

Kata Level: 8 Kyu

Link: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
"""
def evenOrOdd(number: int) -> str:
    return 'this number is even!' if number % 2 ==0 else 'this number is odd!'

def main() -> None:
    print(evenOrOdd(2))   # this number is even!
    print(evenOrOdd(3))   # this number is odd!
    print(evenOrOdd(-1))  # this number is odd!
    print(evenOrOdd(0))   # this number is even!
    print(evenOrOdd(5))   # this number is odd!

if __name__ == '__main__':
    main()

