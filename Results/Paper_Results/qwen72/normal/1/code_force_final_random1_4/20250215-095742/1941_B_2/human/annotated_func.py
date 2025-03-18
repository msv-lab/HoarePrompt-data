#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of an integer n where 3 ≤ n ≤ 2 · 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_j ≤ 10^9, representing the elements of the array. The sum of the values of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: After all iterations of the loop, `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 3 ≤ n ≤ 2 · 10^5, and for each test case, the variable `a` has been assigned the value of `n` (the number of elements in the list `b`). For each list `b` of integers read from the input, if the first element of `b` is odd and the second element is not equal to the first element plus 2, or if the last element of `b` is odd and the second-to-last element is not equal to the last element plus 2, then "NO" is printed. Otherwise, "YES" is printed. The loop iterates `t` times, processing each test case independently.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a list of `n` integers. For each test case, it checks if the first element of the list is odd and the second element is not equal to the first element plus 2, or if the last element of the list is odd and the second-to-last element is not equal to the last element plus 2. If either condition is true, it prints "NO"; otherwise, it prints "YES". The function processes up to 10,000 test cases, with each list containing between 3 and 200,000 integers, and the sum of the lengths of all lists does not exceed 200,000.

