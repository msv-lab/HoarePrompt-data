#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers on the whiteboard are 2n integers a_1, a_2, …, a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: `out` is a list of sums, where each sum is calculated from the first element of every pair in the sorted lists provided by the user for each iteration. The length of `out` is equal to the value of `num`, and each element in `out` is an integer representing the sum of the first elements of the pairs from the sorted lists provided in each iteration.
    for outputs in out:
        print(outputs)
        
    #State: The output state will be a list of integers, where each integer is the sum of the first elements of the pairs from the sorted lists provided in each iteration. The length of the list is equal to the value of `num`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `num`, followed by `2*num` integers. It then sorts these integers and calculates the sum of the first elements of each pair in the sorted list. This sum is stored in a list `out`. After processing all test cases, the function prints each sum in `out`. The final state of the program is a list of integers, where each integer represents the sum of the first elements of the pairs from the sorted lists provided for each test case.

