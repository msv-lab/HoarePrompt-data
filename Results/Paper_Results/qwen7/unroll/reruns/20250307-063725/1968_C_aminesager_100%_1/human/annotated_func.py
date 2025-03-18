#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
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
        
    #State: The output will be a series of lists, each representing the cumulative sum sequence for the respective test case. Each list will start with 1000, followed by the cumulative sums of the input integers for that test case.
#Overall this is what the function does:The function processes a series of test cases, each containing a positive integer `t`, an integer `n`, and a list `x` of `n-1` integers. For each test case, it calculates the cumulative sum sequence starting with 1000, and prints the result as a space-separated string. After processing all test cases, the function outputs a series of lists, each representing the cumulative sum sequence for the respective test case, with each list starting with 1000 followed by the cumulative sums of the input integers.

