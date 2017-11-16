import random

class Dice(object):
    def __init__(self):
        pass

    def roll(self):
        d1 = random.choice(range(1, 7))
        d2 = random.choice(range(1, 7))
        d3 = random.choice(['yellow', 'blue', 'green', 'barbarian', 'barbarian', 'barbarian'])
        print 'white: ', d1
        print 'red: ', d2
        print 'special: ', d3
        print '================'
        print 'total',  d1 + d2
dice = Dice()
dice.roll()
