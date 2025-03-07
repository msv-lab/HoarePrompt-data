#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 1 <= n <= 50, and the list of integers a contains 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7.
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
        
    #State: `out` is a list containing `int(num)` sums, where each sum is the sum of every second element from the sorted list of integers provided for each iteration. All other variables (`t`, `n`, `a`, `num`) remain unchanged.
    for outputs in out:
        print(outputs)
        
    #State: `out` is a list containing `int(num)` sums, where each sum is the sum of every second element from the sorted list of integers provided for each iteration. All other variables (`t`, `n`, `a`, `num`) remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `2n` integers. It then calculates the sum of every second element from the sorted list of integers for each test case and prints these sums.

