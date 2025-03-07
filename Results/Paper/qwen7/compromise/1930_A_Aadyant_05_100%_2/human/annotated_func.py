#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers written on the whiteboard are 2n integers a_1, a_2, …, a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State: After the loop executes all iterations, `t` retains its value, `n` retains its value, `num` is equal to `n-1`, `a` retains its value, `b` retains its value, `list1` is empty, `str` is undefined, `list2` is a sorted list of integers derived from `list1` for each iteration, and `final` is a list containing the sum of elements at even indices for each `list2`.
    for fin in final:
        print(fin)
        
    #State: `final` is a list containing the sums of elements at even indices for each of the three `list2` iterations, with each `list2` being a sorted list of integers derived from `list1` for each iteration.
#Overall this is what the function does:The function processes multiple test cases, where each case consists of an integer \( t \) (1 ≤ \( t \) ≤ 5000) and an integer \( n \) (1 ≤ \( n \) ≤ 50). For each test case, it reads \( 2n \) integers and sorts them. Then, it calculates the sum of the integers at even indices for each sorted list and stores these sums in a list. Finally, it prints each sum in the list.

