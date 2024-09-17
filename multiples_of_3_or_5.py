"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

"""

def solution( limit_num: int ) -> int :
    
    total: int = 0

    if limit_num < 0:
        return 0

    total = sum(num for num in range(limit_num) if num % 3 == 0 or num % 5 == 0)
    return total

def main() -> None:
    print(solution(-9)) # if number is negative return 0, so this is returning 0.
    print(solution(10)) # 3, 5, 6, 9 = 23
    print(solution(15)) # 3, 5, 6, 9, 10, 12 = 45
    print(solution(20)) # 3, 5, 6, 9, 10, 12, 15, 18 = 78

if __name__ == "__main__":
    main()
