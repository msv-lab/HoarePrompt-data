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
        
    #State: After the loop executes all iterations, `ntest` remains the same input integer between 1 and 500, `t` remains the same integer representing the number of test cases, and the list of lists remains unchanged. For each test case, the variable `kq` will have been calculated and printed as the sum of the differences between the largest and smallest elements in the sorted list `a`, taken in pairs from the ends towards the center. The final value of `kq` for each test case will be the output for that test case.
#Overall this is what the function does:The function `func` reads an integer `ntest` from the input, which represents the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `a` from the input. It then sorts the list `a` and calculates the sum of the differences between the largest and smallest elements in the sorted list, taken in pairs from the ends towards the center. This sum, `kq`, is printed for each test case. The function does not return any value; it only prints the results. After the function concludes, the input variables `ntest` and the list of lists remain unchanged.

