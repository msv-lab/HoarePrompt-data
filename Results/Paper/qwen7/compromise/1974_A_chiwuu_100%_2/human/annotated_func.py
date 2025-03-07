#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
def func():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b
        
        if t % 2 == 0:
            t = t // 2
        else:
            t = t // 2 + 1
        
        t1 = t * 15 - b * 4
        
        if t1 >= a:
            t = t
        else:
            t2 = a - t1
            if t2 % 15 == 0:
                t = t + t2 // 15
            else:
                t = t + t2 // 15 + 1
        
        print(t)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is the number of iterations the loop executed.
    #
    #Explanation: The value of `t` changes based on the inputs provided within each iteration of the loop. After all iterations, `t` will be updated according to the logic inside the loop. Since the exact values of `a` and `b` are not specified, we cannot give a precise numerical value for `t`. However, we know that `t` will be constrained between 1 and 10^4, and it will be updated based on the conditions provided in the loop body.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \(a\) and \(b\). For each test case, it calculates and updates the value of \(t\) based on specific conditions. The final value of \(t\) is printed for each test case. The value of \(t\) is constrained between 1 and \(10^4\), and it is updated according to the logic inside the loop body.

