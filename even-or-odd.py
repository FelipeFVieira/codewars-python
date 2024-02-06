"""

Kata description: Create a function that takes an integer
as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

"""
def evenOrOdd(number: int) -> str:
    return 'this number is even!' if number % 2 ==0 else 'this number is odd!'

def main() -> None:
    print(evenOrOdd(2))
    print(evenOrOdd(3))
    print(evenOrOdd(-1))
    print(evenOrOdd(0))
    print(evenOrOdd(5))

if __name__ == '__main__':
    main()

