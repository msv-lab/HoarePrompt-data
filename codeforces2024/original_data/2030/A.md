While exploring the jungle, you have bumped into a rare orangutan with a bow
tie! You shake hands with the orangutan and offer him some food and water. In
return...

The orangutan has gifted you an array a of length n . Using a , you will
construct two arrays b and c , both containing n elements, in the following
manner:

  * b_i = \min(a_1, a_2, \ldots, a_i) for each 1 \leq i \leq n . 
  * c_i = \max(a_1, a_2, \ldots, a_i) for each 1 \leq i \leq n . 

Define the score of a as \sum_{i=1}^n c_i - b_i (i.e. the sum of c_i - b_i
over all 1 \leq i \leq n ). Before you calculate the score, you can shuffle
the elements of a however you want.

Find the maximum score that you can get if you shuffle the elements of a
optimally.

Input

The first line contains t (1 \leq t \leq 100 ) — the number of test cases.

The first line of each test case contains an integer n (1 \leq n \leq 1000 ) —
the number of elements in a .

The following line contains n integers a_1, a_2, \ldots, a_n (1 \leq a_i \leq
1000 ) — the elements of the array a .

It is guaranteed that the sum of n over all test cases does not exceed 1000 .

Output

For each test case, output the maximum score that you can get.

Example

Input

    3
    
    1
    
    69
    
    3
    
    7 6 5
    
    5
    
    1 1 1 2 2

Output

    0
    4
    4
    
Note

In the first test case, there is no other way to rearrange a . So, b = [69]
and c = [69] . The only possible score is 69 - 69 = 0 .

In the second test case, you can rearrange a as [7, 5, 6] . Here, b = [7, 5,
5] and c = [7, 7, 7] . The score in this case is (7 - 7) + (7 - 5) + (7 - 5) =
4 . It can be shown this is the maximum possible score.
