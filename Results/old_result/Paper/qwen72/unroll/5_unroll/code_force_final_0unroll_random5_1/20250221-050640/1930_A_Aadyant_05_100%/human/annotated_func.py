#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50 and 1 ≤ a_i ≤ 10^7) for each test case.
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
        
    #State: The `final` list will contain `t` integers, each representing the sum of the elements at even indices of the sorted list of 2n integers for each test case. The variables `num`, `s`, `list2`, `a`, `b`, and `list1` will be in their final states after the last iteration of the loop, with `num` being equal to `int(n) - 1`, `s` being the sum of the elements at even indices of the last test case, `list2` being the sorted list of the last test case, and `list1` being the list of strings from the last input split.
    for fin in final:
        print(fin)
        
    #State: Output State: The `final` list will remain unchanged, and the variables `num`, `s`, `list2`, `a`, `b`, and `list1` will retain their final states after the last iteration of the loop. The loop will print each integer in the `final` list, one per line.
#Overall this is what the function does:The function reads an integer `t` (1 ≤ t ≤ 5000) from the user, representing the number of test cases. For each test case, it reads a list of 2n integers (1 ≤ n ≤ 50 and 1 ≤ a_i ≤ 10^7) from the user, sorts the list, and calculates the sum of the elements at even indices. It then prints the sum for each test case, one per line. The function does not return any value.

