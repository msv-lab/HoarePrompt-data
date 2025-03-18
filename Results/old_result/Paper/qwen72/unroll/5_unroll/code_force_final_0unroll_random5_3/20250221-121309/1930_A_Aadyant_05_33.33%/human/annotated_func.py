#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where 1 <= a_i <= 10^7.
def func():
    num = input()
    out = []
    for numbers in range(int(num)):
        list2 = []
        
        list1 = []
        
        a = input()
        
        a = int(a)
        
        b = input('')
        
        list1 = b.split()
        
        list1.sort()
        
        for i in range(a):
            list2.append(int(list1[2 * i]))
        
        out.append(sum(list2))
        
        del list1[:]
        
        del list2[:]
        
    #State: `t` is an integer such that 1 <= t <= 5000, `n` is an integer such that 1 <= n <= 50, `a` is the last input integer read in the loop, `num` is the input string, `out` is a list of `int(num)` integers where each integer is the sum of the first `n` sorted integers from the corresponding input list.
    for outputs in out:
        print(outputs)
        
    #State: The loop prints each integer in the list `out`, which contains `int(num)` integers. Each integer in `out` is the sum of the first `n` sorted integers from the corresponding input list. The values of `t`, `n`, `a`, and `num` remain unchanged.
#Overall this is what the function does:The function reads an integer `num` indicating the number of test cases. For each test case, it reads an integer `a` and a space-separated list of integers `b`. It then sorts the list `b`, selects the first `a` integers, and appends their sum to a list `out`. After processing all test cases, it prints each integer in `out`. The function does not return any value. The final state of the program is that `num` is the input string, `a` is the last input integer read in the loop, and `out` is a list of `int(num)` integers where each integer is the sum of the first `a` sorted integers from the corresponding input list. The values of `t` and `n` are not used or modified by the function.

