You are given a list of n integers a_1, a_2, \dots, a_n . You need to pick 8
elements from the list and use them as coordinates of four points. These four
points should be corners of a rectangle which has its sides parallel to the
coordinate axes. Your task is to pick coordinates in such a way that the
resulting rectangle has the maximum possible area. The rectangle can be
degenerate, i. e. its area can be 0 . Each integer can be used as many times
as it occurs in the list (or less).

Input

The first line contains one integer t (1 \le t \le 25\,000 ) — the number of
test cases.

The first line of each test case contains one integer n (8 \le n \le 2 \cdot
10^5 ).

The second line of each test case contains n integers a_1, a_2, \dots, a_n
(-10^9 \le a_i \le 10^9 ).

Additional constraint on the input: the sum of n over all test cases does not
exceed 2 \cdot 10^5 .

Output

For each test case, print the answer as follows:

  * if it is impossible to construct a rectangle which meets the constraints from the statement, print a single line containing the word NO (case-insensitive); 
  * otherwise, in the first line, print YES (case-insensitive). In the second line, print 8 integers x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4 — the coordinates of the corners of the rectangle. You can print the corners in any order. 

Example

Input

    3
    
    16
    
    -5 1 1 2 2 3 3 4 4 5 5 6 6 7 7 10
    
    8
    
    0 0 -1 2 2 1 1 3
    
    8
    
    0 0 0 0 0 5 0 5

Output

    YES
    1 2 1 7 6 2 6 7
    NO
    YES
    0 0 0 5 0 0 0 5
    