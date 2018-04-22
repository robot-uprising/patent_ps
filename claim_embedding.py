import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm
from gensim.models import doc2vec

sgid1 = ['C12M', 'C12M', 'C12P', 'C12Q', 'C12R', 'C12Y']
fields = ['uuid', 'patent_id','section_id', 'subsection_id', 'group_id'
                            'subgroup_id', 'category', 'sequence']
output = []
post_mayo = []
patids = []

print("Creating catalogue of CPC codes")

with open('C:\\Users\\mgordon\\repos\\patents\\cpc_current.tsv','r') as f:
    for chunk in pd.read_table(f, delimiter = '\t', chunksize=1000000):
        output.append(chunk[chunk['group_id'].isin(sgid1)]['patent_id'])


out = np.asarray(output)
flat = [i for j in out for i in j]
    
for i in flat:
    if i > 8341762:
        post_mayo.append(i)
    
q = 0
post_mayo.sort()
    
for i in post_mayo:
    if i == q:
        pass
    else:
        patids.append(i)
    q = i


print("Preparing table of claims - this will take a long time")

with open('biotech_claims.txt','w') as g:
    with open('claim.tsv','r') as f:
        for chunk in pd.read_table(f, delimiter = '\t', chunksize=100000):
            tmp = (chunk[chunk['patent_id'].isin(patids)][chunk['dependent'].isnull()][['text']].values.tolist())
            flat = [item for sublist in tmp for item in sublist]
            for claim in flat:
                g.write(claim +'\n')
            count += 1
            print(str(count)+' out of 920 steps complete!', end='\r', flush=True)


documents = doc2vec.TaggedLineDocument('biotech_claims.txt')

print('Running gensim.doc2vec')

model = doc2vec.Doc2Vec(documents, vector_size=300, window=10, min_count=20, workers=12, sample=1e-5, seed = 42, epochs=10)

model.save('/artifacts/biotech_embedding.doc2vec')






