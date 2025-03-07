#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a is a list of n non-negative integers where each integer is less than n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a is a list of n non-negative integers where each integer is less than n. After executing the loop, if cntl[0] is not zero, then the minimum value of j (where 1 ≤ j ≤ n) such that cntl[j] is less than 2 is printed; otherwise, 0 is printed. The sum of all n values across all test cases does not exceed 2⋅10^5.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list \( a \) of \( n \) non-negative integers. For each test case, it counts the occurrences of each integer in the list \( a \). If the count of zeros is not zero, it finds and prints the smallest index \( j \) (where \( 1 \leq j \leq n \)) such that the count of \( j \) is less than 2; otherwise, it prints 0. The function does not return any value but prints the result for each test case.

