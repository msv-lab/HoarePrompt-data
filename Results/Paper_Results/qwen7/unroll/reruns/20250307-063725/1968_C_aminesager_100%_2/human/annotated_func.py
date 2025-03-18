#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and the input consists of n-1 integers x_2, \dots, x_n such that 1 ≤ x_i ≤ 500. The sum of all n values over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: The output state will be a series of lists, each representing the cumulative sum up to that point for each input line, formatted as strings.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` indicating the number of subsequent test cases, an integer `n`, and `n-1` integers `x_2, ..., x_n`. For each test case, it calculates the cumulative sum of the sequence starting from 1000 and prints the results as space-separated strings. The function does not return any value but outputs the cumulative sums for all test cases.

