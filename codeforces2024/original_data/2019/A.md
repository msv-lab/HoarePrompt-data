[EnV - Dynasty](https://soundcloud.com/envyofficial/env-dynasty)

⠀

You are given an array a_1, a_2, \ldots, a_n of positive integers.

You can color some elements of the array red, but there cannot be two adjacent
red elements (i.e., for 1 \leq i \leq n-1 , at least one of a_i and a_{i+1}
must not be red).

Your score is the maximum value of a red element plus the number of red
elements. Find the maximum score you can get.

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 500 ). The description of the test cases follows.

The first line of each test case contains a single integer n (1 \le n \le 100
) — the length of the array.

The second line of each test case contains n integers a_1, a_2, \ldots, a_n (1
\le a_i \le 1000 ) — the given array.

Output

For each test case, output a single integer: the maximum possible score you
can get after coloring some elements red according to the statement.

Example

Input

    4
    
    3
    
    5 4 5
    
    3
    
    4 5 4
    
    10
    
    3 3 3 3 4 1 2 3 4 5
    
    9
    
    17 89 92 42 29 92 14 70 45

Output

    7
    6
    10
    97
    
Note

In the first test case, you can color the array as follows: [\color{red}{5},
4, \color{red}{5}] . Your score is \max([5, 5]) + \text{size}([5, 5]) = 5+2 =
7 . This is the maximum score you can get.

In the second test case, you can color the array as follows: [\color{red}{4},
5, \color{red}{4}] . Your score is \max([4, 4]) + \text{size}([4, 4]) = 4+2 =
6 . This is the maximum score you can get.

In the third test case, you can color the array as follows: [\color{red}{3},
3, \color{red}{3}, 3, \color{red}{4}, 1, 2, \color{red}{3}, 4, \color{red}{5}]
. Your score is \max([3, 3, 4, 3, 5]) + \text{size}([3, 3, 4, 3, 5]) = 5+5 =
10 . This is the maximum score you can get.
