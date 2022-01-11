"""
Suppose there is a hat containing 5 blue balls, 4 red balls, and
2 green balls. What is the probability that a random draw of 4 balls
will contain at least 1 red ball and 2 green balls? While it would be
possible to calculate the probability using advanced mathematics, an
easier way is to use this program to perform a large number of
experiments to estimate an approximate probability.

The 'Hat' class takes a variable number of arguments that specify the
number of balls of each color that are in the hat.

You can use the 'experiment' function to check the probability.
"""


import random


class Hat:
    contents: list[str]
    
    def __init__(self, **balls: int):
        self.contents = []
        
        for k, v in balls.items():
            while v > 0:
                self.contents.append(k)
                v -= 1
                
    def drawn(self, quantity: int) -> list[str]:
        h = self.contents.copy()
        
        if quantity >= len(self.contents):
            return h
        else:
            balls_removed = []

            while quantity > 0:
                i = h.pop(random.randrange(len(h)))
                balls_removed.append(i)
                quantity -= 1

            return balls_removed


def experiment(hat: object, expected_balls: dict,
               num_balls_drawn: int, num_experiments: int) -> float:
    count = 0
    controller = num_experiments
    
    while controller > 0:
        d = hat.drawn(num_balls_drawn)
        check = 0
        
        for k, v in expected_balls.items():
            c = d.count(k)
            
            if c >= v:
                check += 1
            else:
                break

        if check == len(expected_balls):
            count += 1
        
        controller -= 1
    
    return round(count / num_experiments, 3)
