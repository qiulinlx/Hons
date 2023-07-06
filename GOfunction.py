import pandas as pd
import json
import os
os.chdir("/home/panda/Documents/Honours Thesis/Dataset")

'''
GeneOntology=[]
Function=[]
# Specify the path to the JSON file
json_file_path = 'HumanSwiss.json'

#Read the JSON file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)
    
#Extract the desired value from the JSON data
for j in range(20422):
    value = json_data['results'][j]['sequence']['value']
    GOannotations = json_data['results'][j]['uniProtKBCrossReferences']
    #Sequence['Sequence_'+str(j)]=value

    for i in range(len(GOannotations)):
        if GOannotations[i]['database'] == 'GO':
            if GOannotations[i]['properties'][0]['value'].startswith('P:'):
                func=GOannotations[i]['properties'][0]['value']
                Gid=(GOannotations[i]['id'])
                GeneOntology.append(Gid)
                Function.append(func)
                #print(func)

    
Genedf=pd.DataFrame(list(zip(GeneOntology,Function)), columns=["GO","Function"])
Genedf.to_csv('BGFunction.csv')'''

df=pd.read_csv('BGFunction.csv')
df.drop_duplicates(subset ="GO", keep = False, inplace = True)
df.to_csv('BGFunction.csv')