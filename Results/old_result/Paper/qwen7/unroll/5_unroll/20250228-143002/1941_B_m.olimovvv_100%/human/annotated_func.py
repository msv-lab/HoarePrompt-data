#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers such that 0 ≤ a_j ≤ 10^9 for each element a_j in the list. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        for i in range(0, a - 2):
            if b[i] < 0:
                print('NO')
                break
            b[i + 1] -= b[i] * 2
            b[i + 2] -= b[i]
            b[i] -= b[i]
        else:
            if b[-1] != 0 or b[-2] != 0:
                print('NO')
            else:
                print('YES')
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers such that 0 ≤ a_j ≤ 10^9 for each element a_j in the list. After executing the loop, if for every test case, the conditions `b[-1] == 0` and `b[-2] == 0` are met without encountering any negative value in the first part of the loop, then the output will be 'YES' for that test case; otherwise, it will be 'NO'. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( t \), an integer \( n \), and a list \( a \) of \( n \) non-negative integers. It then checks if all elements in the list \( a \) are non-negative and if certain arithmetic operations performed on consecutive elements result in specific conditions being met. If these conditions are satisfied for all test cases, it outputs 'YES'; otherwise, it outputs 'NO'.

