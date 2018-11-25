import numpy as np
import pandas as pd
import missingno as msno
import seaborn as sn
import matplotlib.pyplot as plt

features = ['card1 suit', 'card1 rank', 'card2 suit', 'card2 rank', 'card3 suit', 'card3 rank', 'card4 suit',\
            'card4 rank','card5 suit', 'card5 rank','poker hand']

train_data = pd.read_csv("poker_hand_train.csv", names=features)
test_data = pd.read_csv("poker_hand_train.csv", names=features)



pokerHnadMap = {\
    0: "Nothing in hand",\
    1: "One pair",\
    2: "Two pairs",\
    3: "Three pairs",\
    4: "Straight",\
    5: "Flush",\
    6: "Full house",\
    7: "Four of a kind",\
    8: "Straight flush",\
    9: "Royal flush"
}

suitMap = {1: "Hearts", 2: "Spades", 3: "Diamonds", 4: "Clubs"}


data = pd.concat([train_data, test_data])

print(data)

categoryVarLabelList = ['card1 suit', 'card1 rank', 'card2 suit', 'card2 rank', 'card3 suit', 'card3 rank',
                        'card4 suit', 'card4 rank', 'card5 suit', 'card5 rank']

for var in categoryVarLabelList:
    data[var] = data[var].astype('float64')

prettyData = data
prettyData['card1 suit'] = data['card1 suit'].map(suitMap)
prettyData['card2 suit'] = data['card2 suit'].map(suitMap)
prettyData['card3 suit'] = data['card3 suit'].map(suitMap)
prettyData['card4 suit'] = data['card4 suit'].map(suitMap)
prettyData['card5 suit'] = data['card5 suit'].map(suitMap)
prettyData['poker hand'] = data['poker hand'].map(pokerHnadMap)

print(prettyData)


# Correlation analasys
corrMatt = data.corr()
mask = np.array(corrMatt)
mask[np.tril_indices_from(mask)] = False
fig,ax= plt.subplots()
fig.set_size_inches(20,10)
sn.heatmap(corrMatt, mask=mask,vmax=.8, square=True,annot=True)
