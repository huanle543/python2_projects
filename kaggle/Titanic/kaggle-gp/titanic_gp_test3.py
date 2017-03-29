# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:57:34 2017

LB:0.80383  --40mins
LB:0.79426  --60mins
@author: weizihan
"""

from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import dataProcess
import numpy as np
from sklearn.grid_search import GridSearchCV
from sklearn.grid_search import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier

input_df, submit_df = dataProcess.getDataSets(bins=True, scaled=True, \
                                               binary=True)
input_df.rename(columns={'Survived': 'class'}, inplace=True)
#titanic['Sex'] = titanic['Sex'].map({'male':0,'female':1})
#titanic['Embarked'] = titanic['Embarked'].map({'S':0,'C':1,'Q':2})
#titanic = titanic.fillna(-999)

#from sklearn.preprocessing import MultiLabelBinarizer
#mlb = MultiLabelBinarizer()
#CabinTrans = mlb.fit_transform([{str(val)} for val in titanic['Cabin'].values])

#titanic_new = titanic.drop(['Name','Ticket','Cabin','class'], axis=1)
#titanic_new = np.hstack((titanic_new.values,CabinTrans))
titanic_new=input_df.drop(['class'],axis=1).values
titanic_class = input_df['class'].values
training_indices, validation_indices = training_indices, testing_indices = train_test_split(input_df.index, stratify = titanic_class, train_size=0.75, test_size=0.25)
tpot = TPOTClassifier(verbosity=2, max_time_mins=60)
tpot.fit(titanic_new[training_indices], titanic_class[training_indices])

print tpot.score(titanic_new[validation_indices], input_df.loc[validation_indices, 'class'].values)

# Read in the submission dataset
#titanic_sub = MungeData(pd.read_csv('test.csv'))
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
titanic_sub_new =submit_df.values

# Generate the predictions
submission = tpot.predict(titanic_sub_new)

# Create the submission file
final = pd.DataFrame({'PassengerId': submit_df['PassengerId'].astype(int), 'Survived': submission.astype(int)})
final.to_csv('submission_test2.csv', index = False)