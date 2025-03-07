#State of the program right berfore the function call: The function is expected to handle multiple test cases, where each test case includes an integer n representing the length of the array and an array a of integers. t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and each element a_i in the array a is an integer such that 1 ≤ a_i ≤ n. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it processes the array to find the minimum length of consecutive segments of the same number. If the array is uniform (i.e., all elements are the same) or if no such segment is found, it prints -1. Otherwise, it prints the minimum length of these segments. The variables `same`, `num`, `minn`, and `i` are reset for each test case, and the loop continues until all test cases are processed.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and an array `a` of `n` integers. It then processes the array to find the minimum length of consecutive segments of the same number. If the array is uniform (i.e., all elements are the same) or if no such segment is found, it prints `-1`. Otherwise, it prints the minimum length of these segments. The function does not return any value; it only prints the results for each test case.

