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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is an input integer such that 1 ≤ n ≤ 50; `final` is a list containing `n` elements, each element being the sum of every first number in pairs from the sorted lists of integers provided as inputs.
    for fin in final:
        print(fin)
        
    #State: Output State: `final` is a list containing `n` elements, each element being the sum of every first number in pairs from the sorted lists of integers provided as inputs, and the loop prints each element of the `final` list on a new line.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer t (1 ≤ t ≤ 5000) and 2n integers (1 ≤ n ≤ 50) within the range of 1 to 10^7. For each test case, it sorts the integers, sums the first number in each pair, and stores these sums in a list. Finally, it prints each sum on a new line.

