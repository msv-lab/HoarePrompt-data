#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers such that 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] + T[i - 1])
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: The output will be a series of lists, each representing the cumulative sum sequence for the respective test case. Each list starts with 1000, followed by the cumulative sums of the input sequence for that test case.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads an integer `n` (2 ≤ n ≤ 500) and a list `x` of n-1 integers (1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n). It then calculates the cumulative sum sequence starting with 1000 and appends each cumulative sum to a list. Finally, it prints the list for each test case as a space-separated string.

