# Use Standard Input format

def determine_winner(n, ticket):
    half_n = n // 2
    left_sum = 0
    right_sum = 0
    left_question_marks = 0
    right_question_marks = 0

    # Calculate the sums and the count of question marks for each half
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

    # Calculate the difference between the sums of the two halves
    diff = left_sum - right_sum

    # Calculate the difference in the number of question marks
    q_diff = left_question_marks - right_question_marks

    # To balance the sums, the difference must be a multiple of 9
    if (diff + (q_diff // 2) * 9) % 9 == 0:
        print("Bicarp")
    else:
        print("Monocarp")

# Read input
n = int(input())
ticket = input()

# Determine the winner
determine_winner(n, ticket)
