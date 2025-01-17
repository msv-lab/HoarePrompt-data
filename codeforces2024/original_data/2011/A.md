Jane has decided to solve a list of n problems on Codeforces. The i -th
problem in her list has difficulty d_i , and the last problem in the list is
the hardest one (for every problem j < n , d_j < d_n ).

Jane's problem-solving skill is some integer x (unknown to you). If a
problem's difficulty is greater than x , then Jane cannot solve it, otherwise
she can solve it.

Jane has solved all problems form the list, except for the last one — she
found out that it was too difficult for her. Can you uniquely determine the
value of x — Jane's problem solving skill?

Input

The first line contains one integer t (1 \le t \le 1000 ) — the number of test
cases.

Each test case consists of two lines:

  * the first line contains one integer n (2 \le n \le 50 ) — the number of problems; 
  * the second line contains n integers d_1, d_2, \dots, d_n (1 \le d_i \le 50 ). 

Additional constraint on the input: in every test case, the last problem is
more difficult than every other problem (i. e. d_n > d_j for every j < n ).
This means that at least one possible value of x exists.

Output

For each test case, print one line:

  * if you can determine the value of x uniquely, print x ; 
  * otherwise, print Ambiguous. The checking program is case-sensitive, so if you print ambiguous or AMBIGUOUS, your answer will be considered wrong. 

Example

Input

    3
    
    5
    
    1 2 3 4 5
    
    8
    
    8 8 5 3 4 6 8 12
    
    4
    
    3 3 3 4

Output

    4
    Ambiguous
    3
    
Note

In the second test case of the example, the value of x could be 11 , but it
also could be 10 (other possible values for x also exist).
