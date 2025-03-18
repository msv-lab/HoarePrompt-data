#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 500) representing the number of test cases, and a list of lists, where each inner list contains n integers (2 ≤ n ≤ 100) with each integer a_i (1 ≤ a_i ≤ 10^9) representing the elements of the array a.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        kq = 0
        
        for i in range(0, len(a) // 2, 1):
            kq = kq + a[len(a) - i - 1] - a[i]
        
        print(kq)
        
    #State: The variable `kq` will contain the sum of the differences between the largest and smallest elements, the second largest and second smallest elements, and so on, for each test case. The loop will print the value of `kq` for each test case, and `itest` will be equal to `ntest` after the loop finishes executing all iterations.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then calculates the sum of the differences between the largest and smallest elements, the second largest and second smallest elements, and so on, for the list of integers. The function prints this sum for each test case. After processing all test cases, the function concludes without returning any value.

