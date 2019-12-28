import pygame
import random
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

parNum = 1

#week1 = [1,1,1]
#text = ["c1","c1","c1"]
#
#response = ["Yo","hi","this is a sentence"]
#
#week1 = list(zip(week1,text,response))
#print (week1)
#
#df = pd.DataFrame(data = week1, columns=['week','Text', 'Response'])
#df.to_csv('addingTest.csv', encoding='utf-8')

currParData = pd.read_csv('addingTest.csv')

#week2 = [2]
#newText = ["c1"]
#newResponse = ["add"]
#
#week2 = list(zip(week2,newText,newResponse))
#print(week2)
#
#newDf = pd.DataFrame(data = week2, columns=['week','Text', 'Response'])
#
#print(newDf)
#
#temp = [currParData,newDf]
#
#result = pd.concat(temp,sort=True)
#
#print (result)

week2 = [3]
newText = ["c1"]
newResponse = ["YOYOYO"]

week3 = list(zip(week2,newText,newResponse))
print(week3)

newDf = pd.DataFrame(data = week3, columns=['week','Text', 'Response'])

print(newDf)

temp = [currParData,newDf]

result = pd.concat(temp,sort=True)
print(result)