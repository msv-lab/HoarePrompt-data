
Given a Python loop, an initial execution state, and the output states after the first 3 iterations of the loop, determine the output state after all the executions of the loop have finished. 

You must adhere to the text format: Output State: **output state.**

Initial State: `arr` is a list of integers, and the length of `arr` is greater than or equal to 2; `min_diff` is set to infinity (`float('inf')`); `temp` is the first element of `arr`.
Code of the loop:
for i in range(1, len(arr)):
    diff = abs(arr[i] - temp)
    if diff < min_diff:
        min_diff = diff


The output state after the loop executes the first 3 of times includes what needed to be true for the loop to execute at least that number of times:

Output State after the loop executes 1 time: *`arr` is a list of integers with a length of at least 2, `min_diff` is the minimum of its initial value (infinity) and the absolute difference between the first two elements of `arr`, `temp` is the first element of `arr`, `i` is 1, and `diff` is the absolute difference between the second element of `arr` and the first element of `arr`. If `diff` is less than the initial `min_diff`, `min_diff` is updated to `diff`.

**Output State after the loop executes 2 times**: *`arr` is a list of integers with a length of at least 3, `temp` is the first element of `arr`, `i` is 2, `diff` is the absolute difference between the third element of `arr` and the first element of `arr`. If `diff` is less than the initial `min_diff`, `min_diff` is updated to `diff`. Otherwise, `min_diff` remains unchanged.

**Output State after the loop executes 3 times**: *`arr` is a list of integers with a length of at least 3, `temp` is the first element of `arr`, `i` is 3, `diff` is the absolute difference between the fourth element of `arr` and the first element of `arr`. If `diff` is less than the initial `min_diff`, then `min_diff` is updated to `diff`. Otherwise, `min_diff` remains unchanged.




What is the ouput state after the loop executes all the iterations? Change the values of only the variables in the loop head and body.The state of the other variables in the precondition that are not affected by the loop head and body must remain unchanged.
In your response strictly use the format: Output State: **the output state you calculate.**, and describe this output state in Natural language easily understandable by humans.

