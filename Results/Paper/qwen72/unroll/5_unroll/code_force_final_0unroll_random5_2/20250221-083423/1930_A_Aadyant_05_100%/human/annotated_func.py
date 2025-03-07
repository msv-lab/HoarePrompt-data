#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50) with each integer a_i (1 ≤ a_i ≤ 10^7).
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
        
    #State: The `final` list will contain `t` elements, where each element is the sum of the sorted even-indexed integers from the corresponding input list. The variable `num` will be equal to `int(n) - 1`. The variables `s`, `list2`, `a`, `b`, and `list1` will be reset to their final values from the last iteration of the loop.
    for fin in final:
        print(fin)
        
    #State: Output State: The `final` list will contain `t` elements, where each element is the sum of the sorted even-indexed integers from the corresponding input list. The variable `num` will be equal to `int(n) - 1`. The variables `s`, `list2`, `a`, `b`, and `list1` will be reset to their final values from the last iteration of the loop. The loop will have printed each element of the `final` list, one per line.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads a list of 2n integers, sorts the list, and calculates the sum of the integers at even indices (0, 2, 4, ...). It then appends this sum to a list `final`. After processing all test cases, the function prints each element of `final`, one per line. The function does not return any value.

