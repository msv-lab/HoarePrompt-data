#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with values between 1 and 1000 inclusive.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    max_lemons = min(a, b // 2, c // 4)
    total_fruits = max_lemons * 1 + max_lemons * 2 + max_lemons * 4
    print(total_fruits)
#Overall this is what the function does:The function accepts three positive integers `a`, `b`, and `c` representing the number of lemons, apples, and pears respectively, each between 1 and 1000 inclusive. It calculates the maximum number of lemons that can be made based on the number of apples (where each lemon requires 2 apples) and pears (where each lemon requires 4 pears). The function then computes the total number of fruits based on the maximum possible lemons, which is the sum of lemons, twice the number of lemons for apples, and four times the number of lemons for pears, and prints this total. However, it does not return a value; it simply prints the result.

