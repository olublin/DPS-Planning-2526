#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import os
import zipfile


# In[29]:


class buildMatrix:
    def __init__(self, zip_path):
        self.path = zip_path

    def parse_zip(self):
        self.dfs = []
        with zipfile.ZipFile(self.path) as z:
            for file in sorted([f for f in z.namelist() if f.endswith('.csv')]):
                with z.open(file) as f:
                    df = pd.read_csv(f, index_col = 0)
                    self.dfs.append(df)

    def concat(self):
        self.matrix = pd.concat(self.dfs, axis = 1)
        self.matrix = self.matrix.loc[:, ~self.matrix.columns.duplicated()] #remove duplicated columns (one time error)
        self.matrix.columns = range(0,851)  #index with numeric values


    def fill(self):  #fill null values if cross-diagonal is not null with cross-diagonal value
        M = self.matrix.copy()
        M_filled = M.combine_first(M.T) #replaces M[i,j] with M[j,i] if one is null
        self.matrix = M_filled


    def process_na(self, replace = 35): #value to replace null with
        self.matrix = self.matrix.fillna(replace)

    def average(self):             #averages all cross diagonal entries
        M = self.matrix.copy()
        M_averaged = (M + M.T)/2
        self.matrix = M_averaged

        self.matrix.to_csv('dist_matrix_final.csv')




# In[30]:


matrix = buildMatrix(f'{os.getcwd()}//isochron_results.zip')
matrix.parse_zip()
matrix.concat()
matrix.fill()
matrix.process_na()
matrix.average()


# In[ ]:




