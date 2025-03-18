#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists x where each inner list represents the elements x_2, x_3, ..., x_n (1 ≤ x_i ≤ 500) for a given test case, and the length of each inner list is n-1 (2 ≤ n ≤ 500). The sum of values n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The value of `t` is 0, and the loop has processed all test cases. For each test case, the list `a` has been updated to contain the cumulative sums of the elements in `T` starting from 1000, and the result has been printed as a space-separated string.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a space-separated list of integers `T` of length `n-1`. It then computes a new list `a` where each element is the cumulative sum of the elements in `T` starting from 1000. The function prints the elements of `a` as a space-separated string for each test case. After processing all test cases, the function terminates with `t` set to 0.

