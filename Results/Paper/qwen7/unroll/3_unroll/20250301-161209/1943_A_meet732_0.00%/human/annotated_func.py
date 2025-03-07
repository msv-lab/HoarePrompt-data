#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5), an integer representing the size of the array a, followed by a line containing n integers a_1, a_2, \ldots, a_n (0 ≤ a_i < n), where the sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5), an integer representing the size of the array a, followed by a line containing n integers a_1, a_2, \ldots, a_n (0 ≤ a_i < n), where the sum of n over all test cases does not exceed 2 ⋅ 10^5. After executing the loop, if cntl[0] is not zero, then the minimum value of j for which cntl[j] is less than 2 or j equals n is printed; otherwise, 0 is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` representing the size of an array `a`, followed by `n` integers `a_1, a_2, ..., a_n`. For each test case, it counts the occurrences of each integer in the array `a`. If the count of `0` is not zero, it finds the smallest index `j` (starting from 1) where the count of `j` is less than 2 or reaches the end of the array. If the count of `0` is zero, it prints `0`. The function does not return any value but prints the result for each test case.

