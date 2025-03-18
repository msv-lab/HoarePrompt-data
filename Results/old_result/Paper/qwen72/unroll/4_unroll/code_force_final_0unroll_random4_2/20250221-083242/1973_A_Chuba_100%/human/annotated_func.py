#State of the program right berfore the function call: The function should take three integers p_1, p_2, and p_3 as input, where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, representing the scores of the three players, sorted in non-decreasing order.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: The loop will execute `t` times, and for each iteration, it will read three integers from the input, calculate the result based on the given conditions, and print either `-1` or the calculated result. The values of `p_1`, `p_2`, and `p_3` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three integers from the input, which are expected to be in non-decreasing order. It then calculates a result based on these integers and prints either `-1` if the sum of the integers is odd, or a calculated value if the sum is even. The function does not modify the input values and does not return any value. After the function concludes, `t` test cases have been processed, and the corresponding results have been printed.

