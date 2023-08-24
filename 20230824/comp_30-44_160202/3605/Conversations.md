# Question: 3605
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
Andy is going holiday shopping and needs to buy several Christmas trees. At the store, there is a row of Christmas trees of various heights. Andy is only allowed to buy trees that are next to each other, i.e. trees that are contiguous within the row. He also wants to make sure that the shortest tree he buys and the tallest tree he buys are as close in height as possible. What is the smallest height difference he can get given the constraints?

-----Input-----
The input consists of two lines. The first line contains two integers $n$ and $k$ ($2 \leq k \leq n \leq 200000$), representing the number of trees in the row and the number of trees Andy needs to buy, respectively. The second line consists of $n$ integers $a_1, a_2, \ldots , a_ n$ where $1 \leq a_ i \leq 100$, representing the height of each tree.

-----Output-----
Output the minimum height difference between the shortest and tallest trees of any contiguous subrange of $k$ trees.

-----Examples-----
Sample Input:
10 2
1 3 5 7 9 11 13 15 17 16
Sample Output:
1
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
n, k = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

min_diff = float('inf')
for i in range(n-k+1):
    diff = trees[i+k-1] - trees[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)
#@!CODE END!@#
````

---

