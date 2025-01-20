#State of the program right berfore the function call: n is an even integer such that \(2 \leq n \leq 2 \cdot 10^5\), and ticket is a string of length n consisting of digits and '?' characters, where the number of '?' characters is even.
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
        
    #State of the program after the  for loop has been executed: `n` is an even integer such that \(2 \leq n \leq 2 \cdot 10^5\), `ticket` is a string of length `n` consisting of digits and '?' characters, where the number of '?' characters is even, `half_n` is \( \frac{n}{2} \) and must be at least 1, `i` is `half_n - 1`. `right_sum` and `right_question_marks` are 0. `left_sum` is the sum of the integer values of the non-'?' characters in the first half of `ticket`, and `left_question_marks` is the count of '?' characters in the first half of `ticket`.
    for i in range(half_n, n):
        if ticket[i] == '?':
            right_question_marks += 1
        else:
            right_sum += int(ticket[i])
        
    #State of the program after the  for loop has been executed: `n` is an even integer such that \(2 \leq n \leq 2 \cdot 10^5\), `half_n` is \( \frac{n}{2} \) and must be at least 1, `i` is `n - 1`, `left_sum` is the sum of the integer values of the non-'?' characters in the first half of `ticket`, `left_question_marks` is the count of '?' characters in the first half of `ticket`, `right_sum` is the sum of the integer values of the non-'?' characters in the second half of `ticket`, `right_question_marks` is the count of '?' characters in the second half of `ticket`. The loop executes if `n > 2`, and does not execute if `n = 2` and both characters in `ticket` are non-'?'.
    diff = left_sum - right_sum

q_diff = left_question_marks - right_question_marks
    if ((diff + q_diff // 2 * 9) % 9 == 0) :
        print('Bicarp')
    else :
        print('Monocarp')
    #State of the program after the if-else block has been executed: *`n` is an even integer such that \(2 \leq n \leq 2 \cdot 10^5\), `half_n` is \( \frac{n}{2} \) and must be at least 1, `i` is \( n - 1 \), `left_sum` is the sum of the integer values of the non-'?' characters in the first half of ticket, `left_question_marks` is the count of '?' characters in the first half of ticket, `right_sum` is the sum of the integer values of the non-'?' characters in the second half of ticket, `right_question_marks` is the count of '?' characters in the second half of ticket, `diff` is \( left_sum - right_sum \), `q_diff` is \( left_question_marks - right_question_marks \). If \( (diff + q_diff // 2 * 9) \% 9 == 0 \), the condition is true. Otherwise, the condition is false.
#Overall this is what the function does:The function `func_1` takes two parameters: `n` (an even integer within the range \(2 \leq n \leq 2 \cdot 10^5\)) and `ticket` (a string of length `n` containing digits and an even number of '?' characters). It calculates the sum of the integer values of the non-'?' characters in the first and second halves of the `ticket` string (`left_sum` and `right_sum`, respectively) and the count of '?' characters in each half (`left_question_marks` and `right_question_marks`). The function then determines whether the expression `(left_sum - right_sum + (left_question_marks - right_question_marks) // 2 * 9) % 9 == 0` holds true. If it does, the function prints 'Bicarp'; otherwise, it prints 'Monocarp'. The function does not return any value. Potential edge cases include when `n = 2` and both characters in `ticket` are non-'?', or when `ticket` contains only '?' characters. In these cases, the function still correctly evaluates the condition and prints the appropriate result.

