# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:34:46 2017

@author: weizihan
"""

import pandas as pd
import numpy as np
from sklearn.cross_validation import KFold
titanic=pd.read_csv('train.csv')

from sklearn import svm
titanic['Age']=titanic["Age"].fillna(titanic["Age"].median())
titanic=titanic.drop(['Ticket','Cabin','PassengerId'], axis=1)
titanic.loc[titanic["Sex"] == "male", "Sex"] = 1  #将男性转为1
titanic.loc[titanic["Sex"] == "female", "Sex"] = 0 #将女性转为0
# 首先把所有缺失值替换为"S"
titanic["Embarked"] = titanic["Embarked"].fillna("S")

# 将"S"替换为0，C=1,Q=2
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

'''from patsy import dmatrices
from pandas import DataFrame

# 定义纳入训练过程的数据列
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
kf = KFold(titanic.shape[0], n_folds=5, random_state=1)
predictions = []
clf = svm.SVC(kernel='poly',gamma=3)
for train, test in kf: 
    # 提取出用作训练的数据行（不含拟合目标）
    train_predictors = (titanic[predictors].iloc[train,:])
    # 提取用于训练的拟合目标
    train_target = titanic["Survived"].iloc[train]
    # 基于训练数据和拟合目标训练模型
    clf.fit(train_predictors, train_target)
    # 接下来在测试集上执行预测
    test_predictions = clf.predict(titanic[predictors].iloc[test,:])
    predictions.append(test_predictions)'''
    
import re

# 从姓名中提取称谓的函数
def get_title(name):
    # 正则表达式检索称谓，称谓总以大写字母开头并以句点结尾
    title_search = re.search(' ([A-Za-z]+)\.', name)
    # 如果称谓存在则返回其值
    if title_search:
        return title_search.group(1)
    return ""

# 创建一个新的Series对象titles，统计各个头衔出现的频次
titles = titanic["Name"].apply(get_title)
#print(pd.value_counts(titles))

# 将每个称谓映射到一个整数，有些太少见的称谓可以压缩到一个数值
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}
for k,v in title_mapping.items():
    titles[titles == k] = v

# 验证转换结果
#print(pd.value_counts(titles))

# Add in the title column.
titanic["Title"] = titles

titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]

import operator

# 映射姓氏到家庭ID的字典
family_id_mapping = {}

# 从行信息提取家庭ID的函数
def get_family_id(row):
    # 分割逗号获取姓氏
    last_name = row["Name"].split(",")[0]
    # 创建家庭ID列表
    family_id = "{0}{1}".format(last_name, row["FamilySize"])
    # 从映射中查询ID
    if family_id not in family_id_mapping:
        if len(family_id_mapping) == 0:
            current_id = 1
        else:
            # 遇到新的家庭则将其ID设为当前最大ID+1
            current_id = (max(family_id_mapping.items(), key=operator.itemgetter(1))[1] + 1)
        family_id_mapping[family_id] = current_id
    return family_id_mapping[family_id]

# 用.apply()方法获得家庭ID
family_ids = titanic.apply(get_family_id, axis=1)

# 家庭数量过多，所以将所有人数小于3的家庭压缩成一类
family_ids[titanic["FamilySize"] < 3] = -1

# 输出每个家庭ID的数量
#print(pd.value_counts(family_ids))

titanic["FamilyId"] = family_ids
    
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
algorithms = [
    [GradientBoostingClassifier(random_state=1, n_estimators=25, max_depth=3), ["Pclass", "Sex", "Age", "Fare", "Embarked", "FamilySize", "Title", "FamilyId"]],
    [LogisticRegression(random_state=1), ["Pclass", "Sex", "Fare", "FamilySize", "Title", "Age", "Embarked"]]
]

# 初始化交叉验证
kf = KFold(titanic.shape[0], n_folds=3, random_state=1)

predictions = []
for train, test in kf:
    train_target = titanic["Survived"].iloc[train]
    full_test_predictions = []
    # 对每个交叉验证分组，分别使用两种算法进行分类
    for alg, predictors in algorithms:
        # 用训练集拟合算法
        alg.fit(titanic[predictors].iloc[train,:], train_target)
        # 选择并预测测试集上的输出 
        # .astype(float) 可以把dataframe转换为浮点数类型
        test_predictions = alg.predict_proba(titanic[predictors].iloc[test,:].astype(float))[:,1]
        full_test_predictions.append(test_predictions)
    # 对两个预测结果取平均值
    test_predictions = (full_test_predictions[0] + full_test_predictions[1]) / 2
    # 大于0.5的映射为1；小于或等于的映射为0
    test_predictions[test_predictions <= .5] = 0
    test_predictions[test_predictions > .5] = 1
    predictions.append(test_predictions)

# 将预测结果存入一个数组
predictions = np.concatenate(predictions, axis=0)

# 与训练集比较以计算精度
accuracy = float(len(predictions[predictions == titanic["Survived"]])) / float(len(predictions))

print(accuracy)