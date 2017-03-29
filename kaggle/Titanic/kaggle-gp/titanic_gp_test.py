# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:52:23 2017

LB:0.755
@author: weizihan
"""

# Import required libraries
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np

def MungeData(data):
    # Sex
    data.drop(['Ticket', 'Name'], inplace=True, axis=1)
    data.Sex.fillna('0', inplace=True)
    data.loc[data.Sex != 'male', 'Sex'] = 0
    data.loc[data.Sex == 'male', 'Sex'] = 1
    # Cabin
    data.Cabin.fillna('0', inplace=True)
    data.loc[data.Cabin.str[0] == 'A', 'Cabin'] = 1
    data.loc[data.Cabin.str[0] == 'B', 'Cabin'] = 2
    data.loc[data.Cabin.str[0] == 'C', 'Cabin'] = 3
    data.loc[data.Cabin.str[0] == 'D', 'Cabin'] = 4
    data.loc[data.Cabin.str[0] == 'E', 'Cabin'] = 5
    data.loc[data.Cabin.str[0] == 'F', 'Cabin'] = 6
    data.loc[data.Cabin.str[0] == 'G', 'Cabin'] = 7
    data.loc[data.Cabin.str[0] == 'T', 'Cabin'] = 8
    # Embarked
    data.loc[data.Embarked == 'C', 'Embarked'] = 1
    data.loc[data.Embarked == 'Q', 'Embarked'] = 2
    data.loc[data.Embarked == 'S', 'Embarked'] = 3
    data.Embarked.fillna(0, inplace=True)
    data.fillna(-1, inplace=True)
    return data.astype(float)

# Load the data
titanic = MungeData(pd.read_csv('train.csv'))

titanic.rename(columns={'Survived': 'class'}, inplace=True)
#titanic['Sex'] = titanic['Sex'].map({'male':0,'female':1})
#titanic['Embarked'] = titanic['Embarked'].map({'S':0,'C':1,'Q':2})
#titanic = titanic.fillna(-999)

#from sklearn.preprocessing import MultiLabelBinarizer
#mlb = MultiLabelBinarizer()
#CabinTrans = mlb.fit_transform([{str(val)} for val in titanic['Cabin'].values])

#titanic_new = titanic.drop(['Name','Ticket','Cabin','class'], axis=1)
#titanic_new = np.hstack((titanic_new.values,CabinTrans))
titanic_new=titanic.drop(['class'],axis=1).values
titanic_class = titanic['class'].values
training_indices, validation_indices = training_indices, testing_indices = train_test_split(titanic.index, stratify = titanic_class, train_size=0.75, test_size=0.25)
tpot = TPOTClassifier(verbosity=2, max_time_mins=10)
tpot.fit(titanic_new[training_indices], titanic_class[training_indices])

print tpot.score(titanic_new[validation_indices], titanic.loc[validation_indices, 'class'].values)

# Read in the submission dataset
titanic_sub = MungeData(pd.read_csv('test.csv'))
'''for var in ['Cabin']: #,'Name','Ticket']:
    new = list(set(titanic_sub[var]) - set(titanic[var]))
    titanic_sub.ix[titanic_sub[var].isin(new), var] = -999'''
    
#titanic_sub['Sex'] = titanic_sub['Sex'].map({'male':0,'female':1})
#titanic_sub['Embarked'] = titanic_sub['Embarked'].map({'S':0,'C':1,'Q':2})
#titanic_sub = titanic_sub.fillna(-999)
#from sklearn.preprocessing import MultiLabelBinarizer
#mlb = MultiLabelBinarizer()
#SubCabinTrans = mlb.fit([{str(val)} for val in titanic['Cabin'].values]).transform([{str(val)} for val in titanic_sub['Cabin'].values])
#titanic_sub = titanic_sub.drop(['Name','Ticket','Cabin'], axis=1)
# Form the new submission data set
#titanic_sub_new = np.hstack((titanic_sub.values,SubCabinTrans))
titanic_sub_new =titanic_sub.values

# Generate the predictions
submission = tpot.predict(titanic_sub_new)

# Create the submission file
final = pd.DataFrame({'PassengerId': titanic_sub['PassengerId'].astype(int), 'Survived': submission.astype(int)})
final.to_csv('submission_test1.csv', index = False)