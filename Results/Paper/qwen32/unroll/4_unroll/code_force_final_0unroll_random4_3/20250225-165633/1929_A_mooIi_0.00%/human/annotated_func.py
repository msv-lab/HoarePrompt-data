#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the array a contains n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = map(str, sorted(list(map(int, input().split()))))
        
        print(' '.join(ar))
        
    #State: For each test case, the output is a space-separated string of integers from the array `a`, sorted in ascending order. The variable `t` remains unchanged, and `n` and `ar` are not retained after each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it sorts the list of integers in ascending order and prints them as a space-separated string. The number of test cases `t` is specified initially, and the function handles up to 500 test cases. The integers in each list can be as large as \(10^9\).

