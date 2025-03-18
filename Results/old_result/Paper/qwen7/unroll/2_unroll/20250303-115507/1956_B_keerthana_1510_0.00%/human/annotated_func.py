#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the list a contains n integers such that 1 ≤ a_i ≤ n and each integer from 1 to n appears at most twice in the list a.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: Output State: The sum of counts of each unique element in every alternate line of the input file, where the count of each element is divided by 3 and rounded down, printed for each line.
    #
    #This means that for each line in the input file starting from the third line and skipping every other line, the code processes the line, counts the occurrences of each unique element, divides these counts by 3 (rounding down), and then prints the sum of these divisions.
#Overall this is what the function does:The function reads input from stdin, processes every alternate line starting from the third line, counts the occurrences of each unique element in these lines, divides these counts by 3 (rounding down), and prints the sum of these divisions for each line. The function does not return any value but outputs the results directly.

