#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 2 <= n <= 500, and x is a list of n-1 integers where 1 <= x_i <= 500.
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
        
    #State: t = 0, n remains unchanged, x remains unchanged, a is a list of n integers where each integer is the cumulative sum of the elements in T up to that index, result is a string of space-separated integers representing the list a.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, indicating the number of test cases. For each test case, it reads another integer `n` and a line of `n-1` space-separated integers. It then computes a list `a` of `n` integers, where each element is the cumulative sum of the elements read from the input up to that index. The function prints this list as a space-separated string and repeats this process for each test case. After processing all test cases, the function ends with `t` being 0, `n` and `x` remaining unchanged, and `a` being a list of `n` integers representing the cumulative sums.

