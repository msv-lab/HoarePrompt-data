#State of the program right berfore the function call: a is a list of n positive integers where 2 ≤ n ≤ 50 and 1 ≤ a_i ≤ 10^6 for all i.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: Output State: `a` is a list of n positive integers where 2 ≤ n ≤ 50 and 1 ≤ a_i ≤ 10^6 for all i; `n` is the length of list `a`; `sorted_a` is a list of the same integers as `a` but sorted in non-decreasing order; `concatenated_a` is a list equal to `a + a`; The loop checks if any substring of `concatenated_a` with the same length as `sorted_a` is equal to `sorted_a`. If such a substring is found, it returns 'Yes'. Otherwise, it continues checking until all iterations are completed and returns 'No' if no such substring exists.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function accepts a list of positive integers and checks if any substring of the concatenated list (the original list appended to itself) has the same length as the sorted version of the original list. If such a substring is found, it returns 'Yes'; otherwise, it returns 'No'. Given the return postconditions, the function will always return 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `idx` is 2 + 2t, `t` is an integer such that 1 ≤ t ≤ 1000, `results` is a list containing `t` elements where each element is the result of `func_1(a)` for each iteration.
    print('\n'.join(results))
    #This is printed: \n'.join([str(func_1(a))]*t)
#Overall this is what the function does:The function reads input from stdin, processes it according to predefined variables `t`, `n`, and `a`, and then calls `func_1` for each set of inputs defined by `t`. It collects the results of these calls into a list and prints them out, separated by newlines. The final state of the program includes the variable `idx` updated to reflect the position in the input data after processing all sets, and the list `results` containing the processed outputs.

