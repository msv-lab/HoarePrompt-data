#State of the program right berfore the function call: a is a list of integers where each integer is positive (1 ≤ a_i ≤ 10^6) and the length of the list n satisfies 2 ≤ n ≤ 50.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: Output State: `a` is a list of integers where each integer is positive (1 ≤ a_i ≤ 10^6) and the length of the list n is equal to the length of `a`; n satisfies 2 ≤ n ≤ 50; `sorted_a` is a list of integers which is a sorted version of `a`; `concatenated_a` is a list obtained by concatenating `a` with itself; the function returns 'Yes' if there exists an index i such that the sublist of `concatenated_a` starting at index i and having the same length as `sorted_a` is equal to `sorted_a`, otherwise it returns 'No'.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function accepts a list of integers `a`, where each integer is positive and within the range of 1 to 10^6, and the length of the list is between 2 and 50. It sorts the list and then checks if any subsequence of the concatenated list (which is the original list appended to itself) matches the sorted list. If such a subsequence is found, the function returns 'Yes'; otherwise, it returns 'No'. The final state of the program is that it returns 'No'.

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
        
    #State: idx is 2 + t, t is an integer equal to int(data[0]), results is a list containing t elements where each element is the result of calling func_1 on a list of integers.
    print('\n'.join(results))
    #This is printed: the results of `func_1` applied to a list of integers, each on a new line
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` indicating the number of test cases, an integer `n` indicating the length of an array `a`, and the array `a` itself. For each test case, it calls another function `func_1` on array `a` and collects the results. Finally, it prints the results of `func_1` for each test case, each result on a new line.

