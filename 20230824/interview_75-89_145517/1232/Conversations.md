# Question: 1232
## Generation 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Coding Contest Participant. Imagine that you are taking part in a prestigious coding competition. Your task is to design an efficient algorithm for a complex problem. You need to consider all possible edge cases, optimize for efficiency, and ensure that your solution is clean and readable. In addition, provide a Python code of your solution, and put the solution in a code delimiter.For example:
### QUESTION
A. Watermelon
time limit per test: 1 second
memory limit per test: 64 megabytes
input: standard input
output: standard output
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 <= w <= 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
input
8
output
YES
Note
For example, the boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos).

### Expected response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w < 4:
print("NO")
else:
print("YES")
#@!CODE END!@#
````

---

**role**: 
````markdown
user
````

---

**content**: 
````markdown
### QUESTION
You are given two arrays A and B consisting of integers, sorted in non-decreasing order. Check whether it is possible to choose k numbers in array A and choose m numbers in array B so that any number chosen in the first array is strictly less than any number chosen in the second array.


-----Input-----

The first line contains two integers n_{A}, n_{B} (1 ≤ n_{A}, n_{B} ≤ 10^5), separated by a space — the sizes of arrays A and B, correspondingly.

The second line contains two integers k and m (1 ≤ k ≤ n_{A}, 1 ≤ m ≤ n_{B}), separated by a space.

The third line contains n_{A} numbers a_1, a_2, ... a_{n}_{A} ( - 10^9 ≤ a_1 ≤ a_2 ≤ ... ≤ a_{n}_{A} ≤ 10^9), separated by spaces — elements of array A.

The fourth line contains n_{B} integers b_1, b_2, ... b_{n}_{B} ( - 10^9 ≤ b_1 ≤ b_2 ≤ ... ≤ b_{n}_{B} ≤ 10^9), separated by spaces — elements of array B.


-----Output-----

Print "YES" (without the quotes), if you can choose k numbers in array A and m numbers in array B so that any number chosen in array A was strictly less than any number chosen in array B. Otherwise, print "NO" (without the quotes).


-----Examples-----
Input
3 3
2 1
1 2 3
3 4 5

Output
YES

Input
3 3
3 3
1 2 3
3 4 5

Output
NO

Input
5 2
3 1
1 1 1 1 1
2 2

Output
YES



-----Note-----

In the first sample test you can, for example, choose numbers 1 and 2 from array A and number 3 from array B (1 < 3 and 2 < 3).

In the second sample test the only way to choose k elements in the first array and m elements in the second one is to choose all numbers in both arrays, but then not all the numbers chosen in A will be less than all the numbers chosen in B: $3 < 3$.
### Requirements
1. Use Standard Input Format (read inputs with `input()`, write results with `print()`)
2. You will NOT return anything except for the program. 
3. DO NOT WRITE PLANS OR EXPLANATIONS
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
#@!CODE START!@#
nA, nB = map(int, input().split())
k, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Check if the maximum number in A is strictly less than the minimum number in B
if A[k-1] < B[nB-m]:
    print("YES")
else:
    print("NO")
#@!CODE END!@#
````

---

