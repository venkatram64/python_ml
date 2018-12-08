import os
import io
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


"""
P(A|B) = P(A)P(B|A)/P(B)
Let's use it for machine learning I want a spam classifier.
Example: how would we expres the probability of an email being spam if it contains
the word "free"

P(Spam|Free) = P(Spam)P(Free|Spam)/P(Free)
The numerator is the probability of a message being spam and containing the
word "free" (this subtly different from what we are looking for)
The denominator is the overall probability of an email containing the word
"free". (Equivalent to P(Free|Spam)P(Spam) + P(Free|Not Spam)P(Not Spam))
So together- this ratiois the % of emails with the word "free" that are spam.
"""

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return pd.DataFrame(rows, index=index)

data = pd.DataFrame({'message': [], 'class':[]})

data = data.append(dataFrameFromDirectory('D:\\python3_spark\\DataScience\\DataScience-Python3\\emails\\spam', 'spam'))
data = data.append(dataFrameFromDirectory('D:\\python3_spark\DataScience\\DataScience-Python3\\emails\\ham', 'ham'))

print(data.head())

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

#let's try it out

examples = {'Free Viagra', "Hi Sachin, how are you"}
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print(predictions)