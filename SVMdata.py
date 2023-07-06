import pandas as pd
import os

import pandas as pd
import os

os.chdir("/home/panda/Documents/Honours Thesis/Dataset")

GOdf = pd.read_csv('CleanedBGO.csv',keep_default_na=False)

Seqdf = pd.read_csv('CleanedSequence.csv',keep_default_na=False)

df=pd.concat([Seqdf, GOdf], axis=1)
df.columns = range(df.columns.size)

# Assuming df is your DataFrame
new_df = df[df.eq('GO:0006357').any(axis=1)].copy()
new_df1=f=df[df.eq('GO:0000122').any(axis=1)].copy()
new_df2=f=df[df.eq('GO:0002250').any(axis=1)].copy()
new_df3=f=df[df.eq('GO:0006355').any(axis=1)].copy()
new_df4=f=df[df.eq('GO:0016567').any(axis=1)].copy()



svmdf=pd.concat([new_df, new_df1], axis=0)
svmdf=pd.concat([svmdf, new_df2], axis=0)
svmdf=pd.concat([svmdf, new_df3], axis=0)
svmdf=pd.concat([svmdf, new_df4], axis=0)
import pandas as pd
# Remove the first two columns by column indices
GOdff = svmdf.drop(svmdf.columns[:4], axis=1)

#print(GOdff)
# Assuming 'df' is your DataFrame and 'my_list' is the list of elements
my_list = ['GO:0006355', 'GO:0002250', 'GO:0000122', 'GO:0006357', 'GO:0016567', ]
dff = GOdff[GOdff.isin(my_list)]

dff['Labels'] = dff[dff.columns[1:]].apply(lambda x: ','.join(x.dropna().astype(str)),
    axis=1)

df=pd.concat( [dff['Labels'], svmdf[2]], axis=1)

df= df[~df['Labels'].str.contains(',')]

df = df[df['Labels'].ne('')]

print(df.head(20))
#print(svmdf)
df.to_csv("SVMdata1.csv")