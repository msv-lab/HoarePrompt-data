I shall be looking for you who would be out of Existence.

— HyuN, [Disorder](https://soundcloud.com/k-sounds-studio/g2r2018-hyun-
disorder-feat-yuri)

There are always many repetitive tasks in life. Iris always dislikes them, so
she refuses to repeat them. However, time cannot be turned back; we only have
to move forward.

Formally, Iris has an integer sequence a_1, a_2, \ldots, a_n , where each
number in the sequence is between 1 and w , inclusive. It is guaranteed that w
\geq 2 .

Iris defines an operation as selecting two numbers a_i, a_{i+1} satisfying a_i
= a_{i+1} , and then changing them to two arbitrary integers within the range
[1, w] . Iris does not like equality, so she must guarantee that a_i \neq
a_{i+1} after the operation. Two identical pairs a_i, a_{i+1} can be selected
multiple times.

Iris wants to know the maximum possible sum of all elements of a after several
(possible, zero) operations, as well as the minimum number of operations
required to achieve this maximum value.

Input

Each test contains multiple test cases. The first line contains an integer t
(1 \leq t \leq 10^5 ) — the number of test cases. The description of the test
cases follows.

The first line of each test case contains two integers n and w (1 \leq n \leq
2\cdot 10^5 , 2 \leq w \leq 10^8 ) — the length of the array, and the maximum
allowed value of the elements.

The second line of each test case contains n integers a_1, a_2, \ldots, a_n (1
\leq a_i \leq w ) — the elements in the array.

It is guaranteed that the sum of n over all test cases does not exceed 10^6 .

Output

For each test case, output two integers — the maximum possible sum of all
elements of a and the minimum number of operations required, respectively.

Example

Input

    2
    
    5 8
    
    1 2 3 4 5
    
    7 5
    
    3 1 2 3 4 1 1

Output

    15 0
    34 6
    
Note

In the first test case, no operation can be performed so the answers are \sum
a_i = 15 and 0 , respectively.

In the second test case, the operations can be performed as follows:

It can be shown this is optimal, so we should output \sum a_i = 34 and the
number of operations, 6 , respectively.
