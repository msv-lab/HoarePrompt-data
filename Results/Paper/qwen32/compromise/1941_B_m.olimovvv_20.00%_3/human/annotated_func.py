#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each element a_j satisfies 0 <= a_j <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: A series of 'YES' or 'NO' printed for each test case, where 'YES' is printed if the first element is even or the second element is exactly two more than the first element when the first is odd, and the last element is even or the second-to-last element is exactly two less than the last element when the last is odd. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it checks a list of integers and prints 'YES' if the first element is even or the second element is exactly two more than the first element when the first is odd, and the last element is even or the second-to-last element is exactly two less than the last element when the last is odd. Otherwise, it prints 'NO'.

