# Python class that accepts a dataframe and applies a conditional argument
import pandas as pd
import numpy as np

###Create a dummy dataframe
list_ = ['ABC::1234545432', 'AB23423432', 'A234523423']
list2_ = ['A','AAMC','ZX']
list3_ =[2,5,999999999990]

data = {'Account':list_ , 'Stock_Indices':list2_, 'Even_Odd':list3_}
df = pd.DataFrame(data =data)
print(df)



#Parent Class
class DataFrameModifier():
    def __init__(self, dataframe):
        self.dataframe =dataframe

    def if_then_str(self, col_name) -> int:
        conditional =self.dataframe[col_name].apply(lambda x: np.where(x == 'A', 1, np.where(x =='AAMC',2,np.where(x == 'AAME',3,np.where(x =='ZX',10,4)))))
        return conditional
    
    def if_then_numeric_str(self, col_name) -> str:
        return self.dataframe[col_name].apply(lambda x: x[5:] if x.startswith('ABC') else x[4:] if x.startswith('AB') else x)

#Test the classes on dataframe
modifier = DataFrameModifier(df)
df['modifier'] = modifier.if_then_str(col_name= 'Stock_Indices')

df['modifier_2'] =modifier.if_then_numeric_str(col_name='Account')

#Child Class
class DataFrameBuilder(DataFrameModifier):
    def __init__ (self, dataframe):
        super().__init__(dataframe)
        self.dataframe =dataframe

    def even_odd_child_test(self, col_name) -> str:
        return self.dataframe[col_name].apply(lambda x: np.where(x % 2 != 0, 'Odd', np.where(x % 2 == 0 and x >10000,'Even & Large Number', np.where(x % 2 ==0, 'Even','Error'))))
    

child_modifier = DataFrameBuilder(df)
df['test_even_odd'] =child_modifier.even_odd_child_test(col_name= 'Even_Odd')
print(df)
   
#Further cases to incorporate into OOP
""" import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
    elif n%2 ==0 and n < 6:
        print('Not Weird')
    elif n%2 ==0 and  (6<= n <=20):
        print('Weird')
    elif n%2 ==0 and n >20:
        print('Not Weird')
          """
