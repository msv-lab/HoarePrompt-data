#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers written on the whiteboard are 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State: The final value of `s` is the sum of all integers in `list2` at even indices from all iterations combined, `i` is equal to the total length of `list2` across all iterations, `final` is a list containing the cumulative sum of `s` from each iteration, and `list2` is a sorted list of integers from all iterations combined with a length that is the sum of the lengths of `list2` from each iteration.
    for fin in final:
        print(fin)
        
    #State: final must contain the cumulative sum of s from each iteration, and list2 must contain a sorted list of integers from all iterations combined with a length that is the sum of the lengths of list2 from each iteration.
#Overall this is what the function does:The function processes multiple test cases, each involving an integer \( n \) and an array of \( 2n \) integers. For each test case, it calculates the sum of integers at even indices in the sorted array of these integers, then appends this sum to a list. After processing all test cases, it prints the cumulative sums for each test case.

