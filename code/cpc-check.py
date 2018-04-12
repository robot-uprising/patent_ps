import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm

sgid = 'C12Q1/68'
fields = ['uuid', 'patent_id','section_id', 'subsection_id', 'group_id'
                            'subgroup_id', 'category', 'sequence']
output = []

with open('C:\\Users\\mgordon\\repos\\patents\\post_mayo_output.pickle','wb') as g:
    with open('C:\\Users\\mgordon\\repos\\patents\\cpc_current.tsv','r') as f:
        for chunk in tqdm(pd.read_table(f, delimiter = '\t', chunksize=1000000), total=34):
            output.append(chunk[chunk['subgroup_id'] == sgid]['patent_id'])
    out = np.asarray(output)
    flat = [i for j in out for i in j]
    pickle.dump(flat, g, pickle.HIGHEST_PROTOCOL)
