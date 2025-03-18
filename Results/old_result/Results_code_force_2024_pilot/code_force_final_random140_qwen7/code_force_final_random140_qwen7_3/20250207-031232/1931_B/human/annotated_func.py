#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and there are n integers a_1, a_2, ..., a_n such that 0 ≤ a_i ≤ 10^9 and the sum of a_i is divisible by n. Additionally, the sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: `t` is greater than 2 and less than or equal to 10^4 - 2, `n` is an integer input from the user, `arr` is a sorted list of integers obtained from splitting the input string and converting each element to an integer, `n` is the new integer input from the user after each iteration. The list `arr` remains sorted after the if-else block executes in each iteration.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t`, followed by an integer `n` and a list of `n` integers. It then sorts the list of integers and checks if the list is already sorted in non-decreasing order. If the list is sorted, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

