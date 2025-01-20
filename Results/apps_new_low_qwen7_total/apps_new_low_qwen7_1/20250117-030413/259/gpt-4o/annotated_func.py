#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 2 * 10^5, and ticket is a string of length n containing digits from '0' to '9' and '?' characters. The number of '?' characters in the ticket is even.
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
        
    #State of the program after the  for loop has been executed: `i` is \( n // 2 - 1 \), `left_sum` is the sum of all non-'?' characters in the first half of the ticket, and `left_question_marks` is the count of '?' characters in the first half of the ticket.
    for i in range(half_n, n):
        if ticket[i] == '?':
            right_question_marks += 1
        else:
            right_sum += int(ticket[i])
        
    #State of the program after the  for loop has been executed: `i` is `n-1`, `right_sum` is the sum of all non-'?' characters in the second half of the `ticket` list, and `right_question_marks` is the count of '?' characters in the second half of the `ticket` list.
    diff = left_sum - right_sum

q_diff = left_question_marks - right_question_marks
    if ((diff + q_diff // 2 * 9) % 9 == 0) :
        print('Bicarp')
    else :
        print('Monocarp')
    #State of the program after the if-else block has been executed: *`i` is n-1, `right_sum` is the sum of all non-'?' characters in the second half of the ticket list, `right_question_marks` is the count of '?' characters in the second half of the ticket list, `diff` is `left_sum - right_sum`, `q_diff` is `left_question_marks - right_question_marks`. If `((diff + q_diff // 2 * 9) % 9 == 0)`, no changes are made. Otherwise, no changes are made as well since the else part has the same conditions as the if part.
#Overall this is what the function does:The function `func_1` accepts an even integer `n` and a string `ticket` of length `n` containing digits from '0' to '9' and '?' characters, where the number of '?' characters is even. It calculates the sum of non-'?' characters and counts the '?' characters in two halves of the ticket. Based on these values, it determines whether the ticket can be considered "bicarp" or "monocarp". Specifically, it checks if the difference between the sums of non-'?' characters in the two halves plus half of the '?' characters (multiplied by 9) is divisible by 9. If true, it prints "Bicarp"; otherwise, it prints "Monocarp". The function handles the case where the number of '?' characters is even and ensures all necessary calculations are performed before making the final decision.

