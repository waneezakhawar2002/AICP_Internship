""" QUESTION # 1 """
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import plotly 
import seaborn as sn
columns = ['Category','Item','Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars',
           'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)',
           'Calcium (% Daily Value)', 'Iron (% Daily Value)']
print("\nQUESTION # 01\n")
df = pd.read_csv('menu.csv', usecols=columns, index_col='Item')
data_without_Category= df.drop(['Category'], axis=1)
print("Libraries imported and CSV File read.")

""" QUESTION # 2 """
print("\nQUESTION # 02\n")
statistical_facts = data_without_Category.describe(include='all').transpose()
print("Statistical Facts:")
print(statistical_facts) # print descriptive statistics for each column
print("\nMaximum Values:")
print(statistical_facts['max'])

""" QUESTION # 3 """
print("\nQUESTION # 03")
print("Heat Map")
corr_matrix = data_without_Category.corr()
plt.figure(figsize=(10,6))
sn.heatmap(corr_matrix)
plt.grid()
plt.show()
# The heat map shows the correlation between all pairs of variables in the dataset.
# The color intensity represents the correlation strength: darker colors represent stronger correlations.
# Variables with strong positive or negative correlations are highlighted by having darker colors.

""" QUESTION #  4 """
print("\nQUESTION # 04\n")
print("Box Plot")
plt.figure(figsize=(10,6))
sn.boxplot(y='Category',x='Calories',data=df,width=0.2,hue='Category',legend='brief')
plt.ylabel("Category")
plt.grid(axis='x')
plt.show()

""" QUESTION # 5 """
print("\nQUESTION # 05\n")
print("Items with highest quantities:\n")

values = statistical_facts['max']
attributes = values.index
maximum_values = values.values
for i in range (len(maximum_values)):
    item = df[df[attributes[i]]==maximum_values[i]].index[0]
    print(f"{attributes[i]}:  {item}  -  {maximum_values[i]}")

""" QUESTION # 6 """
print("\nQUESTION # 0\n")
print("Strip Plot")
plt.figure(figsize=(10,6))
sn.stripplot(x='Category',y='Calories',data=df,hue='Category',legend='brief')
plt.xlabel("Category")
plt.ylabel("Calories")
plt.grid(axis='y')
plt.title("Calories Content")
plt.show()

""" QUESTION # 7 """
print("\nQUESTION # 07\n")
print("Bar Plot")
Beef_Pork = df[df['Category']=='Beef & Pork']
plt.barh(Beef_Pork.index,sorted(Beef_Pork['Calories'],reverse=True))
plt.xlabel("Calories")
plt.show()