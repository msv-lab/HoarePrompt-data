#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. Additionally, a list of n integers representing the numbers on the cards is provided for each test case, where each integer is in the range 1 ≤ c_i ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: Output State: t is an integer between 1 and 500. For each iteration i in the range of t, two integers n and k are read, followed by a list of n integers. The code then prints k - 1. After all iterations, the output consists of t lines, each containing a single integer which is k - 1 for the corresponding iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer t (1 ≤ t ≤ 500), followed by pairs of integers n and k (1 ≤ n ≤ 100, 2 ≤ k ≤ 100), and a list of n integers (1 ≤ c_i ≤ 100). It then prints k - 1 for each test case, resulting in t lines of output, each containing a single integer which is k - 1.

