#State of the program right berfore the function call: The function should accept an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and for each test case, an integer n (2 ≤ n ≤ 500) representing the number of elements in the array a, and a list of n-1 integers x_2, ..., x_n (1 ≤ x_i ≤ 500) representing the elements of the array x. The sum of values n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is 0, `n` is the same as the initial input, `a` has `n` elements, where each new element from index 1 to `n-1` is the sum of the previous element in `a` and the corresponding element in `T`, `result` is a string containing the elements of `a` separated by spaces.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list `T` of `n-1` integers. It constructs a new list `a` of `n` elements, where each element from index 1 to `n-1` is the sum of the previous element in `a` and the corresponding element in `T`. The function then prints the elements of `a` as a space-separated string. After processing all test cases, the function terminates with `t` set to 0, `n` unchanged from its initial value for the last test case, and `a` containing `n` elements as described.

