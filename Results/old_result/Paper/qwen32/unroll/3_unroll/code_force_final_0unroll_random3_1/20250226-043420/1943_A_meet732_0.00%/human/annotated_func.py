#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2 ⋅ 10^5) representing the size of the array a. The next line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n) representing the elements of the array a. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: 2 2
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and an array `a` of `n` integers. It then determines and prints a value based on the frequency of elements in the array. Specifically, it finds the smallest index `j` such that the number of elements less than 2 up to that index is exhausted, starting from the count of zeros in the array. If there are no zeros, it immediately prints 0.

