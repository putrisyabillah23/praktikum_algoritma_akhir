# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:41:37 2022

@author: putri
"""

import pandas as pd

df = pd.read_csv("Negara.csv" , index_col=1)
mean = df.groupby(["Benua"]).mean()
std = df.groupby(["Benua"]).std()

print("Berikut data framenya :")
print(df, "\n")

print("Berikut data mean :")
print(mean, "\n")

print("Berikut data standard deviation")
print(std, "\n")

mean.to_csv("NegaraMean.csv")
std.to_csv("NegaraStandardDeviation.csv")
print("File Berhasil Dibuat")



                 