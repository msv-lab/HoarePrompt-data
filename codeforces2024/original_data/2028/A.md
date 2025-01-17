Alice is trying to meet up with the Red Queen in the countryside! Right now,
Alice is at position (0, 0) , and the Red Queen is at position (a, b) . Alice
can only move in the four cardinal directions (north, east, south, west).

More formally, if Alice is at the point (x, y) , she will do one of the
following:

  * go north (represented by N), moving to (x, y+1) ; 
  * go east (represented by E), moving to (x+1, y) ; 
  * go south (represented by S), moving to (x, y-1) ; or 
  * go west (represented by W), moving to (x-1, y) . 

Alice's movements are predetermined. She has a string s representing a
sequence of moves that she performs from left to right. Once she reaches the
end of the sequence, she repeats the same pattern of moves forever.

Can you help Alice figure out if she will ever meet the Red Queen?

Input

Each test contains multiple test cases. The first line contains the number of
test cases t (1 \le t \le 500 ). The description of the test cases follows.

The first line of each test case contains three integers n , a , b (1 \le n ,
a , b \le 10 ) — the length of the string and the initial coordinates of the
Red Queen.

The second line contains a string s of length n consisting only of the
characters N, E, S, or W.

Output

For each test case, output a single string "YES" or "NO" (without the quotes)
denoting whether Alice will eventually meet the Red Queen.

You can output the answer in any case (upper or lower). For example, the
strings "yEs", "yes", "Yes", and "YES" will be recognized as positive
responses.

Example

Input

    6
    
    2 2 2
    
    NE
    
    3 2 2
    
    NNE
    
    6 2 1
    
    NNEESW
    
    6 10 10
    
    NNEESW
    
    3 4 2
    
    NEE
    
    4 5 5
    
    NEWS

Output

    YES
    NO
    YES
    YES
    YES
    NO
    
Note

In the first test case, Alice follows the path (0,0)
\xrightarrow[\texttt{N}]{} (0,1) \xrightarrow[\texttt{E}]{} (1,1)
\xrightarrow[\texttt{N}]{} (1,2) \xrightarrow[\texttt{E}]{} (2,2) .

In the second test case, Alice can never reach the Red Queen.
