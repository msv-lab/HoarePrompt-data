#State of the program right berfore the function call: The input is a string in the format "ns" where n is a positive integer (1 ≤ n ≤ 10^18) representing the row number and s is a character from 'a' to 'f' representing the seat in that row.
def func():
    s = input().strip()

n = int(s[:-1])

seat = s[-1]

group = (n - 1) // 4

base_time = group * 8 * 3

row_position_in_group = (n - 1) % 4
    if (row_position_in_group == 0 or row_position_in_group == 2) :
        base_time += 0
    else :
        if (row_position_in_group == 1 or row_position_in_group == 3) :
            base_time += 7
        #State of the program after the if block has been executed: *s is the input string, n is the integer part of the input string, seat is the last character of the input string, group is (n - 1) // 4, and row_position_in_group is (n - 1) % 4. If row_position_in_group is 1 or 3, base_time is (group * 24) + 7. Otherwise, base_time remains as group * 24.
    #State of the program after the if-else block has been executed: *s is the input string, n is the integer part of the input string, seat is the last character of the input string, group is (n - 1) // 4, and row_position_in_group is (n - 1) % 4. If row_position_in_group is 0 or 2, base_time remains as group * 24. If row_position_in_group is 1 or 3, base_time is (group * 24) + 7.
    seat_time = {'f': 0, 'e': 1, 'd': 2, 'c': 3, 'b': 4, 'a': 5}[seat]

total_time = base_time + seat_time + 1

print(total_time)
#Overall this is what the function does:The function processes a string input in the format "ns", where `n` is a positive integer (1 ≤ n ≤ 10^18) representing the row number, and `s` is a character from 'a' to 'f' representing the seat in that row. It calculates and prints a total time based on the following logic:
- The row number `n` is divided into groups of 4 rows each.
- Each group contributes a base time of 24 units.
- Rows 1 and 3 within a group add an additional 7 units to the base time.
- The seat position contributes an additional 0 to 5 units, depending on the seat letter ('f' to 'a').
- A final constant of 1 unit is added to the total time.
The function does not return any value; instead, it prints the calculated total time. Edge cases include very large values of `n` (up to 10^18), which should still be handled correctly by the function.

