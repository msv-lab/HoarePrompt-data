#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, n is an integer such that 1 <= n <= 50, and a is a list of 2n integers where 1 <= a_i <= 10^7.
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
        
    #State: t is an integer such that 1 <= t <= 5000, n is an input integer such that 1 <= n <= 50, a is a list of 2n integers where 1 <= a_i <= 10^7, final is a list of n integers where each integer is the sum of the sorted even-indexed elements from the corresponding input list.
    for fin in final:
        print(fin)
        
    #State: The variable `t` remains an integer such that 1 <= t <= 5000, `n` remains an input integer such that 1 <= n <= 50, `a` remains a list of 2n integers where 1 <= a_i <= 10^7, and `final` remains a list of n integers where each integer is the sum of the sorted even-indexed elements from the corresponding input list. The loop has printed each element of the `final` list, one per line.
#Overall this is what the function does:The function reads an integer `n` from the user, indicating the number of lists to process. For each of the `n` lists, it reads a list of 2n integers from the user, sorts the list, and calculates the sum of the elements at even indices (0, 2, 4, ...). It stores these sums in a list `final` and then prints each sum on a new line. The function does not return any value. After the function concludes, the variable `n` is an integer such that 1 <= n <= 50, and `final` is a list of `n` integers, each representing the sum of the sorted even-indexed elements from the corresponding input list.

