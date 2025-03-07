#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7.
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
        
    #State: `t` is an integer such that 1 <= t <= 5000; for each test case, `n` is an integer such that 1 <= n <= 50, and `a` is a list of 2n integers where each integer `a_i` satisfies 1 <= `a_i` <= 10^7; `num` is a string read from input; `out` is a list containing the sums of the selected elements from each test case.
    for outputs in out:
        print(outputs)
        
    #State: `t` is an integer such that 1 <= t <= 5000; for each test case, `n` is an integer such that 1 <= n <= 50, and `a` is a list of 2n integers where each integer `a_i` satisfies 1 <= `a_i` <= 10^7; `num` is a string read from input; `out` is a list containing the sums of the selected elements from each test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `2n` integers. It then computes the sum of every other element from the sorted list of integers (starting from the first element) and prints this sum for each test case.

