# Question: 0564
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
Sereja showed an interesting game to his friends. The game goes like that. Initially, there is a table with an empty cup and n water mugs on it. Then all players take turns to move. During a move, a player takes a non-empty mug of water and pours all water from it into the cup. If the cup overfills, then we assume that this player lost.

As soon as Sereja's friends heard of the game, they wanted to play it. Sereja, on the other hand, wanted to find out whether his friends can play the game in such a way that there are no losers. You are given the volumes of all mugs and the cup. Also, you know that Sereja has (n - 1) friends. Determine if Sereja's friends can play the game so that nobody loses.


-----Input-----

The first line contains integers n and s (2 ≤ n ≤ 100; 1 ≤ s ≤ 1000) — the number of mugs and the volume of the cup. The next line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10). Number a_{i} means the volume of the i-th mug.


-----Output-----

In a single line, print "YES" (without the quotes) if his friends can play in the described manner, and "NO" (without the quotes) otherwise.


-----Examples-----
Input
3 4
1 1 1

Output
YES

Input
3 4
3 1 3

Output
YES

Input
3 4
4 4 4

Output
NO
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
n, s = map(int, input().split())
mugs = list(map(int, input().split()))

# Sort the mugs in increasing order of volume
mugs.sort()

# Calculate the total volume of all mugs except the largest one
total_volume = sum(mugs[:-1])

# If the total volume is less than or equal to the cup volume, the friends can play without anyone losing
if total_volume <= s:
    print("YES")
else:
    print("NO")
#@!CODE END!@#
````

---

