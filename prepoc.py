#%%
import re
import pandas as pd
#%%
df=pd.read_csv("dataset.csv")
# print(df)

# span=df["span"][1:-1]
# df['span']=[];
ss=[]
for s in df["span"]:
    s=s[1:-1].split(",")
    if(len(s)!=1):
        s=[int(z.strip()) for z in s]
    else:
        s=[]
    ss.append(s)
# print(ss)
df["span"]=ss
print(type(df["span"][1][0]))

# print(span)

# %%
