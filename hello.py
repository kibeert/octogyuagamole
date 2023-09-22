import pandas as pd
x= pd.read_csv("data.csv")
print(x)
print(pd.__version__)
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])