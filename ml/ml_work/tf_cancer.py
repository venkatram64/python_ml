import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

#activate chat_bot  then run the code at command prompt

masses_data = pd.read_csv('mammographic_masses.data.txt')
print(masses_data.head())

names = ['BI-RADS', 'age', 'shape', 'margin', 'density', 'severity']

masses_data = pd.read_csv('mammographic_masses.data.txt', na_values=['?'], names=names)
print(masses_data.head())

#Evaluate whether the data needs cleaning; your model is only as good as the data it's given

print(masses_data.describe())

masses_data.loc[(masses_data['age'].isnull()) |
                  (masses_data['shape'].isnull()) |
                  (masses_data['margin'].isnull()) |
                  (masses_data['density'].isnull())]

masses_data.dropna(inplace=True)
print(masses_data.describe())

all_features = masses_data[['age', 'shape', 'margin', 'density']].values

all_classes = masses_data['severity'].values

feature_names = ['age', 'shape', 'margin', 'density']

print(all_features)

scalar = preprocessing.StandardScaler()
all_features_scaled = scalar.fit_transform(all_features)

print(all_features_scaled)

def create_model():
    model = Sequential()
    # 4 feature inputs going into an 6-unit layer (more does not seem to help - in fact you can go down to 4)
    model.add(Dense(6, input_dim=4, kernel_initializer='normal', activation='relu'))
    # "Deep learning" turns out to be unnecessary - this additional hidden layer doesn't help either.
    # model.add(Dense(4, kernel_initializer='normal', activation='relu'))
    # Output layer with a binary classification (benign or malignant)
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    # Compile model; adam seemed to work bes
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

estimator = KerasClassifier(build_fn=create_model, epochs=100, verbose=0)
cv_scores = cross_val_score(estimator, all_features_scaled, all_classes, cv=10)
print(cv_scores.mean())