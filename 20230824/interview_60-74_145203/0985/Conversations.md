# Question: 0985
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
Today, Wet Shark is given n bishops on a 1000 by 1000 grid. Both rows and columns of the grid are numbered from 1 to 1000. Rows are numbered from top to bottom, while columns are numbered from left to right.

Wet Shark thinks that two bishops attack each other if they share the same diagonal. Note, that this is the only criteria, so two bishops may attack each other (according to Wet Shark) even if there is another bishop located between them. Now Wet Shark wants to count the number of pairs of bishops that attack each other.


-----Input-----

The first line of the input contains n (1 ≤ n ≤ 200 000) — the number of bishops.

Each of next n lines contains two space separated integers x_{i} and y_{i} (1 ≤ x_{i}, y_{i} ≤ 1000) — the number of row and the number of column where i-th bishop is positioned. It's guaranteed that no two bishops share the same position.


-----Output-----

Output one integer — the number of pairs of bishops which attack each other. 


-----Examples-----
Input
5
1 1
1 5
3 3
5 1
5 5

Output
6

Input
3
1 1
2 3
3 5

Output
0



-----Note-----

In the first sample following pairs of bishops attack each other: (1, 3), (1, 5), (2, 3), (2, 4), (3, 4) and (3, 5). Pairs (1, 2), (1, 4), (2, 5) and (4, 5) do not attack each other because they do not share the same diagonal.
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
def count_attacking_pairs(n, bishops):
    pair_count = 0
    row_diagonal_count = [0] * 2001
    col_diagonal_count = [0] * 2001

    for bishop in bishops:
        row, col = bishop
        diagonal = row + col
        reverse_diagonal = row - col + 1000

        pair_count += row_diagonal_count[diagonal]
        pair_count += col_diagonal_count[reverse_diagonal]

        row_diagonal_count[diagonal] += 1
        col_diagonal_count[reverse_diagonal] += 1

    return pair_count


n = int(input())
bishops = [list(map(int, input().split())) for _ in range(n)]

result = count_attacking_pairs(n, bishops)
print(result)
#@!CODE END!@#
````

---

