Is the given Python program correct based on the problem description and the correct execution states of the program provided as comment?



# Problem:
Given an integer list, the task is to find the maximum product of any sublist.


# Annotated Program:

#State: xs is a list of integers.
def func_1(xs):
    if (not xs) :
        return float('-inf')
        #The program returns -inf
    #State: xs is a list of integers, and xs is not empty
    min_ending_here = xs[0]
    max_ending_here = xs[0]
    best_so_far = xs[0]
    for num in xs[1:]:
        temp = max_ending_here * num
        
        max_ending_here = max(num, temp, min_ending_here * num)
        
        min_ending_here = min(num, temp, min_ending_here * num)
        
    #State: `xs remains the same, num is the last element of xs, temp is the product of max_ending_here and num after the last iteration, max_ending_here is the maximum product of any sublist ending at the last element of xs, min_ending_here is the minimum product of any sublist ending at the last element of xs, best_so_far is the first element of xs.
    if (max_ending_here > best_so_far) :
        best_so_far = max_ending_here
    #State: *`xs` is a list of integers; `min_ending_here` is the minimum product of sublists ending at the last element of `xs`; `max_ending_here` is the maximum product of sublists ending at the last element of `xs`. If `max_ending_here` is greater than `best_so_far`, then `best_so_far` is updated to the value of `max_ending_here`. Otherwise, `best_so_far` remains unchanged.
    return best_so_far

Reply Correctness: **True**  if the given program is correct or Correctness: **False**  if the given program is incorrect.