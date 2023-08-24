# Question: 0124
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
The Duck song

For simplicity, we'll assume that there are only three types of grapes: green grapes, purple grapes and black grapes.

Andrew, Dmitry and Michal are all grapes' lovers, however their preferences of grapes are different. To make all of them happy, the following should happen: Andrew, Dmitry and Michal should eat at least $x$, $y$ and $z$ grapes, respectively. Andrew has an extreme affinity for green grapes, thus he will eat green grapes and green grapes only. On the other hand, Dmitry is not a fan of black grapes — any types of grapes except black would do for him. In other words, Dmitry can eat green and purple grapes. Michal has a common taste — he enjoys grapes in general and will be pleased with any types of grapes, as long as the quantity is sufficient.

Knowing that his friends are so fond of grapes, Aki decided to host a grape party with them. He has prepared a box with $a$ green grapes, $b$ purple grapes and $c$ black grapes.

However, Aki isn't sure if the box he prepared contains enough grapes to make everyone happy. Can you please find out whether it's possible to distribute grapes so that everyone is happy or Aki has to buy some more grapes?

It is not required to distribute all the grapes, so it's possible that some of them will remain unused.


-----Input-----

The first line contains three integers $x$, $y$ and $z$ ($1 \le x, y, z \le 10^5$) — the number of grapes Andrew, Dmitry and Michal want to eat.

The second line contains three integers $a$, $b$, $c$ ($1 \le a, b, c \le 10^5$) — the number of green, purple and black grapes in the box.


-----Output-----

If there is a grape distribution that allows everyone to be happy, print "YES", otherwise print "NO".


-----Examples-----
Input
1 6 2
4 3 3

Output
YES

Input
5 1 1
4 3 2

Output
NO



-----Note-----

In the first example, there is only one possible distribution:

Andrew should take $1$ green grape, Dmitry should take $3$ remaining green grapes and $3$ purple grapes, and Michal will take $2$ out of $3$ available black grapes.

In the second test, there is no possible distribution, since Andrew is not be able to eat enough green grapes. :(
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
# read input
x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

# check if there are enough grapes for each person
if a >= x and a + b >= x + y and a + b + c >= x + y + z:
    print("YES")
else:
    print("NO")
#@!CODE END!@#
````

---

