import random

class Game:
    def __init__(self, range1):
        self.range1 = range1
        self.number = random.randint(1, range1)
        self.cluebank = []
        self.cluebank = self.divisibile() + self.smaller_than() + self.bigger_than()
        self.points = 10

    def play(self):
        guess = int(input())
        if guess == self.number:
            print("You Win!! points are {}".format(self.points))
        else:
            self.points -=1
            print("another clue is")
            if self.cluebank:
                clue = random.randint(0, len(self.cluebank)-1)
                print(self.cluebank[clue])
                self.cluebank.remove(self.cluebank[clue])
                self.play()
            elif not self.cluebank:
                print("Game Over no more clues")


    def divisibile(self):
        divlist = []
        for i in range(2, self.range1):
            if (self.number % i == 0) and (i != self.number):
                clue = "number is divisible by {}".format(i)
                divlist.append(clue)
        return divlist

    def bigger_than(self):
        biggerlist = []
        for i in range(1, self.number):
            clue = "number is bigger than {}".format(i)
            biggerlist.append(clue)
        return biggerlist

    def smaller_than(self):
        smallerlist = []
        for i in range(self.number+1, self.range1+1):
            clue = "number is smalller than {}".format(i)
            smallerlist.append(clue)
        return smallerlist




if __name__ == "__main__":
    c = Game(10)
    c.play()


