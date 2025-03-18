#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of 2n integers, and n is a positive integer such that 1 ≤ n ≤ 50. The integers in each test case are positive and within the range 1 ≤ a_i ≤ 10^7. The function should also handle up to t test cases, where 1 ≤ t ≤ 5000.
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
        
    #State: `out` is a list containing the sum of the selected elements from each test case, and `list1` and `list2` are empty lists.
    for outputs in out:
        print(outputs)
        
    #State: The `out` list remains unchanged, and `list1` and `list2` are still empty lists.
#Overall this is what the function does:The function `func` reads a series of test cases from user input. Each test case consists of a list of 2n positive integers, where 1 ≤ n ≤ 50 and each integer is within the range 1 to 10^7. The function processes up to 5000 test cases. For each test case, it selects every second element from the sorted list of integers and calculates the sum of these selected elements. The function then prints the sum for each test case. After processing all test cases, the function does not return any value, but the `out` list contains the sums of the selected elements for each test case, and `list1` and `list2` are empty lists.

