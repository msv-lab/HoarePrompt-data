#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and a is a list of 2n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^7.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 5000; `n` is a string representation of an integer input by the user such that 1 ≤ int(n) ≤ 50; `a` is a string input by the user; `final` is a list of `int(n)` integers, each being the sum of the integers at even indices in the sorted list derived from the respective strings `b`.
    for fin in final:
        print(fin)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is a string representation of an integer input by the user such that 1 ≤ int(n) ≤ 50, `a` is a string input by the user, `final` is a list of `int(n)` integers, and all elements of `final` have been printed.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it reads an integer `n` and a list of `2n` integers. It then calculates the sum of the integers at even indices in the sorted list of these integers and prints this sum for each test case.

