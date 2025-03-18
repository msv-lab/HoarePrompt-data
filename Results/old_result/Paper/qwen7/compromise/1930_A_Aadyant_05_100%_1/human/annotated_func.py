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
        
    #State: Output State: The final state after the loop executes all its iterations will be as follows:
    #
    #- `t` remains an integer within the range 1 ≤ t ≤ 5000, as it was not affected by the loop.
    #- `n` remains an integer within the range 1 ≤ n ≤ 50, as it was not modified inside the loop.
    #- `final` is a list that contains the sum of every second element from each `list2` created during the loop's iterations, starting from the first element of each `list2`. This means `final` will contain the sum of every second element from the first `list2`, then the sum of every second element from the second `list2`, and so on, for all iterations of the loop.
    #
    #This output state reflects the cumulative sum of every second element from each `list2` created during the loop's execution, with the sums being stored in the `final` list.
    for fin in final:
        print(fin)
        
    #State: `final` is an empty list.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer \( n \) and \( 2n \) integers. It calculates the sum of every second element from each group of \( 2n \) integers, starting from the first element, and stores these sums in a list. Finally, it prints each sum in the list.

