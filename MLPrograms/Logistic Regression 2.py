#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

#Get Dataset
dataset = pd.read_csv('newHIV-1_data/746Data.csv')
data = pd.read_csv('newHIV-1_data/746Data.csv').values
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, 1].values
y = y.reshape(len(y), 1)
print(data)
print(X)
print(y)
#Given Condition
allcolumns = np.array(list('ARNDCQEGHILKMFPSTWYV'))

#Get the count of each letter from given dataset

def ConvertCategory(given_list):
    new_list =[]
    for index in given_list:
        my_list = []
        for i in allcolumns:
            index = str(index)
            my_list.append(index.count(i))
        new_list.append(my_list)
    return new_list


new_list = ConvertCategory(data)
matX=np.asarray(new_list)

#Splitting data to test and train
xtrain,xtest,ytrain,ytest=train_test_split(matX,y,test_size=0.2,random_state=0)

#Fit train data to model
classifier= LogisticRegression()
classifier.fit(xtrain,ytrain)

#Prediction
ypred=classifier.predict(xtest)

#Confusion Matrix
cm=confusion_matrix(ytest,ypred)
#ranpred=reg.predict([[3, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]])
new_list123 = ConvertCategory([['AAAMKRHG']])
pred = classifier.predict(new_list123)