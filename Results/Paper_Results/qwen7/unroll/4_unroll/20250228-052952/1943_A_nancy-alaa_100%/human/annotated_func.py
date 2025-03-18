#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: The output is the smallest missing integer in the array `arr` for each test case. If there are no duplicates and the array is complete (i.e., it contains all integers from 0 to n-1), then the output is n. If the smallest missing integer is found before completing the loop, that integer is printed.
#Overall this is what the function does:For each test case, the function reads a positive integer `n` and a list `arr` of `n` non-negative integers. It then finds and prints the smallest missing integer in the list `arr`. If there are no duplicates and the list contains all integers from 0 to n-1, it prints `n`. If the smallest missing integer is found during the iteration, it is printed immediately.

