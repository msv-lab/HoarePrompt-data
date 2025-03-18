#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each element a_j satisfies 0 <= a_j <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: A sequence of 'YES' or 'NO' for each test case, based on whether the list can be reduced to zeros following the specified rules.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it determines if the list can be reduced to all zeros by applying specific operations: subtracting twice the current element from the next element and the current element from the element after next, while ensuring no element becomes negative. It outputs 'YES' if the list can be reduced to all zeros, otherwise 'NO'.

