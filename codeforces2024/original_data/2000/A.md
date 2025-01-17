Dmitry wrote down t integers on the board, and that is good. He is sure that
he lost an important integer n among them, and that is bad.

The integer n had the form \text{10^x} (x \ge 2 ), where the symbol '\text{^}
' denotes exponentiation.. Something went wrong, and Dmitry missed the symbol
'\text{^} ' when writing the important integer. For example, instead of the
integer 10^5 , he would have written 105 , and instead of 10^{19} , he would
have written 1019 .

Dmitry wants to understand which of the integers on the board could have been
the important integer and which could not.

Input

The first line of the input contains one integer t (1 \le t \le 10^4 ) — the
number of integers on the board.

The next t lines each contain an integer a (1 \le a \le 10000 ) — the next
integer from the board.

Output

For each integer on the board, output "YES" if it could have been the
important integer and "NO" otherwise.

You may output each letter in any case (lowercase or uppercase). For example,
the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive
answer.

Example

Input

    7
    
    100
    
    1010
    
    101
    
    105
    
    2033
    
    1019
    
    1002

Output

    NO
    YES
    NO
    YES
    NO
    YES
    NO
    