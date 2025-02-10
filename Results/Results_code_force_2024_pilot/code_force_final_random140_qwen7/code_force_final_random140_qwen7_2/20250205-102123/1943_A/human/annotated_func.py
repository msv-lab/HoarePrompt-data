#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5) and an array a of n integers where 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
                    if cntl[j] == 0:
                        print(j)
                        break
                    else:
                        c -= 1
                        if not c:
                            print(j)
                            break
        
    #State: Output State: The list `a` is an empty list, and `cntl` is an array where the value at each index `i` from the original list `a` is increased by 1 for every occurrence of `i` in `a`. If `cntl[0]` was initially 0, it remains 0. If `cntl[0]` was not 0, then `c` is reduced to 0 after processing all elements in `a`, and the loop exits without printing any value other than 0 when `cntl[0]` is 0.
    #
    #In simpler terms, after the loop completes all its iterations, the list `a` will be empty because it has been fully processed. The `cntl` array will contain the count of each integer from the original list `a`, and if `cntl[0]` was initially 0, it will still be 0. If `cntl[0]` was not 0, the loop will exit without printing any specific value other than 0 if `cntl[0]` was 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and an array \( a \) of \( n \) integers. For each test case, it counts the occurrences of each integer in the array \( a \) and stores these counts in the `cntl` array. If the count of the integer 0 in the array \( a \) is zero, it prints 0. Otherwise, it finds the smallest integer \( j \) (other than 0) whose count is less than 2 and prints \( j \). After processing all test cases, the function outputs the results for each case.

