#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2 · 10^5, representing the number of containers. a is a list of n integers where 0 ≤ a_i ≤ 10^9, representing the initial amounts of water in the containers. The sum of a_i is divisible by n, and the sum of n over all test cases does not exceed 2 · 10^5.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        arr.sort()
        
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
            print('YES')
        else:
            print('NO')
        
    #State: `t` is an input integer where 1 ≤ t ≤ 10^4, `n` is an input integer where 1 ≤ n ≤ 2 · 10^5, `a` is a list of `n` integers where 0 ≤ a_i ≤ 10^9, the sum of a_i is divisible by n, and the sum of n over all test cases does not exceed 2 · 10^5, `_` is `t - 1`, and for each test case, `arr` is a sorted list of integers read from the input. For each test case, if all elements in `arr` are in non-decreasing order, the output is 'YES'. Otherwise, the output is 'NO'.
#Overall this is what the function does:The function `func_1` reads multiple test cases from the standard input. For each test case, it reads the number of containers `n` and a list of `n` integers representing the initial amounts of water in the containers. It sorts the list and checks if the elements are in non-decreasing order. If they are, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function completes, and the state of the program includes the printed results for each test case.

