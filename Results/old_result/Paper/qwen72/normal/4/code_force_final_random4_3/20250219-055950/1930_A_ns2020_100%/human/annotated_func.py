#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 5000), the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50) with each integer a_i (1 ≤ a_i ≤ 10^7). The function should return a list of integers representing the maximum final score for each test case.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: `t` is 0, `n` is the input integer, `A` is a list of integers in ascending order.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of 2n integers. It sorts the list and prints the sum of the elements at even indices. The function does not return any value. After the function concludes, `t` is 0, and the state of `n` and `A` is undefined as they are reinitialized for each test case.

