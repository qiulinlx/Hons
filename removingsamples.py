
import pandas as pd
import os

os.chdir("/home/panda/Documents/Honours Thesis/Dataset")

GOdf = pd.read_csv('BGO.csv',keep_default_na=False)

GOdf.drop(columns=GOdf.columns[0], axis=1, inplace=True)

Seqdf = pd.read_csv('Sequence.csv',keep_default_na=False)


df=pd.concat([Seqdf, GOdf], axis=1)
df.columns = range(df.columns.size)

# Assuming df is your DataFrame and 'Column' is the column name
df = df[df[2] != '']


GOdf=df.iloc[:,2:]
#print(GOdf)
#GOdf.to_csv("CleanedBGO.csv")

Seqdf=df.iloc[:,:2]
print(Seqdf)
Seqdf.to_csv("CleanedSequence.csv")