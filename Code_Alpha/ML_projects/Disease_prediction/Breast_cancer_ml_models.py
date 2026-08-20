# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 13:30:05 2025

@author: komme
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import xgboost as Xgb
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
import lightgbm as lgbm



dataset = pd.read_csv(r'D:\GenAi\ML\BrestCancer\Breast_cancer_dataset.csv')

#split the data into x and y
x= dataset.drop(['id','diagnosis'],axis=1)
y = dataset['diagnosis']

#label encoder beacuse dependent variables are in category and it is classification model
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
y = lb.fit_transform(y)

#train and test the data

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=20,random_state=0)


# scaling the data
sc = StandardScaler()
x_train= sc.fit_transform(x_train)
x_test= sc.transform(x_test)


#model selection
models = {'LogisticRegression': LogisticRegression(),
          'SVC':SVC(),
          'RandomForestClassifier':RandomForestClassifier(),
          'xgboost':Xgb.XGBRegressor(),
          'KNeighboursClassifier': KNeighborsClassifier(),
          'GaussianNB': GaussianNB(),
          'BernoulliNB': BernoulliNB(),
          'lgboost': lgbm.LGBMClassifier()
          }

result=[]
for name,model in models.items():
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    
    mae= mean_absolute_error(y_test, y_pred)
    mse= mean_squared_error(y_test,y_pred)
    r2 = r2_score(y_test, y_pred)
    
    bias = model.score(x_train,y_train)
    print('model name:',name,'bias:',bias)

    variance = model.score(x_test,y_test)
    print('model name:',name,'variance:',variance)
    
    '''ac_score= accuracy_score(y_test,y_pred)
    print('Model Name:',name,'Accuracy_score:',ac_score)'''
    
    ''' cr_val= cross_val_score(model,x,y)
    print('Model name:',name,'Cross_validation_score:',cr_val)'''


    result.append({'Model': name,
                   'MAE': mae,
                   'MSE': mse,
                   'R2': r2,
                   'Bias':bias,
                   'Variance':variance,
                   #'Accuracy_score': ac_score,
                  # 'Cross_validation_score':cr_val
                   })
    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(model, f)
    

    
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test,y_pred)
print(ac)

from sklearn.metrics import classification_report
cr = classification_report(y_test,y_pred)
print(cr)

# finding the result of the model predicted whether no of patients have malignant cancer or bengin cancer
results = x_test.reshape(1,-1)
results = model.predict_proba(x_test)[0]

print(results)
if results[0] > results[1]:
    print("bengin cancer")
else:
    print('malignant cancer')
## malignant cancer patients are more than bengin cancer patients.



# Convert results to DataFrame and save to CSV
result_df = pd.DataFrame(result)
result_df.to_csv('model_evaluation_results.csv', index=False)

print("Models have been trained and saved as pickle files. Evaluation results have been saved to model_evaluation_results.csv.")


### from all the models LogisticRegressor,SVC is the best models 






