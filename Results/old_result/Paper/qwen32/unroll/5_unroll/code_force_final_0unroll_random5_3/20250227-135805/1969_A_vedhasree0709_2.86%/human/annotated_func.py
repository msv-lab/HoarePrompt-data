#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000; for each test case, n is an integer such that 2 <= n <= 50; p is a list of n distinct integers such that 1 <= p_i <= n for all i in [1, n] and p_i != i for all i in [1, n].
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: For each test case, the output will be either `2` or `3`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `p` of `n` distinct integers. For each test case, it checks if there exists a pair of consecutive elements in the list that can be swapped to move towards sorting the list in ascending order with a specific pattern. If such a pair is found, it outputs `2`; otherwise, it outputs `3`. The function does not return a value but prints the result for each test case.

