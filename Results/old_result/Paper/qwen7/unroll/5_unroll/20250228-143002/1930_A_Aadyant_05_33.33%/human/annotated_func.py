#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 5000, `num` is an input string, `n` is an integer such that 1 ≤ n ≤ 50, `out` is a list containing the sum of every second element from a sorted list of `a` space-separated integers, repeated `int(num)` times.
    for outputs in out:
        print(outputs)
        
    #State: Output State: `out` is a list containing the sum of every second element from a sorted list of `a` space-separated integers, printed `int(num)` times.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer t and 2n integers a_1, a_2, ..., a_{2n}. For each test case, it sorts the 2n integers, selects every second element from the sorted list, sums these elements, and repeats this process t times. Finally, it prints the sum of every second element for each test case, repeated t times.

