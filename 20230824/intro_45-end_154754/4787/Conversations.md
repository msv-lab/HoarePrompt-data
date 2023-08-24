# Question: 4787
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
Seven Wonders is a card drafting game in which players build structures to earn points. The player who ends with the most points wins. One winning strategy is to focus on building scientific structures. There are three types of scientific structure cards: Tablet (‘T’), Compass (‘C’), and Gear (‘G’). For each type of cards, a player earns a number of points that is equal to the squared number of that type of cards played. Additionally, for each set of three different scientific cards, a player scores $7$ points. 

For example, if a player plays $3$ Tablet cards, $2$ Compass cards and $1$ Gear card, she gets $3^2 + 2^2 + 1^2 + 7 = 21$ points.

It might be tedious to calculate how many scientific points a player gets by the end of each game. Therefore, you are here to help write a program for the calculation to save everyone’s time.

-----Input-----
The input has a single string with no more than $50$ characters. The string contains only letters ‘T’, ‘C’ or ‘G’, which denote the scientific cards a player has played in a Seven Wonders game.

-----Output-----
Output the number of scientific points the player earns.

-----Note-----
Seven Wonders was created by Antoine Bauza, and published by Repos Production. Antoine Bauza and Repos Production do not endorse and have no involvement with the ProgNova contest.

-----Examples-----
Sample Input 1:
TCGTTC
Sample Output 1:
21

Sample Input 2:
CCC
Sample Output 2:
9
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
cards = input()
tablets = cards.count('T')
compasses = cards.count('C')
gears = cards.count('G')

points = (tablets ** 2) + (compasses ** 2) + (gears ** 2)
points += 7 * min(tablets, compasses, gears)

print(points)
#@!CODE END!@#
````

---

