#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each sublist contains 2n integers (1 ≤ n ≤ 50) with each integer in the range 1 to 10^7.
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
        
    #State: Output State: `t` remains an integer between 1 and 5000, `list_of_lists` remains a list of lists where each sublist contains 2n integers (1 ≤ n ≤ 50) with each integer in the range 1 to 10^7, `num` remains an input string, `out` is a list of integers where each integer is the sum of the first, third, fifth, etc., integers from each sorted sublist of 2n integers read from the input, and the length of `out` is equal to the integer value of `num`.
    for outputs in out:
        print(outputs)
        
    #State: The `out` list remains unchanged, and `t`, `list_of_lists`, and `num` also remain unchanged. The loop simply prints each element in the `out` list, but does not modify any of the variables.
#Overall this is what the function does:The function reads an integer `t` (1 ≤ t ≤ 5000) representing the number of test cases. For each test case, it reads a list of 2n integers (1 ≤ n ≤ 50) from the input, sorts the list, and computes the sum of the first, third, fifth, etc., integers from the sorted list. It then prints the sum for each test case. The function does not return any value; it only prints the results. After the function concludes, `t` remains an integer between 1 and 5000, and the input lists remain unchanged. The `out` list contains the sums for each test case, and these sums are printed to the console.

