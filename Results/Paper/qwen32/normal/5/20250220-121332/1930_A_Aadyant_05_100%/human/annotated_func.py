#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 50), representing half the number of integers on the whiteboard. This is followed by a line containing 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7), which are the numbers written on the whiteboard. The total number of test cases, t, is given at the beginning and satisfies 1 ≤ t ≤ 5000.
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
        
    #State: final is a list of n sums, where each sum is the sum of the integers at even indices of the sorted list of integers provided in each iteration.
    for fin in final:
        print(fin)
        
    #State: The loop will print each element of the `final` list, which contains `n` sums. Each sum is the sum of the integers at even indices of the sorted list of integers provided in each iteration.
#Overall this is what the function does:The function processes multiple test cases. Each test case consists of an integer `n` and a list of `2n` integers. For each test case, it sorts the list of integers and calculates the sum of the integers located at even indices in the sorted list. The function then prints the sum for each test case.

