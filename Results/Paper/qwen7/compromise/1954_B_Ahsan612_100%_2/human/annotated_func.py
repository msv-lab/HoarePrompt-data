#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n. Additionally, the sum of n over all test cases does not exceed 3 ⋅ 10^5.
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
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: Output State: The loop has executed all iterations, and `minn` is the minimum count of consecutive occurrences of any element in the list `ar`. If `minn` was infinity or equal to the length of `ar` at any point, it remains unchanged. Otherwise, `minn` is the smallest value found during the loop execution. If no valid minimum consecutive occurrence was found, `minn` will be infinity, indicating that there were no repeating elements in the list `ar` that met the criteria. The final value of `minn` is either the smallest count of consecutive occurrences or infinity, depending on the input list `ar`.
    #
    #In simpler terms, after all iterations, `minn` will hold the smallest number of consecutive identical elements found in the list `ar`, or it will be infinity if no such sequence exists.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` and a list `ar` of `n` integers. It then finds and prints the smallest number of consecutive identical elements in the list `ar`. If no such sequence exists, it prints `-1`. The function implicitly accepts input through standard input and outputs results through standard output.

