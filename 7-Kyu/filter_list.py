"""
Kata description In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

Kata Level: 7 Kyu

Link: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
"""

def filter_list(test_list) -> list:

    return [i for i in test_list if isinstance(i, int) and i >= 0]

print(filter_list([1, 5, -2, 0, 'Hello World', '2'])) ## == [1, 5, 0]
print(filter_list([3, 9, 99.99, "FelipeFVieira", 2])) ## == [3, 9, 2]
print(filter_list([8,7,20,-100,"CODEWARS","1020"])) ## == [8, 7, 20]