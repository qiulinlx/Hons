import pandas as pd
import os
import numpy as np
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

# Import required packages
import gensim

from gensim.models import Word2Vec, KeyedVectors
import pandas as pd 

os.chdir("/home/panda/Documents/Honours Thesis/Dataset")

df=pd.read_csv('BGFunction.csv')
df['Function'] = df['Function'].str.replace('of', '')
df['Function'] = df['Function'].str.replace('to', '')
df['Function'] = df['Function'].str.replace('across', '')
df['Function'] = df['Function'].str.replace('in', '')
df['Function'] = df['Function'].str.replace('by', '')
df['Function'] = df['Function'].str.replace('P:', '')

data=df['Function']

new=data.apply(gensim.utils.simple_preprocess)
#print(new)

# Model parameters
model=gensim.models.Word2Vec(window=5, min_count=2, workers=4, sg=0)

model.build_vocab(new, progress_per=1000)
model.train(new, total_examples=model.corpus_count, epochs=model.epochs)

for i in range(len(new)):
    print(new[i])
    #print(model.wv[new[i]])