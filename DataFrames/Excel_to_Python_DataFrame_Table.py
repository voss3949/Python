#Excel to Python Conversion:
from __future__ import print_function
import pandas as pd
import numpy as np
df = pd.read_excel("P:\sd.xlsx")
df.head()

df.Product

df.iloc[:3]

#Pivot Table:
sales_report = pd.pivot_table(df, index=["Manager", "Rep", "Product"], values=["Price", "Quantity"],
                           aggfunc=[np.sum, np.mean], fill_value=0)
sales_report.head()

#Descriptive Statistics:
print(df[df["Product"]=="CPU"]["Quantity"].mean())
print(df[df["Product"]=="CPU"]["Price"].mean())
print(df[df["Product"]=="Software"]["Quantity"].mean())
print(df[df["Product"]=="Software"]["Price"].mean())

