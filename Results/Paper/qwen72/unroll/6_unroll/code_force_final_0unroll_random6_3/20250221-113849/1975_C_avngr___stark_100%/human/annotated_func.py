#State of the program right berfore the function call: The function is expected to handle multiple test cases, where each test case includes an integer n (2 ≤ n ≤ 10^5) representing the length of the array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The total number of test cases t is an integer (1 ≤ t ≤ 500), and the sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: The loop executes `t` times, processing each test case. For each test case, if `n` is 2, the minimum value of the two elements in the array `a` is printed. If `n` is greater than 2, the maximum of the second largest elements from every consecutive triplet in the array `a` is printed. The variables `t`, `n`, and `a` are not retained between test cases, and their values are reset for each new test case.
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case consists of an integer `n` and a list of `n` integers `a`. For each test case, if `n` is 2, the function prints the minimum value of the two elements in the array `a`. If `n` is greater than 2, the function prints the maximum of the second largest elements from every consecutive triplet in the array `a`. The function does not return any values; it only prints the results for each test case. The variables `t`, `n`, and `a` are reset for each new test case.

