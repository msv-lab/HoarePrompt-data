#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. Each of the following t test cases consists of two lines: the first line contains an integer n such that 1 <= n <= 50, and the second line contains 2n integers a_1, a_2, ..., a_{2n} such that 1 <= a_i <= 10^7.
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
        
    #State: `t` is an integer such that 1 <= t <= 5000; `num` is a string containing the input line; `out` is a list containing the sums of the selected elements from each iteration.
    for outputs in out:
        print(outputs)
        
    #State: `t` is an integer such that 1 <= t <= 5000; `num` is a string containing the input line; `out` is a list containing the sums of the selected elements from each iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `2n` integers. For each test case, it selects every other integer starting from the first one, sums these selected integers, and prints the sum for each test case.

