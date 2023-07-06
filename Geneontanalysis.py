import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
os.chdir("/home/panda/Documents/Honours Thesis/Dataset")

""" GOdf = pd.read_csv('BGO.csv',keep_default_na=False)
'''
def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

GOrows= GOdf.values.tolist()
GOunion=[]

for i in range(len(GOrows)):
    GOunion=Union(GOunion, GOrows[i])

for element in GOunion:
    if element.startswith("GO_"):
        GOunion.remove(element)

#print(len(GOunion))
Counter=[]

df=pd.DataFrame(columns=GOunion)

for i in range(len(GOdf.columns)):
    df=GOdf[i].value_counts()
    print(i)
    name=f"BGOCount{i}.csv"
    df.to_csv(name)
'''
GOdf.drop(columns=GOdf.columns[0], axis=1, inplace=True)
df1 = GOdf.apply(pd.value_counts).fillna(0)
df1 = df1.iloc[1:]
df1=df1.loc[:, (df1 != 0).any(axis=0)]

# Display the histogram
plt.show()


#df1.to_csv("BGOCount.csv")
count=df1.sum(axis='columns') 
#count.to_csv("BGOCount.csv")
count=pd.DataFrame(count)
largest_value_row = count[0].idxmax()
print(largest_value_row) """
df = pd.read_csv('BGOCount.csv',keep_default_na=False)

row = df.reset_index().transpose()


print(row.columns)
#print(df['0'])
plt.plot(df['0'])
#df.hist(column='0')
# Set the title and axis labels
plt.title('Histogram of GO labels')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()