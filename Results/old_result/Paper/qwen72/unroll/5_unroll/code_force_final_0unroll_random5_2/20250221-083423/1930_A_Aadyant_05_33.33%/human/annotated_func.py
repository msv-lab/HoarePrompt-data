#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7.
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
        
    #State: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7, num is an input string, out is a list of t integers where each integer is the sum of the first n sorted integers from the input list.
    for outputs in out:
        print(outputs)
        
    #State: The variable `out` remains a list of `t` integers, where each integer is the sum of the first `n` sorted integers from the input list `a`. The values of `t`, `n`, `a`, and `num` remain unchanged.
#Overall this is what the function does:The function reads a series of inputs and processes them to output the sum of the first `n` sorted integers from each input list. Specifically, it first reads an integer `num` indicating the number of test cases. For each test case, it reads an integer `a` and a space-separated string of `2n` integers. It then sorts these integers, selects the first `n` of them, sums them, and appends the result to a list `out`. Finally, it prints each element in `out`. The function does not return any value, but it modifies the list `out` to contain the sums for each test case. The state of the program after the function concludes includes the variable `out` as a list of `t` integers, where each integer is the sum of the first `n` sorted integers from the input list. The values of `t`, `n`, `a`, and `num` remain unchanged.

