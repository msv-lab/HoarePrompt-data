#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and the array a consists of n positive integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: Output State: After the loop executes all its iterations, `t` must be greater than 0, `n` will be the value it was set to in the last iteration of the loop, `a` will remain unchanged from its initial input, `max` will hold the highest value that was the second largest in any of the three-element sublists of `a`, and `i` will be equal to `n - 2`.
    #
    #In simpler terms, after the loop completes all its iterations, `t` remains greater than 0, `n` is the value it had in the last iteration, `a` stays as the list of integers entered by the user, `max` contains the maximum value found as the second largest element in any three consecutive elements of `a`, and `i` equals `n - 2`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n` (size of the array), and an array `a` of `n` positive integers. If `n` is 2, it prints the minimum of `a`. Otherwise, it finds the maximum value among the second largest elements in all possible three-element sublists of `a` and prints this value. After processing all test cases, it outputs the results for each case.

