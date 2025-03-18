#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_j ≤ 10^9 for each element a_j in the list. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: After all iterations of the loop have finished, `t` will be the total number of test cases (an integer greater than 0), `a` will be the last input integer received, and `b` will be the list of integers corresponding to the last input string split by spaces. For each test case, if the first element of `b` is an odd number and does not differ from the second element by 2, or if the last element of `b` is an odd number and does not differ from the second last element by 2, the output will be 'NO'. Otherwise, the output will be 'YES'.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n` and a list of `n` integers `a`. For each test case, it checks if the first element of the list `a` is an odd number differing from the second element by 2, and if the last element of the list `a` is an odd number differing from the second last element by 2. If either condition fails for any test case, it prints 'NO' for that test case; otherwise, it prints 'YES'. The function does not return anything but prints 'YES' or 'NO' for each test case.

