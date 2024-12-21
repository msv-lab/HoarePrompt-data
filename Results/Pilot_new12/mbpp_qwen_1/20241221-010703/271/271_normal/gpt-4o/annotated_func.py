#State of the program right berfore the function call: tuples is a list of tuples, where each tuple contains numerical values (integers or floats).
def func_1(tuples):
    num_elements = len(tuples[0])
    averages = []
    for i in range(num_elements):
        elements_at_position = [t[i] for t in tuples]
        
        avg = sum(elements_at_position) / len(tuples)
        
        averages.append(avg)
        
    #State of the program after the  for loop has been executed: `tuples` is a list of tuples, `num_elements` is a positive integer, `averages` is a list of `num_elements` elements, `elements_at_position` is a list of elements from each tuple in `tuples` at position `i`, `avg` is the sum of `elements_at_position` divided by the length of `tuples`.
    return averages
    #The program returns a list of `num_elements` elements, where each element is the average of the corresponding position's elements across all tuples in `tuples`
#Overall this is what the function does:The function `func_1` accepts a parameter `tuples`, which is a list of tuples containing numerical values. It calculates the average of the corresponding position's elements across all tuples in `tuples` and returns a list of these averages. The function iterates over each position in the tuples, collects the elements at that position from each tuple, computes their average, and appends it to the `averages` list. If the `tuples` list is empty, the function will return an empty list. This process handles both integer and float values within the tuples.

