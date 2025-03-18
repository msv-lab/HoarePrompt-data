#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 50), representing half the number of integers on the whiteboard. This is followed by a line containing 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7), which are the numbers written on the whiteboard. The total number of test cases, t, is between 1 and 5000.
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
        
    #State: `final` is a list containing `int(n)` sums, each sum being the sum of integers at even indices of the respective `list2` generated in each iteration.
    for fin in final:
        print(fin)
        
    #State: All elements of the `final` list have been printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `2n` integers. It calculates the sum of the integers at even indices after sorting the list for each test case and prints these sums.

