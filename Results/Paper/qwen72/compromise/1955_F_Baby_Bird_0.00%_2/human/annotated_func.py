#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i is a list of four integers where 0 <= p_i <= 200.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: The value of `t` is unchanged, and for each test case, the output is the sum of the integer division of the modified list `p` by 2, plus 1 if the first three elements of the modified list `p` were all odd before the modification. The modified list `p` consists of even numbers derived from the original list by subtracting the remainder when divided by 2.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case is a list of four integers between 0 and 200. For each test case, it modifies the list such that all elements become even by subtracting their remainder when divided by 2. It then calculates and prints a result for each test case, which is the sum of the modified list divided by 2, plus 1 if the first three elements of the original list were all odd. The function does not return any value; it only prints the results. The value of `t` (the number of test cases) is unchanged after the function concludes.

