#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and the list of integers a_1, a_2, ..., a_n is provided, where each integer in the list is between 1 and n inclusive, and each integer from 1 to n appears at most twice in the list.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: Output State: The sum of the counts of each unique element in every second line (starting from the third line) of the input, divided by 3, for all lines processed by the loop.
#Overall this is what the function does:The function processes every second line starting from the third line of the input, counting the occurrences of each unique element in these lines, and then outputs the sum of these counts divided by 3. The function does not return any value but prints the result.

