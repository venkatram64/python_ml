from numpy import random
import matplotlib.pyplot as plt

"""
Bayes' Theorem:
No that you understand conditional probability, you can understand Bayes' Theorem:

P(A|B) = P(A)P(B|A)/P(B)
In English - The probability of A given B, is the Probability of A times the probability of B given
A over the probability of B.

The key insight is that the probability of something that depends on B depends
very much on the base probability of B and A.  People ignore this all the time.

"""

"""
Bayes' Theorem to the rescue:
Event A = Is a user of the drug, Event B= tested positively for the drug.
We can work out from that information that P(B) is 1.3%(0.99 * 0.003 +
0.01 * 0.997 - the probability of testing positive if you do use, plus the 
probability of testing positive if you don't)
P(A|B) = P(A)P(B|A)/P(B) = 0.003 * 0.99/0.013 = 22.8%
So the odds of someone being an actual user of the drug given that they
tested positive is only 22.8%
Even though P(B|A) is high(99%), it doesn't mean P(A|B) is high
"""


