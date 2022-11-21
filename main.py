import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import time

# weather dataset 

def read_data():
    print("Reading data from csv...\n")
    time.sleep(2)
    df = pd.read_csv("data.csv", index_col=0)
    d = df.to_dict("split")
    d = dict(zip(d["index"], d["data"]))
    print("Done...\n")
    return d
class NaiveBayes:
    def __init__(self,x,y,df) -> None:
        self.df=df
        self.x=x
        self.y=y
        self.allFeatures=list(x.columns)
        self.dct={}
        self.total=len(self.df[self.y.name])
        self.totalYes=0
        self.totalNo=0
    @staticmethod
    def pre_processing(df):
        print("Processing your data...\n")
        time.sleep(2)
        x = df.drop(df.columns[-1],axis=1)
        y = df[df.columns[-1]]
        print("Data processed!\n")
        return x, y
    
    def train_model(self):
        print("Training your model...\n")
        time.sleep(2)
        for item in self.df[self.y.name]:
            if item=="yes":
                self.totalYes+=1
            else:
                self.totalNo+=1
        for feature in self.allFeatures:
            uniqueItemsList = list(self.df[feature])
            for uniqueItem in np.unique(uniqueItemsList):
                yes=0
                no=0
                for indx in range(len(list(self.df[feature]))):
                    if self.df[feature][indx]==uniqueItem and self.df[self.y.name][indx]=="yes":
                        yes+=1
                    elif self.df[feature][indx]==uniqueItem:
                        no+=1
                self.dct[uniqueItem]={"yes":yes,"no":no,"total":yes+no}
        print("Model trained. You can now test!\n")
    
    def test_model(self,testList):
        print("Testing...\n")
        time.sleep(2)
        sum1Yes=(self.totalYes/self.total)
        sum2Yes=1
        for testItem in testList:
            sum1Yes*=(self.dct[testItem]['yes']/self.totalYes)
            sum2Yes*=(self.dct[testItem]['total']/self.total)
            
        sumYes = sum1Yes/sum2Yes
        sum1No=(self.totalNo/self.total)
        sum2No=1
        for testItem in testList:
            sum1No*=(self.dct[testItem]['no']/self.totalNo)
            sum2No*=(self.dct[testItem]['total']/self.total)
        sumNo = sum1No/sum2No
        return sumYes,sumNo

df = pd.DataFrame(read_data())
x,y=NaiveBayes.pre_processing(df)
# print(y.name)
naive=NaiveBayes(x,y,df)
naive.train_model()
test=[]

for uniqueCol in list(x.columns):
    columnData=list(np.unique(df[uniqueCol]))
    print(f"Choose an option from {uniqueCol}")
    for indx in range(len(columnData)):
        print(f"{indx}. {columnData[indx]}")
    x=int(input())
    if x<0 or x>=len(columnData):
        print("Error occured. Try again!")
    test.append(columnData[x])
    print("\n\n")
print(f"\nYour test data is: {test}\n")
sumYes,sumNo=naive.test_model(test)
print(f"Probability of yes: {sumYes}\nProbability of no: {sumNo}",end="\n\n")
if sumYes > sumNo:
    print(f"answer is yes, you can {y.name}")
else:
    print(f"answer is no, you can't {y.name}")

            

