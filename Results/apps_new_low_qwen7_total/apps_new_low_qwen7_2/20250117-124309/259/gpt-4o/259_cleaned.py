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
    for i in range(half_n, n):
        if ticket[i] == '?':
            right_question_marks += 1
        else:
            right_sum += int(ticket[i])
    diff = left_sum - right_sum
    q_diff = left_question_marks - right_question_marks
    if (diff + q_diff // 2 * 9) % 9 == 0:
        print('Bicarp')
    else:
        print('Monocarp')
n = int(input())
ticket = input()
func_1(n, ticket)