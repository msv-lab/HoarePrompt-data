#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50, 1 ≤ a_i ≤ 10^7) for each test case.
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
        
    #State: `t` is an integer (1 ≤ t ≤ 5000), `test_cases` is a list of lists where each inner list contains 2n integers (1 ≤ n ≤ 50, 1 ≤ a_i ≤ 10^7) for each test case, `num` is an input string, `out` is a list of integers where each integer is the sum of the first, third, fifth, etc., elements of the sorted list of integers from each test case.
    for outputs in out:
        print(outputs)
        
    #State: The variable `out` remains unchanged, and the loop prints each element of `out` to the console. The variables `t`, `test_cases`, and `num` remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from user input, representing the number of test cases. For each test case, it reads a list of 2n integers (where 1 ≤ n ≤ 50) from user input, sorts the list, and sums every other element starting from the first one. It then appends this sum to a list `out`. After processing all test cases, it prints each sum in `out` to the console. The function does not return any value.

