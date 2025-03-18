#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: Output State: After the loop executes all iterations, `ntest` is an input integer which represents the total number of times the loop has run. `itest` will be equal to `ntest - 1`, indicating that the loop has completed all its iterations. For each iteration, `n` is an input integer representing the size of the list `a`, and `a` is a sorted list of integers obtained by mapping `int` to each element of the input split by spaces. The final output of the loop will be the difference between the largest and smallest elements in each list `a` printed during the iterations.
    #
    #In summary, `ntest` equals the total number of iterations, `itest` is `ntest - 1`, and for each `itest` from 0 to `ntest - 1`, there exists an `n` and a sorted list `a` of integers, with the output being the difference between the maximum and minimum values in `a`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a list of `n` integers. For each test case, it sorts the list of integers and calculates the difference between the largest and smallest values in the sorted list. It then prints this difference for each test case. After processing all test cases, the function does not return any value but outputs the differences for each test case.

