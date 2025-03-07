#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5), followed by a list of n integers a_1, a_2, \ldots, a_n where 0 ≤ a_i < n. It is also given that the sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: After the loop executes all iterations, `cntl[i]` for all `i` will represent the frequency of the integer `i` in the list `a`. If `cntl[0]` is greater than or equal to 2, it will be adjusted by subtracting `2 * n` and setting `c` to the minimum of 2 and the updated value of `cntl[0] - (2 * n)`. The loop will continue until `c` is 0 or `j` equals `n + 1`. In the final state, `j` will be `n + 1`, and the loop will terminate.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) followed by a list of \( n \) integers. For each test case, it calculates the frequency of each integer in the list and determines a specific integer \( j \) based on certain conditions. If the integer 0 appears at least twice, it adjusts the count and finds the smallest integer \( j \) that meets the criteria. The function prints the value of \( j \) for each test case or 0 if no such \( j \) exists.

