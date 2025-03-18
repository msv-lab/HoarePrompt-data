#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 50) representing the number of pairs of integers on the whiteboard. The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7) which are the numbers written on the whiteboard. The total number of test cases t is between 1 and 5000.
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
        
    #State: final is a list containing the sum of every other element (starting from the first) of the sorted list of integers for each pair of inputs.
    for fin in final:
        print(fin)
        
    #State: final is a list containing the sum of every other element (starting from the first) of the sorted list of integers for each pair of inputs.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `2n` integers. For each test case, it sorts the list of integers, sums every other element starting from the first, and prints the result for each test case.

