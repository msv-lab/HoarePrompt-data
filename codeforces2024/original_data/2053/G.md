And I will: love the world that you've adored; wish the smile that you've
longed for. Your hand in mine as we explore, please take me to tomorrow's
shore.

— Faye Wong, [As Wished](https://www.youtube.com/watch?v=ZoJCN0pV7Qs)

Cocoly has a string t of length m , consisting of lowercase English letters,
and he would like to split it into parts. He calls a pair of strings (x, y)
beautiful if and only if there exists a sequence of strings a_1, a_2, \ldots,
a_k , such that:

  * t = a_1 + a_2 + \ldots + a_k , where + denotes string concatenation. 
  * For each 1 \leq i \leq k , at least one of the following holds: a_i = x , or a_i = y . 

Cocoly has another string s of length n , consisting of lowercase English
letters. Now, for each 1 \leq i < n , Cocoly wants you to determine whether
the pair of strings (s_1s_2 \ldots s_i, \, s_{i+1}s_{i+2} \ldots s_n) is
beautiful.

Note: since the input and output are large, you may need to optimize them for
this problem.

For example, in C++, it is enough to use the following lines at the start of
the main() function:

    int main() {  
        std::ios::sync_with_stdio(false);  
        std::cin.tie(nullptr); std::cout.tie(nullptr);  
    }  
    
Input

Each test contains multiple test cases. The first line contains an integer T
(1 \leq T \leq 10^5 ) — the number of test cases. The description of the test
cases follows.

The first line of each test case contains two integers n and m (2 \leq n \leq
m \leq 5 \cdot 10^6 ) — the lengths of s and the length of t .

The second line of each test case contains a single string s of length n ,
consisting only of lowercase English letters.

The third line of each test case contains a single string t of length m ,
consisting only of lowercase English letters.

It is guaranteed that the sum of m over all test cases does not exceed 10^7 .

Output

For each test case, output a single binary string r of length n - 1 : for each
1 \leq i < n , if the i -th pair is beautiful, r_i=\texttt{1} ; otherwise,
r_i=\texttt{0} . Do not output spaces.

Example

Input

    7
    
    3 5
    
    aba
    
    ababa
    
    4 10
    
    czzz
    
    czzzzzczzz
    
    5 14
    
    dream
    
    dredreamamamam
    
    5 18
    
    tcccc
    
    tcctccccctccctcccc
    
    7 11
    
    abababc
    
    abababababc
    
    7 26
    
    aaaaaaa
    
    aaaaaaaaaaaaaaaaaaaaaaaaaa
    
    19 29
    
    bbbbbbbbbbbbbbbbbbb
    
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbb

Output

    11
    011
    0010
    0000
    010100
    111111
    110010001100010011
    
Note

In the first test case, s = \tt aba , t = \tt ababa .

  * For i = 1 : Cocoly can split t = \texttt{a} + \texttt{ba} + \texttt{ba} , so the string pair (\texttt{a}, \texttt{ba}) is beautiful. 
  * For i = 2 : Cocoly can split t = \texttt{ab} + \texttt{ab} + \texttt{a} , so the string pair (\texttt{ab}, \texttt{a}) is beautiful. 

In the second test case, s = \tt czzz , t = \tt czzzzzczzz .

  * For i = 1 : It can be proven that there is no solution to give a partition of t using strings \texttt{c} and \texttt{zzz} . 
  * For i = 2 : Cocoly can split t into \texttt{cz} + \texttt{zz} + \texttt{zz} + \texttt{cz} + \texttt{zz} . 
  * For i = 3 : Cocoly can split t into \texttt{czz} + \texttt{z} + \texttt{z} + \texttt{z} + \texttt{czz} + \texttt{z} . 
