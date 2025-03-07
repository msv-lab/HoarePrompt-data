#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2 × 10^5), followed by a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i < n). The total number of elements across all test cases does not exceed 2 × 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: After all iterations, `n` is the integer from the last test case, `arr` is the list of integers from the last test case, `mpp` is the Counter object created from `arr` in the last test case, and `first` is `True` if there was any integer in `arr` that occurred exactly once and was not the first such integer encountered, otherwise `False`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it identifies and prints the smallest integer between 0 and `n-1` that either does not appear in the list or appears exactly once, ensuring that if multiple such integers exist, the smallest one is chosen.

