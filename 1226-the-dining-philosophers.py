'''
Leetcode problem 1226. The Dining Philosophers
https://leetcode.com/problems/the-dining-philosophers/description/
Difficulty: Medium

Five silent philosophers sit at a round table with bowls of spaghetti. Forks are
placed between each pair of adjacent philosophers.

Each philosopher must alternately think and eat. However, a philosopher can only
eat spaghetti when they have both left and right forks. Each fork can be held by
only one philosopher and so a philosopher can use the fork only if it is not
being used by another philosopher. After an individual philosopher finishes
eating, they need to put down both forks so that the forks become available to
others. A philosopher can take the fork on their right or the one on their left
as they become available, but cannot start eating before getting both forks.

Eating is not limited by the remaining amounts of spaghetti or stomach space; an
infinite supply and an infinite demand are assumed.

Design a discipline of behavior (a concurrent algorithm) such that no
philosopher will starve; i.e., each can forever continue to alternate between
eating and thinking, assuming that no philosopher can know when others may want
to eat or think.

The problem statement and the image above are taken from wikipedia.org



The philosophers' ids are numbered from 0 to 4 in a clockwise order. Implement
the function void wantsToEat(philosopher, pickLeftFork, pickRightFork, eat,
putLeftFork, putRightFork) where:

- `philosopher` is the id of the philosopher who wants to eat.
- `pickLeftFork` and pickRightFork are functions you can call to pick the
corresponding forks of that philosopher.
- `eat` is a function you can call to let the philosopher eat once he has picked
both forks.
- `putLeftFork` and `putRightFork` are functions you can call to put down the
corresponding forks of that philosopher.
- The philosophers are assumed to be thinking as long as they are not asking to
eat (the function is not being called with their number).

Five threads, each representing a philosopher, will simultaneously use one
object of your class to simulate the process. The function may be called for the
same philosopher more than once, even before the last call ends.


Example 1:

Input: n = 1
Output:
[[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,2],[3,2,1],[3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]
Explanation:
n is the number of times each philosopher will call the function.
The output array describes the calls you made to the functions controlling the
forks and the eat function, its format is:
output[i] = [a, b, c] (three integers)
- a is the id of a philosopher.
- b specifies the fork: {1 : left, 2 : right}.
- c specifies the operation: {1 : pick, 2 : put, 3 : eat}.


Constraints:

1 <= n <= 60

'''

# An attempt to solve without mutexes, just timing

"""
Approach:
Every cycle of pick left/right, eat, put left/right is one round.
In each round, there are the five steps (pick/pick/eat/put/put).
Two philosphers can eat at a time, and so each philosopher needs to 
think for two rounds in between each round eating.
As two philosphers can eat at a time, on the second step of putting
right, declare the round over and begin a new round.
For round r, on all rounds % 5 == 0, philosopher 0 and 0 + 2 (2) go 
through the steps for eating. On rounds % 5 = 1, philosphers 1 & 1+2
(3) go through the eating steps, and generically, on round r where
round r == [0,4], philosopher r and (r + 2) % N go through the steps
of eating.

"""

import threading


class DiningPhilosophers:
    def __init__(self):
        self.lock = threading.Lock()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        with self.lock:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
            
# Below was an attempt to solve without mutexes, just timing.
# I think this works but doesn't fit what the description is calling for
# which is that, for n=1, the test code will call wantsToEat(p) once for
# each philosphere, not once for each step

"""
Approach:
Every cycle of pick left/right, eat, put left/right is one round.
In each round, there are the five steps (pick/pick/eat/put/put).
Two philosphers can eat at a time, and so each philosopher needs to 
think for two rounds in between each round eating.
As two philosphers can eat at a time, on the second step of putting
right, declare the round over and begin a new round.
For round r, on all rounds % 5 == 0, philosopher 0 and 0 + 2 (2) go 
through the steps for eating. On rounds % 5 = 1, philosphers 1 & 1+2
(3) go through the eating steps, and generically, on round r where
round r == [0,4], philosopher r and (r + 2) % N go through the steps
of eating.

"""
class DiningPhilosophersNoMutex:
    def __init__(self):
        self.round = 0
        self.step = 0
        self.alt = 0

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        print(f"{philosopher}: round {self.round}, step {self.step}|{self.alt}")
        phil_to_eat = self.round
        alt_to_eat = (phil_to_eat + 2) % 5
        if philosopher not in [phil_to_eat, alt_to_eat]:
            return # time for thinking
        def think():
            pass
        steps = {
            0: pickLeftFork,
            1: pickRightFork,
            2: eat,
            3: putLeftFork,
            4: putRightFork,
        }
        if philosopher == phil_to_eat:
            steps.get(self.step, think)()
            self.step += 1
        else:
            steps.get(self.alt, think)()
            self.alt += 1
        if self.step >= 4 and self.alt >= 4: # Might need mutex here
            self.step, self.alt, self.round = 0, 0, (self.round + 1) % 5

        
tests = [
    [[1],[[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,2],[3,2,1],[3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]]
]
