#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7.
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
        
    #State: t is an integer such that 1 <= t <= 5000, n is an input integer, a is a list of 2n integers where each integer a_i satisfies 1 <= a_i <= 10^7, final is a list of n integers where each integer is the sum of the smaller elements in each pair of sorted input integers.
    for fin in final:
        print(fin)
        
    #State: The list `final` remains unchanged, and all elements in `final` are printed one by one. The variables `t`, `n`, and `a` remain unchanged.
#Overall this is what the function does:The function reads an integer `n` from the user, and for each of the `n` test cases, it reads a list of 2n integers from the user, sorts the list, and calculates the sum of the smaller integers in each pair of the sorted list. It then appends these sums to a list `final`. After processing all test cases, it prints each element in `final` one by one. The function does not return any value. The variables `t` and `a` mentioned in the comments are not used in the function, and the state of the program after the function concludes is that `final` contains the sums of the smaller integers for each test case, and these sums have been printed.

