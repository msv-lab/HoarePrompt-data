#State of the program right berfore the function call: n is an even integer between 2 and 2 * 10^5, and ticket is a string of length n containing digits and '?' characters, where the number of '?' characters is even.
def func_1(n, ticket):
    half_n = n // 2

left_sum = 0

right_sum = 0

left_question_marks = 0

right_question_marks = 0
    for i in range(half_n):
        if ticket[i] == '?':
            left_question_marks += 1
        else:
            left_sum += int(ticket[i])
        
    #State of the program after the  for loop has been executed: `left_sum` is the sum of all non-question mark characters from index 0 to `half_n - 1`, `left_question_marks` is the count of question mark characters from index 0 to `half_n - 1`, `n` and `half_n` remain unchanged, `ticket` remains unchanged, and `right_sum` and `right_question_marks` remain 0.
    for i in range(half_n, n):
        if ticket[i] == '?':
            right_question_marks += 1
        else:
            right_sum += int(ticket[i])
        
    #State of the program after the  for loop has been executed: Output State: `left_sum` is the sum of all non-question mark characters from index 0 to `half_n - 1`, `left_question_marks` is the count of question mark characters from index 0 to `half_n - 1`, `half_n` must be less than `n`, `ticket` remains unchanged, and `right_sum` is the sum of all non-question mark characters from index `half_n` to `n - 1`, `right_question_marks` is the count of question mark characters from index `half_n` to `n - 1`.
    #
    #Explanation:
    #1. **Analyze the Code and Initial State**: The loop iterates over the second half of the `ticket` string from index `half_n` to `n - 1`. It updates `right_sum` by adding the integer value of each non-question mark character encountered and increments `right_question_marks` by 1 for each question mark encountered.
    #
    #2. **Track Variable Changes**:
    #   - `left_sum` and `left_question_marks` remain constant throughout the loop as they are initialized before the loop starts.
    #   - `right_sum` and `right_question_marks` are updated inside the loop based on the current character being processed.
    #   - `half_n` and `n` remain unchanged.
    #   - `ticket` remains unchanged.
    #
    #3. **Summarize the Loop Behavior**: The loop processes each character in the second half of the `ticket` string once. For each character, it either adds its integer value to `right_sum` or increments `right_question_marks` by 1 if the character is a question mark.
    #
    #4. **Verify Relationships**: After the loop completes, `right_sum` contains the sum of all non-question mark characters from index `half_n` to `n - 1`, and `right_question_marks` contains the count of question mark characters from index `half_n` to `n - 1`. These values are consistent with the behavior of the loop and the provided output states.
    #
    #Thus, the final output state after the loop finishes is:
    #Output State: `left_sum` is the sum of all non-question mark characters from index 0 to `half_n - 1`, `left_question_marks` is the count of question mark characters from index 0 to `half_n - 1`, `half_n` must be less than `n`, `ticket` remains unchanged, and `right_sum` is the sum of all non-question mark characters from index `half_n` to `n - 1`, `right_question_marks` is the count of question mark characters from index `half_n` to `n - 1`.
    diff = left_sum - right_sum

q_diff = left_question_marks - right_question_marks
    if ((diff + q_diff // 2 * 9) % 9 == 0) :
        print('Bicarp')
    else :
        print('Monocarp')
    #State of the program after the if-else block has been executed: `left_sum` is the sum of all non-question mark characters from index 0 to half_n - 1, `left_question_marks` is the count of question mark characters from index 0 to half_n - 1, `half_n` must be less than `n`, `ticket` remains unchanged, `right_sum` is the sum of all non-question mark characters from index half_n to n - 1, `right_question_marks` is the count of question mark characters from index half_n to n - 1, `diff` is the difference between `left_sum` and `right_sum`, `q_diff` is the difference between `left_question_marks` and `right_question_marks`. If `(diff + q_diff // 2 * 9) % 9 == 0`, then the string 'Bicarp' is printed to the console. Otherwise, the string 'Monocarp' is printed.
#Overall this is what the function does:The function `func_1` accepts two parameters: an even integer `n` and a string `ticket` of length `n` containing digits and '?' characters. The function calculates the sum of non-question mark characters and counts the number of question marks in the first and second halves of the `ticket` string. Based on these calculations, it determines whether the ticket is 'Bicarp' or 'Monocarp' and prints the result to the console.

