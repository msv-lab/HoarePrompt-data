#State of the program right berfore the function call: The function `func` is expected to be called within a context where it processes multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 2 · 10^5) and a list of `n` integers `a` (0 ≤ a_i < n). The sum of `n` over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n + 1):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: The loop processes each test case by reading an integer `n` and a list of `n` integers `a`. For each test case, it prints the smallest integer `i` that is not present in the list `arr` or the smallest integer `i` that appears exactly once in `arr` after the first such integer has been found. The variables `n`, `arr`, and `mpp` are reset for each test case, and `first` is used to track the first occurrence of a unique integer. After all iterations, the initial state of the function remains unchanged, except that the output for each test case has been printed.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers `a`. It then prints the smallest integer `i` (0 ≤ i < n) that is not present in the list `a`. If all integers from 0 to n are present, it prints the smallest integer `i` that appears exactly once in the list `a` after the first such integer has been found. The function does not return any values; it only prints the results for each test case. After processing all test cases, the function exits, and the program state is unchanged except for the printed output.

