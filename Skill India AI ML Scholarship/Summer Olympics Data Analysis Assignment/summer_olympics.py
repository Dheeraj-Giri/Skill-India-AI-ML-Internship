import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('summer.csv')

print(len(df['City'].unique()))



item=[]
for sports in df['Sport'].unique():
    item.append([sports,len(df[df['Sport']==sports])])
pd.DataFrame(item,columns=['Sport','Medal']).sort_values(by='Medal',ascending=False)
print(item)


item=[]
for Sport in df["Sport"].unique():
    item.append([Sport , len(df[df["Sport"] == Sport])])
pd.DataFrame(item,columns = ['Sport','Medal']).sort_values(by='Medal', ascending=False).head().plot(x = 'Sport', y = 'Medal', kind = 'bar', figsize = (5,5))
print(item)
