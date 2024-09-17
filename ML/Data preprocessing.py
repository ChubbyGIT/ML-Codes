from optparse import Values
import pandas as pd
import matplotlib.pyplot as plt
#import numpy  as np
dataset =pd.read_csv("Data.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
print(x)
print(y)
from sklearn.impute import SimpleImputer
