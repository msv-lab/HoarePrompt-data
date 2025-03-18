#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a is a list of n integers where 0 ≤ a_j ≤ 10^9 for each element a_j in the array. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\), `a` is an input integer, `b` is a list of integers obtained from the final input string split on spaces and converted to integers, `num` is the initial value of `t` minus the total number of iterations, `a` is assigned the value of the final input integer, and `b` is updated with the final list of integers.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an array `a` of `n` integers. For each test case, it checks if the first two elements of the array `a` meet specific conditions: both are odd and the second element equals the first element plus two, or if the last two elements meet similar conditions. If either condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

