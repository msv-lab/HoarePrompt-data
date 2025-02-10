#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list a contains n non-negative integers such that 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all iterations, the variable `cntl` will be a list where each index `i` (from 0 to `n`) represents the frequency of occurrence of `i` in the list `a`. If `cntl[0]` is 0, it means there are no zeros in the list `a`. Otherwise, `cntl[0]` will be the count of zeros in `a`. The variable `c` will be 0 if `cntl[0]` is 0, otherwise, it will be the minimum of 2 and the count of zeros in `a`. The loop will print the smallest index `j` (from 1 to `n`) that has a count less than 2, or it will print 0 if all indices from 1 to `n` have a count of at least 2.
    #
    #In more detail:
    #- `cntl` will be updated to reflect the frequency of each element in `a`.
    #- If `cntl[0]` is 0, the loop will print 0.
    #- If `cntl[0]` is not 0, the loop will find the smallest index `j` (from 1 to `n`) with a count less than 2 and print it. If no such index exists, it will print the smallest index with a count of exactly 2.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list \( a \) of \( n \) non-negative integers. It calculates the frequency of each number in the list \( a \) and determines the smallest index \( j \) (from 1 to \( n \)) that appears fewer than twice in the list. If no such index exists, it prints 0. If the number 0 does not appear in the list, it directly prints 0. Otherwise, it prints the smallest index of 0 if it appears fewer than twice, or the smallest index of any other number that appears fewer than twice.

