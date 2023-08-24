# Question: 4182
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
Our world is one-dimensional, and ruled by two empires called Empire A and Empire B.
The capital of Empire A is located at coordinate X, and that of Empire B is located at coordinate Y.
One day, Empire A becomes inclined to put the cities at coordinates x_1, x_2, ..., x_N under its control, and Empire B becomes inclined to put the cities at coordinates y_1, y_2, ..., y_M under its control.
If there exists an integer Z that satisfies all of the following three conditions, they will come to an agreement, but otherwise war will break out.
 - X < Z \leq Y
 - x_1, x_2, ..., x_N < Z
 - y_1, y_2, ..., y_M \geq Z
Determine if war will break out.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N, M \leq 100
 - -100 \leq X < Y \leq 100
 - -100 \leq x_i, y_i \leq 100
 - x_1, x_2, ..., x_N \neq X
 - x_i are all different.
 - y_1, y_2, ..., y_M \neq Y
 - y_i are all different.

-----Input-----
Input is given from Standard Input in the following format:
N M X Y
x_1 x_2 ... x_N
y_1 y_2 ... y_M

-----Output-----
If war will break out, print War; otherwise, print No War.

-----Sample Input-----
3 2 10 20
8 15 13
16 22

-----Sample Output-----
No War

The choice Z = 16 satisfies all of the three conditions as follows, thus they will come to an agreement.
 - X = 10 < 16 \leq 20 = Y
 - 8, 15, 13 < 16
 - 16, 22 \geq 16
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
# Read inputs
N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# Check if war will break out
if X < min(y) <= Y and max(x) < min(y):
    print("No War")
else:
    print("War")
#@!CODE END!@#
````

---

