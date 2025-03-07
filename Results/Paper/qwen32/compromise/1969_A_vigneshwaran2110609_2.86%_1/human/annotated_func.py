#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i for all i in [1, n], and all p_i are distinct.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: 3 printed n times.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `p` of `n` integers. For each test case, it checks a specific condition related to the list `p` and prints either `2` or `3` based on whether the condition is met or not. The function does not return any value; it only prints the results.

