#State of the program right berfore the function call: The function `func` is expected to process inputs representing events and friends' names, where the number of events `n` and the number of friends `m` are integers within the ranges 1 ≤ n ≤ 10^5 and 1 ≤ m ≤ 40. The events consist of changes to Hiasat's handle and visits by friends, with each friend's name being a string of lowercase Latin letters and having a length of 1 to 40 characters. The first event is always a handle change, and each friend visits Hiasat's profile at least once.
def func():
    n, m = [int(x) for x in raw_input().split()]
    start_counting = 'NO'
    counter = {}
    final_cnt = 0
    for i in range(0, n):
        tmp_str = raw_input().split()
        
        state = int(tmp_str[0])
        
        if state == 1:
            if start_counting == 'YES':
                if len(counter):
                    final_cnt += max(counter.values())
                counter = {}
            start_counting = 'YES'
        else:
            frnd = tmp_str[1]
            if frnd in counter:
                counter[frnd] += 1
            else:
                counter[frnd] = 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `m` is an input integer, `start_counting` is 'YES' if any `state` in the input lines was 1, otherwise it remains 'NO', `final_cnt` is the sum of the maximum values in `counter` each time `state` is 1 and `start_counting` is 'YES', `counter` is an empty dictionary if the last `state` is 1, otherwise it contains the counts of friends (if any) from the last segment of input where `start_counting` was 'YES', `tmp_str` is the list of the last input line split by spaces, `state` is the integer value of the last `tmp_str[0]`, and `frnd` is the last friend string from `tmp_str[1]` if `state` is not 1.
    if (start_counting == 'YES') :
        if len(counter) :
            final_cnt += max(counter.values())
        #State of the program after the if block has been executed: *`n` is an input integer, `m` is an input integer, `start_counting` is 'YES', `final_cnt` is the sum of the maximum values in `counter` each time `state` is 1 and `start_counting` is 'YES'. If `counter` is non-empty, `final_cnt` is updated to include the maximum value in `counter`, and `counter` remains a non-empty dictionary containing the counts of friends (if any) from the last segment of input where `start_counting` was 'YES'. `tmp_str` is the list of the last input line split by spaces, `state` is the integer value of the last `tmp_str[0]`, and `frnd` is the last friend string from `tmp_str[1]` if `state` is not 1.
    #State of the program after the if block has been executed: *`n` is an input integer, `m` is an input integer, `start_counting` is either 'YES' or 'NO', `final_cnt` is the sum of the maximum values in `counter` each time `state` is 1 and `start_counting` is 'YES'. If `start_counting` is 'YES', and `counter` is non-empty, `final_cnt` is updated to include the maximum value in `counter`, and `counter` remains a non-empty dictionary containing the counts of friends (if any) from the last segment of input where `start_counting` was 'YES'. `tmp_str` is the list of the last input line split by spaces, `state` is the integer value of the last `tmp_str[0]`, and `frnd` is the last friend string from `tmp_str[1]` if `state` is not 1. If `start_counting` is 'NO', `counter` is an empty dictionary, and `final_cnt` remains unchanged.
    print(final_cnt)
#Overall this is what the function does:The function processes a series of events related to changes in Hiasat's handle and visits by friends. It takes two integers `n` and `m` as input, where `n` represents the number of events and `m` represents the number of friends. Each event is read from the standard input and can be one of two types: a handle change (state 1) or a friend visit (state 2). The function maintains a count of the maximum number of unique friends who visited Hiasat's profile between handle changes. After processing all events, it prints the total count of these maximum values. The function does not return any value; instead, it outputs the result directly. Edge cases include scenarios where no handle changes occur, or where the last segment of events does not end with a handle change, both of which are handled correctly by the function.

