#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, and for each participant i, a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 4126, representing the rating of the i-th participant before and after the round, respectively. The participants are ordered from the top to the bottom of the standings.
def func():
    n = int(input())

ratings_before = []

ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: n is an integer such that 0 ≤ n ≤ 0, ratings_before is [a, a_new, ..., a_final] with n elements, ratings_after is [b, b_new, ..., b_final] with n elements, _ is not used
    rated = False

unrated = True

maybe = True
    for i in range(n):
        for j in range(i + 1, n):
            if ratings_before[i] < ratings_before[j] and ratings_after[i
                ] > ratings_after[j]:
                unrated = False
                break
        
        if not unrated:
            break
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `i` is at least 0 and less than `n`, `ratings_before` is [], `ratings_after` is [], `_` is not used, `rated` is False, `unrated` is False, `maybe` is True. If `unrated` is set to False during any iteration, the loop terminates immediately. The loop will not execute if `n` is 0.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `i` is `n-1` or less, `ratings_before` is [], `ratings_after` is [], `_` is not used, `rated` is True if any `ratings_before[j]` is different from `ratings_after[j]` for `j` in range(`n`), otherwise `rated` is False, `unrated` is False, `maybe` is True. The loop will terminate if `unrated` is set to False during any iteration, or it will complete all iterations if no such condition is met.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is greater than 0, `i` is `n-1` or less, `ratings_before` is [], `ratings_after` is [], `_` is not used, `rated` is False, `maybe` is True. If `unrated` is True, the state remains unchanged. If `unrated` is False, the state remains unchanged except `unrated` is False.
    #State of the program after the if-else block has been executed: *`n` is greater than 0, `i` is `n-1` or less, `ratings_before` is [], `ratings_after` is [], `_` is not used, `maybe` is True. If `rated` is True, then at least one `ratings_before[j]` is different from `ratings_after[j]` for `j` in range(`n`), and `unrated` is False. If `rated` is False, then `rated` remains False, and `unrated` remains unchanged (either True or False).
#Overall this is what the function does:This function reads an integer `n` representing the number of participants in a competition, where `2 ≤ n ≤ 1000`. For each participant, it reads two integers `a_i` and `b_i` (where `1 ≤ a_i, b_i ≤ 4126`), representing the rating of the participant before and after the competition, respectively. The participants are ordered from the top to the bottom of the standings. The function then determines the type of the competition based on the following criteria:
- If any participant's rating has changed (`a_i ≠ b_i` for any `i`), the competition is classified as "rated".
- If the relative order of any two participants has changed (i.e., if `a_i < a_j` but `b_i > b_j` for any `i < j`), the competition is classified as "unrated".
- If neither of the above conditions is met, the competition is classified as "maybe".

The function prints one of the three possible outcomes: "rated", "unrated", or "maybe". After the function executes, the state of the program is:
- `n` is an integer such that `2 ≤ n ≤ 1000`.
- `ratings_before` and `ratings_after` are lists containing the ratings before and after the competition, respectively, each with `n` elements.
- The variables `rated`, `unrated`, and `maybe` are boolean values that determine the classification of the competition.
- The function does not return any value; it only prints the result to the console.

