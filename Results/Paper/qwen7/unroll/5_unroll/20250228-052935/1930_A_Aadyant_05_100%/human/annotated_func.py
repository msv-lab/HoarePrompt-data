#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers a_1, a_2, ..., a_{2n} are positive integers such that 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 5000, `n` is an integer such that 1 ≤ n ≤ 50, and `final` is a list of `n` elements where each element is the sum of the smallest elements from pairs of a given list of integers. The integers `a_1, a_2, ..., a_{2n}` are positive integers such that 1 ≤ a_i ≤ 10^7.
    for fin in final:
        print(fin)
        
    #State: Output State: `final` is a list of `n` elements where each element is printed on a new line.
#Overall this is what the function does:The function processes multiple test cases, each involving a pair of lists of integers. For each test case, it calculates the sum of the smallest elements from each pair of integers in the second list and stores these sums in a list. Finally, it prints each sum on a new line.

