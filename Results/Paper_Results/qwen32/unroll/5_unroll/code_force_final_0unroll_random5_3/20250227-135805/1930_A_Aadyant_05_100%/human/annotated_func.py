#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 50), representing that there are 2n integers on the whiteboard. The next line contains 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7), which are the numbers written on the whiteboard. The first line of the input contains a single integer t (1 ≤ t ≤ 5000), the number of test cases.
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
        
    #State: `final` is a list of sums of elements at even indices of the sorted lists from each iteration. `n` remains unchanged as the input string.
    #
    #Since the specific values of `n` and the inputs for `a` and `b` are not provided, we can only describe the structure of the `final` list in terms of the operations performed.
    #
    #Output State:
    for fin in final:
        print(fin)
        
    #State: `final` is a list of sums of elements at even indices of the sorted lists from each iteration. `n` remains unchanged as the input string.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a number `n` and a list of `2n` integers. It sorts the list of integers and calculates the sum of the elements at even indices (0, 2, 4, ...). The function then prints the sum for each test case.

