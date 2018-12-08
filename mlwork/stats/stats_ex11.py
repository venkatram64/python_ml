from numpy import random
import matplotlib.pyplot as plt

"""
Conditioanl Probability:
If I have two events that depend on each other, what's the 
probability that both will occur?
Notation: P(A, B) is the probability of A and B both occuring 
P(B|A): Probability of B given that A has Occurred
We know:

P(B|A) P(A,B)/P(A)

Example:
I gave my students two tests. 60% of my students passed both tests, but
the first test was easier 80% passed that one.  What percentage of students 
who passed the first test also passed the second?
A = passing the first test, B = passing the second test
So we asking for P(B|A) - The probability of B given A

P(B|A) = P(A,B)/P(A) = 0.6/0.8 = 0.75

75% of students who passed the first test,
passed the second test.

"""

"""
Below is some code to create some fake data on how much stuff people purchase given their age range.
It generates 100,000 random "people" and randomly assigns them as being in their 20's, 30's, 40's, 50's, 60's, or 70's.
It then assigns a lower probability for young people to buy stuff.
In the end, we have two Python dictionaries:
"totals" contains the total number of people in each age group. "purchases" contains the total number of things purchased by people in each age group. The grand total of purchases is in totalPurchases, and we know the total number of people is 100,000.
Let's run it and have a look:
"""
def findProbability():
    random.seed(0)

    totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
    purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
    totalPurchases = 0

    for _ in range(100000):
        ageDecade = random.choice([20, 30, 40, 50, 60, 70])
        purchaseProbability = float(ageDecade) / 100.0
        totals[ageDecade] += 1
        if(random.random() < purchaseProbability):
            totalPurchases += 1
            purchases[ageDecade] += 1

    print(totals)
    print(purchases)
    print(totalPurchases)
    """
    Let's play with conditional probability.
    First let's compute P(E|F), where E is "purchase" and F is "you're in your 30's". 
    The probability of someone in their 30's buying something is just the percentage 
    of how many 30-year-olds bought something:
    """
    PEF = float(purchases[30]) /float(totals[30])
    print('P(purchase | 30s): ' + str(PEF))
    #P(F) is just the probability of being 30 in this data set

    PF = float(totals[30]) / 100000.0
    print("P(30's): " + str(PF))

    #Add P(E) is the overall probability of buying something, regardless of your age
    PE = float(totalPurchases) / 100000.0
    print("P(purchase) :" + str(PE))

    """
    If E and F were independent, then we would expect P(E | F) to be about the same as P(E). 
    But they're not; PE is 0.45, and P(E|F) is 0.3. So, that tells us that E and F are dependent 
    (which we know they are in this example.)
    What is P(E)P(F)?
    """
    print("P(30's)P(Purchase) " + str(PE * PF))

    """
    P(E,F) is different from P(E|F). P(E,F) would be the probability of both being in your 30's and buying something, 
    out of the total population - not just the population of people in their 30's:
    """

    print("P(30's, Purchase) " + str(float(purchases[30]) / 100000.0))

    """
    P(E,F) = P(E)P(F), and they are pretty close in this example. But because E and F are 
    actually dependent on each other, and the randomness of the data we're working with, 
    it's not quite the same.
    We can also check that P(E|F) = P(E,F)/P(F) and sure enough, it is:
    """
    print((purchases[30]/100000.0) / PF)


if __name__ == '__main__':
    findProbability()

