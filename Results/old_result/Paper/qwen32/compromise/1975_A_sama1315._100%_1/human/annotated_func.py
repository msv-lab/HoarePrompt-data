#State of the program right berfore the function call: a is a list of positive integers, and n is the length of the list a such that 2 <= n <= 50.
def func_1(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    for i in range(n):
        if concatenated_a[i:i + len(sorted_a)] == sorted_a:
            return 'Yes'
        
    #State: None.
    return 'No'
    #The program returns 'No'
#Overall this is what the function does:The function accepts a parameter `a`, which is a list of positive integers, and it checks if any contiguous subsequence of length equal to the list itself in a doubled version of the list matches the sorted version of the list. The function always returns 'No'.

#State of the program right berfore the function call: a is a list of n positive integers where n is an integer such that 2 <= n <= 50, and each element in a satisfies 1 <= a_i <= 10^6.
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
        
    #State: `a` is the last list of integers processed by the loop; `idx` is the position right after the last list of integers in the input; `t` is unchanged; `results` contains the results of `func_1` for each list `a` processed in the loop.
    print('\n'.join(results))
    #This is printed: result1\nresult2\n...\nresultN (where result1, result2, ..., resultN are the results of func_1 for each list a processed in the loop)
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of a list of positive integers. For each list, it computes a result using the `func_1` function and then prints all results, one per line.

