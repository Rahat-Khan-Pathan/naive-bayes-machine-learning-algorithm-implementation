import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# weather dataset 

def read_data():
    df = pd.read_csv("data.csv", index_col=0)
    d = df.to_dict("split")
    d = dict(zip(d["index"], d["data"]))
    return d
class NaiveBayes:
    def __init__(self,x,y,df) -> None:
        self.df=df
        self.x=x
        self.y=y
        self.allFeatures=list(x.columns)
        self.dct={}
        self.total=len(self.df["Play"])
        self.totalYes=0
        self.totalNo=0
    @staticmethod
    def pre_processing(df):
        x = df.drop(df.columns[-1],axis=1)
        y = df[df.columns[-1]]
        return x, y
    
    def train_model(self):
        for item in self.df["Play"]:
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
                    if self.df[feature][indx]==uniqueItem and self.df["Play"][indx]=="yes":
                        yes+=1
                    elif self.df[feature][indx]==uniqueItem:
                        no+=1
                self.dct[uniqueItem]={"yes":yes,"no":no,"total":yes+no}
    
    def test_model(self,testList):
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
naive=NaiveBayes(x,y,df)
naive.train_model()
sumYes,sumNo=naive.test_model(['Rainy','Mild', 'Normal', 'y'])
print(sumYes,sumNo)
if sumYes > sumNo:
    print("yes")
else:
    print("no")

            

