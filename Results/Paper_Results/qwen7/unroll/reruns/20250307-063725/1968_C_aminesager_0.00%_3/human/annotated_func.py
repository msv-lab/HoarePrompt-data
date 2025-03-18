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
            a.append(a[i - 1] - T[i - 1])
        
        a = a[::-1]
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: Output State: The output state will be a series of lists, each representing the transformed sequence `a` for each input integer `n` provided by the user. Each list `a` is constructed such that `a[i] = 1000 - Σ(T[j])` for `j` from `0` to `i-1`, where `T` is the list of integers inputted for each `n`. The final list `a` for each iteration is reversed before being printed.
    #
    #To break it down further:
    #- For each value of `t`, the user inputs an integer `n`.
    #- Then, the user inputs a line of space-separated integers, which are split into a list `T`.
    #- A list `a` is initialized with `[1000]`.
    #- For each index `i` from `1` to `n-1`, `a[i]` is calculated as `a[i-1] - T[i-1]`.
    #- After the loop completes for each `n`, the list `a` is reversed.
    #- The reversed list `a` is then joined into a string and printed.
    #
    #The output state will consist of these printed strings, one for each input `n`, showing the transformed list `a` for each respective `n`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n` (length of the sequence minus one), and a list `T` of `n-1` integers. It constructs a list `a` starting with 1000 and iteratively updates it based on the values in `T`. After processing all elements in `T`, it reverses the list `a` and prints it. The function outputs a series of transformed sequences `a`, one for each test case.

