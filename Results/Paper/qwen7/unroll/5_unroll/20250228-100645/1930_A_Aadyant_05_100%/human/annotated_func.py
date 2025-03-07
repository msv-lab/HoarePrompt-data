#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is an input integer such that 1 ≤ n ≤ 50; `final` is a list containing `n` elements, each element being the sum of every first number in pairs from the input lists sorted in ascending order.
    for fin in final:
        print(fin)
        
    #State: Output State: `final` is a list containing `n` elements, each element being the sum of every first number in pairs from the input lists sorted in ascending order, and the loop prints each element of the `final` list on a new line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (1 ≤ t ≤ 5000) and 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7) for each n (1 ≤ n ≤ 50). For each test case, it sorts the input integers in ascending order, then sums the first number from each pair of consecutive numbers in the sorted list. The function returns a list containing the sum for each test case, with each sum printed on a new line.

