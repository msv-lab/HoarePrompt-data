#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers on the whiteboard are 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 5000, `num` is an input integer, `n` is an input integer such that 1 ≤ n ≤ 50, and `out` is a list containing the sum of every second element from each input list, sorted and summed based on the given number of iterations specified by `num`.
    for outputs in out:
        print(outputs)
        
    #State: Output State: `out` is a list containing the sum of every second element from each input list, sorted and summed based on the given number of iterations specified by `num`. The loop iterates over each element in `out` and prints it, but the value of `out` itself does not change after the loop execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t and an integer n, along with 2n integers. For each test case, it calculates the sum of every second element from the input list, sorts these sums, and then prints each sum. The final output is a series of printed sums corresponding to each test case.

