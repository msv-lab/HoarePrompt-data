#State of the program right berfore the function call: The function will receive multiple test cases. For each test case, it will first receive an integer n (1 ≤ n ≤ 50) representing the number of pairs of integers on the whiteboard. Following this, it will receive 2n integers (1 ≤ a_i ≤ 10^7) representing the numbers written on the whiteboard. The function should handle up to 5000 such test cases.
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
        
    #State: The `final` list contains the sum of the smaller numbers for each pair of integers in each test case.
    for fin in final:
        print(fin)
        
    #State: the printed values of each element in the `final` list.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and then reads `2n` integers. It calculates the sum of the smaller number in each pair of integers and prints the result for each test case.

