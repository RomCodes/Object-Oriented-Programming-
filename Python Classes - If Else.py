# Python class that accepts a dataframe and applies a conditional argument
import pandas as pd
import numpy as np

class DataFrameModifier():
    def __init__(self, dataframe):
        self.dataframe =dataframe

    def if_then_str(self, col):
        conditional =self.dataframe[col].apply(lambda x: np.where(x == 'A', 1, np.where(x =='AAMC',2,np.where(x == 'AAME',3,np.where(x =='ZX',10,4)))))
        return conditional
    
    def if_then_numeric_str(self, col_name):
        return self.dataframe[col_name].apply(lambda x: x[5:] if x.startswith('ABC') else x[4:] if x.startswith('AB') else x)

    
#Create a dummy dataframe
list_ = ['ABC::1234545432', 'AB23423432', 'A234523423']
list2_ = ['A','AAMC','ZX']

data = {'Account':list_ , 'Stock_Indices':list2_}
df = pd.DataFrame(data =data)
print(df)