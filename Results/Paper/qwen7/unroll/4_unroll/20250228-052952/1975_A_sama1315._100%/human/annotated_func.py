#State of the program right berfore the function call: a is a list of n positive integers (2 ≤ n ≤ 50) where each element is between 1 and 1,000,000 inclusive.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: Output State: `a` is a list of n positive integers; `n` is the length of the list `a`; `sorted_a` is a list of the same n elements as `a` but sorted in ascending order; `concatenated_a` is a list containing the elements of `a` followed by the elements of `a` again; The loop has executed all its iterations without finding any subsequence in `concatenated_a` that matches `sorted_a`, so it returns 'No'.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function accepts a list of positive integers `a` and checks if, when concatenating the list with itself, any subsequence matches the sorted version of the original list. If such a subsequence is found, it returns 'Yes'; otherwise, it returns 'No'. After executing all iterations of the loop, if no matching subsequence is found, the function returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 50, representing the length of the array a. a is a list of n integers such that 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n.
def func_2():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        result = func_1(a)
        
        results.append(result)
        
    #State: Output State: `data` is a list of strings, `t` is an integer, `n` is an integer such that 2 ≤ n ≤ 50, representing the length of the array `a`, `idx` is an integer greater than `t * (n + 1)`, and `results` is a list containing the results of calling `func_1(a)` for each iteration of the loop.
    print('\n'.join(results))
    #This is printed: each element of the `results` list on a new line
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t indicating the number of subsequent test cases, an integer n indicating the length of an array a, and an array a of n integers. For each test case, it calls another function `func_1(a)` to perform an unspecified operation on the array a and collects the results. Finally, it prints each result on a new line.

