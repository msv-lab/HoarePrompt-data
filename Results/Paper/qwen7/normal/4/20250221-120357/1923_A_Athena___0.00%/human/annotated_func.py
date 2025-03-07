#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and the second line contains a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. At least one a_i is 1 in each test case.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: The list `a` will be a non-empty list of integers with its first element set to the second element of the original list, the length of `a` is at most the length of the original list minus 7, and the last element of `a` is 0. The variable `res` will be equal to the count of zeros in the final list `a`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (1 ≤ t ≤ 1000) and a list of n integers (2 ≤ n ≤ 50) where each integer is either 0 or 1, with at least one integer being 1. For each test case, it removes leading and trailing zeros from the list, counts the remaining zeros, and prints both the modified list and the zero count. The function ultimately outputs these results for each test case.

