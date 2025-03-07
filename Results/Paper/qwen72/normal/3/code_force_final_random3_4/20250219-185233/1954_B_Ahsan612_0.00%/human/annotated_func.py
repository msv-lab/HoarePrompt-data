#State of the program right berfore the function call: The function `func` is expected to take input through standard input and output through standard output, as it does not have any parameters defined. The input consists of multiple test cases, where the first line contains a single integer t (1 ≤ t ≤ 10^4) indicating the number of test cases. Each test case starts with a single integer n (1 ≤ n ≤ 3 · 10^5), followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n). The array a in each test case is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf:
            print(-1)
        else:
            print(minn)
        
    #State: The input value is a positive integer (1 ≤ t ≤ 10^4), `_` is a temporary variable used for iteration and has been incremented by `t` times, `n` is the input integer from the last test case, `ar` is a list of integers from the last test case with at least 2 elements, `i` is equal to the length of `ar`, `num` is the last element of `ar` that was processed, `same` is the count of the last sequence of consecutive elements equal to `num`, and `minn` is the minimum value of the lengths of consecutive sequences of the same number in all the test cases. If `minn` is `inf`, it indicates that there were no sequences of consecutive same numbers in any of the test cases. Otherwise, `minn` is the smallest length of such sequences found across all test cases.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, processes each test case to find the minimum length of consecutive sequences of the same number in the list, and prints this minimum length to standard output for each test case. If no such sequences exist in a test case, it prints `-1`. The function does not return any value and modifies no external state.

