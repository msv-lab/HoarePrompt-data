#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 3 ≤ n ≤ 2 · 10^5, representing the number of elements in the array. The array a consists of n integers a_1, a_2, ..., a_n where 0 ≤ a_j ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: For each of the `t` test cases, the program checks if the conditions for the array `b` (as described in the loop) are met. If the conditions are met for any test case, 'YES' is printed; otherwise, 'NO' is printed. After all iterations, `t` remains an integer within the range 1 ≤ t ≤ 10^4, and the values of `a` and `b` for each test case are processed according to the loop logic.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` and an array `b` of `n` integers. For each test case, it checks if the first element of `b` is odd and the second element is not exactly two more than the first, or if the last element of `b` is odd and the second-to-last element is not exactly two more than the last. If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function completes, and the state of the program reflects the results of these checks for each test case.

