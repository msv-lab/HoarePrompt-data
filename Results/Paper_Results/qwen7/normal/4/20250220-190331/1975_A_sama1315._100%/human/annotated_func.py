#State of the program right berfore the function call: a is a list of n positive integers where n is an integer such that 2 <= n <= 50 and each element a_i is an integer such that 1 <= a_i <= 10^6.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: Output State: The function will either return 'Yes' at some point during the loop's execution or it will return None if no substring `concatenated_a[i:i + len(sorted_a)]` equals `sorted_a` for any `i` in the range of `n`.
    #
    #In Natural Language: After all the iterations of the loop have finished, the function will either find a match where a substring of `concatenated_a` from index `i` to `i + len(sorted_a)` is equal to `sorted_a` and return 'Yes', or it will not find any such match and will return None (meaning it will implicitly return None since no return statement was encountered).
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function `func_1` accepts a list of `n` positive integers (`a`) where `2 <= n <= 50` and each integer in the list is between `1` and `10^6`. It first sorts the list and then concatenates the original list with itself. The function checks if any substring of the concatenated list, whose length is equal to the original list, matches the sorted version of the original list. If such a substring is found, the function returns 'Yes'; otherwise, it returns 'No'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `t` is 0, `n` is int(data[11]), `idx` is 14 + int(data[11]), `a` is a list of integers extracted from `data` starting from index `idx + n` and of length `n`, `results` is a list containing the results of `func_1(a)` for each iteration of the loop.
    #
    #Explanation: After the loop has executed all its iterations, `t` will be reduced to 0 since it starts as a positive integer and decreases by 1 in each iteration. The final value of `idx` will be 14 plus the value of `n` (which was determined in the third iteration) because `idx` is incremented by `n` at the end of each iteration. The value of `a` will be the last list of integers extracted from `data` based on the final value of `idx` and `n`. The `results` list will contain the results of applying `func_1(a)` to each list `a` processed during the loop's iterations.
    print('\n'.join(results))
    #This is printed: the results of func_1(a) for each iteration, separated by newlines
#Overall this is what the function does:The function processes a series of test cases (determined by the value of `t`) where each test case consists of an integer `n` followed by a list of `n` integers `a`. For each test case, it calls another function `func_1(a)` to compute a result, collects these results in a list, and finally prints each result on a new line. The function does not return any value directly but modifies the global variables `t`, `n`, `idx`, and `a` as it processes the input data.

