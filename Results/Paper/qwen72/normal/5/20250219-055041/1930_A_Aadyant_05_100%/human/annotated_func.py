#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50) with each integer a_i in the range 1 ≤ a_i ≤ 10^7.
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
        
    #State: `n` must be an integer greater than 0, `num` is `n-1`, `final` is a list containing the sums of all elements at even indices in each of the `n` sorted lists `list2` generated during the loop, `s` is the sum of all elements at even indices in the last `list2`, `list1` is a list of strings resulting from splitting the last user input `b` by spaces, `i` is the last even index in the last `list2` (or `len(list2) - 1` if the length of the last `list2` is odd), `list2` is a sorted list containing the integer values of all the strings in the last `list1`, `a` is the user input, `b` is the last user input.
    for fin in final:
        print(fin)
        
    #State: `n` must be an integer greater than 0, `num` is `n-1`, `final` is a list containing the sums of all elements at even indices in each of the `n` sorted lists `list2` generated during the loop, `s` is the sum of all elements at even indices in the last `list2`, `list1` is a list of strings resulting from splitting the last user input `b` by spaces, `i` is the last even index in the last `list2` (or `len(list2) - 1` if the length of the last `list2` is odd), `list2` is a sorted list containing the integer values of all the strings in the last `list1`, `a` is the user input, `b` is the last user input, `fin` is the last element in `final`.
#Overall this is what the function does:The function reads an integer `n` from the user, representing the number of test cases. For each test case, it reads a line of input containing space-separated integers, converts them to a list of integers, sorts the list, and calculates the sum of the elements at even indices. It then appends this sum to a list `final`. After processing all test cases, it prints each element in `final` on a new line. The function does not return any value.

