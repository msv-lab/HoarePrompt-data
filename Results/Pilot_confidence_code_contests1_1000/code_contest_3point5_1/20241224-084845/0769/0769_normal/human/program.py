class Dice(object):
    """Dice Class

    """

    def __init__(self, numbers):
        """

        Args:
            numbers:
        """
        self.numbers_inverse = {numbers[0]: 1, numbers[1]: 2, numbers[2]: 3, numbers[3]: 4, numbers[4]: 5,
                                numbers[5]: 6}
        self.numbers = {1: numbers[0], 2: numbers[1], 3: numbers[2], 4: numbers[3], 5: numbers[4], 6: numbers[5]}

        self.vertical = [self.numbers[1], self.numbers[2], self.numbers[6], self.numbers[5]]
        self.horizontal = [self.numbers[4], self.numbers[1], self.numbers[3], self.numbers[6]]

    def roll_dice(self, str):
        """

        Args:
            str: move direction

        Returns:

        """
        for s in str:
            if s == 'N':
                self.move_north()
            elif s == 'S':
                self.move_south()
            elif s == 'W':
                self.move_west()
            elif s == 'E':
                self.move_east()

    def set_top(self, value):
        """
        Args:
            value: target_value
        """
        counter = 0
        while counter < 4:
            if self.vertical[0] == value:
                self.map_values()
                return
            else:
                self.roll_dice("S")
            counter += 1
        counter = 0
        while counter < 4:
            if self.vertical[0] == value:
                self.map_values()
                return
            else:
                self.roll_dice("W")
            counter += 1

    def set_front(self, value):
        """
        Args:
            value: target value
        """
        counter = 0
        while counter < 4:
            if self.vertical[1] == value:
                self.map_values()
                return
            else:
                self.roll_dice("SWN")
            counter += 1

    def move_south(self):
        """move this dice towered north
        """
        self.vertical = (self.vertical * 2)[3:7]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
        self.map_values()

    def move_north(self):
        """move this dice towered south
        """
        self.vertical = (self.vertical * 2)[1:5]
        self.horizontal[1] = self.vertical[0]
        self.horizontal[3] = self.vertical[2]
        self.map_values()

    def move_east(self):
        """move this dice towered east
        """
        self.horizontal = (self.horizontal * 2)[3:7]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
        self.map_values()

    def move_west(self):
        """move this dice towered west
        """
        self.horizontal = (self.horizontal * 2)[1:5]
        self.vertical[0] = self.horizontal[1]
        self.vertical[2] = self.horizontal[3]
        self.map_values()

    def map_values(self):
        self.numbers[1] = self.vertical[0]
        self.numbers[2] = self.vertical[1]
        self.numbers[3] = self.horizontal[2]
        self.numbers[4] = self.horizontal[0]
        self.numbers[5] = self.vertical[3]
        self.numbers[6] = self.vertical[2]

    def get_top(self):
        return self.vertical[0]


def is_same(dice1, dice2):
    """compare two dices

    Args:
        dice1: dice1
        dice2: dice2

    Returns:
        Bool (whether dice1 is equals to be dice2 or not)
    """
    flag = False
    if dice1.numbers == dice2.numbers:
        flag = True
    else:
        for i in range(6):
            dice1.set_top(i + 1)
            for j in xrange(4):
                dice1.roll_dice("SWN")
                if dice1.numbers == dice2.numbers:
                    flag = True
            dice1.roll_dice("S")

    return flag


dice_number = int(raw_input())
dices = []
counter = 0
while counter < dice_number:
    dices.append(Dice([int(x) for x in raw_input().split()]))
    counter += 1

ans = 0
for i in range(dice_number - 1):
    if ans > 0:
        break
    for j in range(i + 1, dice_number):
        ans += int(is_same(dices[i], dices[j]))
        if ans > 0:
            print("No")
            break

if ans == 0:
    print("Yes")