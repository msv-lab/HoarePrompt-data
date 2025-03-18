#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7.
def func():
    n = input()
    final = []
    for num in range(int(n)):
        s = 0
        
        list2 = []
        
        a = input()
        
        list1 = []
        
        b = input()
        
        list1 = b.split()
        
        for str in list1:
            list2.append(int(str))
        
        list2.sort()
        
        for i in range(0, len(list2), 2):
            s = s + int(list2[i])
        
        final.append(s)
        
    #State: `final` is a list of `int(n)` integers, where each integer is the sum of the elements at even indices of the sorted sublists of `a`. The values of `t`, `n`, and `a` remain unchanged.
    for fin in final:
        print(fin)
        
    #State: Each element of the list `final` is printed on a new line. The values of `t`, `n`, and `a` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `2n` integers. For each test case, it sorts the list, sums the elements at even indices, and prints the result for each test case.

