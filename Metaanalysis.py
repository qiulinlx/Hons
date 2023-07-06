#Meta-data anaylsis
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir("/home/panda/Documents/Honours Thesis/Dataset")

#Read in the data
df = pd.read_csv("dataset.csv")
meta=df[['Annotation']]
for i in range(10):#len(meta)):
    m=meta.iloc[i,0]
    mm=m.split()
    print(mm)

import pandas as pd

GOdf = pd.read_csv('GO.csv',keep_default_na=False)
#Seqdf= pd.read_csv('Sequence.csv')

# Convert each row into a list
GOrows= GOdf.values.tolist()
GOunion=set()
for i in range (len(GOrows)):
    filtered_list = [x for x in GOrows[i] if x != '']
    GOn=set(filtered_list)
    GOunion=GOunion.union(GOn)
