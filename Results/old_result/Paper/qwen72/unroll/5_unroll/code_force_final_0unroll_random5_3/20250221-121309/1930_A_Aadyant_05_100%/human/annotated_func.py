#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50, 1 ≤ a_i ≤ 10^7) representing the numbers on the whiteboard for each test case.
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
        
    #State: Output State: `final` is a list containing `t` integers, each integer is the sum of the elements at even indices of a sorted list of integers input by the user. `t` remains an integer (1 ≤ t ≤ 5000), and `n` remains a string.
    for fin in final:
        print(fin)
        
    #State: The `final` list remains unchanged, and `t` and `n` also remain unchanged. The loop prints each integer in the `final` list, which contains `t` integers, each being the sum of the elements at even indices of a sorted list of integers input by the user.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads a list of 2n integers from the user, sorts the list, and calculates the sum of the elements at even indices. The function then prints the sum for each test case. The function does not return any value, but it prints a list of `t` integers, each being the sum of the elements at even indices of a sorted list of integers input by the user. The final state of the program is that `t` remains an integer (1 ≤ t ≤ 5000), `n` remains a string, and the `final` list contains `t` integers.

