#State of the program right berfore the function call: tuples is a list of tuples, where each tuple contains numeric values (integers or floats).
def func_1(tuples):
    num_elements = len(tuples[0])
    averages = []
    for i in range(num_elements):
        elements_at_position = [t[i] for t in tuples]
        
        avg = sum(elements_at_position) / len(tuples)
        
        averages.append(avg)
        
    #State of the program after the  for loop has been executed: `averages` is a list of the averages of each position across all tuples in `tuples`, `num_elements` is the number of elements in the first tuple of `tuples`, `elements_at_position` is a list of the last element evaluated (last position across all tuples), `i` is `num_elements - 1`, and `avg` is the average of the last evaluated position across all tuples in `tuples`.
    return averages
    #`The program returns the list of averages 'averages' which contains the average of each position across all tuples in 'tuples'`
#Overall this is what the function does:The function `func_1` accepts a parameter `tuples`, which is a list of tuples containing numeric values (integers or floats). It calculates the average of the values at each position across all tuples in `tuples` and returns a list of these averages. The function iterates over each position in the tuples, collects the values at that position into a list, computes their average, and appends the result to the `averages` list. If the input list `tuples` is empty or any of the tuples within it is empty, the function will still execute correctly and return an empty list for `averages`.

