# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 21:40:10 2016

@author: weizihan
"""

import pandas as pd
import numpy as np

data_fields = ['user id','item id', 'rating', 'timestamp']
user_fields = ['user id', 'age', 'gender', 'occupation', 'zip code']

#默认names = None，此时pd.read_table会拿第1行的value当作列名
data_df = pd.read_table(r"F:\python2_pr\ml-100k\u.data", names = data_fields)
#默认sep = '\t'，拿tab作为分列符
user_df = pd.read_table(r"F:\python2_pr\ml-100k\u.user", sep = "|", names = user_fields)
#生成2个新的DataFrame,去掉不需要的列
data1_df = pd.DataFrame([])
data1_df['user id'] = data_df['user id']
data1_df['rating'] = data_df['rating']
user1_df = pd.DataFrame([])
user1_df['user id'] = user_df['user id']
user1_df['gender'] = user_df['gender']
#合并2个DataFrame, 默认how = 'inner'，即新的DF仅包含2个DF交集的Key
rating_df = pd.merge(data1_df, user1_df)
#按性别生成数据透视表, 默认aggfunc = 'mean', 即values是每个用户为N个电影打分的平均值
###注意：pivot_table的类型不是DataFrame, 而是Series, 所以要进行转换
gender_s = pd.pivot_table(rating_df, index = ['gender', 'user id'], 
                          values = 'rating')
gender_df = pd.DataFrame(gender_s)
#对DataFrame进行筛选，分别生成女性和男性的DataFrame
Female_df = gender_df.query("gender == ['F']")
Male_df = gender_df.query("gender == ['M']")
#按性别计算评分标准差
Female_std = np.std(Female_df)
Male_std = np.std(Male_df)
#格式化输出
print 'Gender\n', 'F\t%.6f' % Female_std, '\nM\t%.6f' % Male_std