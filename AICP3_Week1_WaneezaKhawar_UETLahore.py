import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

""" Question # 01 """
print("\nQuestion # 01\n")
df = pd.read_csv("transaction_anomalies_dataset.csv")
print("Checking for Null Values:")
print(df.isnull().sum())
print("\nChecking Column Info:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe().T)

""" Question # 02 """
print("\nQuestion # 02\n")
fig = px.histogram(df, x='Transaction_Amount', title='Distribution of Transaction Amounts in the data.')
fig.show()

""" Question # 03 """
print("\nQuestion # 03\n")
fig = px.box(df, x='Account_Type', y='Transaction_Amount', title='Distribution of Transaction Amounts by Account Type.')
fig.show()

""" Question # 04 """
print("\nQuestion # 04\n")
fig = px.scatter(df, x='Age', y='Average_Transaction_Amount', color='Account_Type',trendline='ols', title='Distribution of Average Transaction Amounts by Age.')
fig.show()

""" Question # 05 """
print("\nQuestion # 05\n")
df1 = df.groupby(['Day_of_Week'])['Transaction_Amount'].count()
print(df1)
fig = px.bar(df1, x=df1.index, y=df1, title='Distribution of Transactions by Day of Week.')
fig.show()

""" Question # 06 """
print("\nQuestion # 06\n")
df2 = df[['Transaction_Amount','Transaction_Volume','Average_Transaction_Amount','Frequency_of_Transactions','Time_Since_Last_Transaction','Age','Income']]
df_corr = df2.corr()
fig = px.imshow(df_corr, title='Correlation Heatmap')
fig.show()

""" Question # 07 """
print("\nQuestion # 07\n")
avg = df['Transaction_Amount'].mean()
upper_bound = avg*2
df['Is_Anomaly'] =  df['Transaction_Amount']>upper_bound
fig = px.scatter(df, x='Transaction_Amount', y='Average_Transaction_Amount', color='Is_Anomaly', title='Anomalies in Transaction Amount.')
fig.show()

""" Question # 08 """
print("\nQuestion # 08\n")
total = df['Is_Anomaly'].value_counts()
normal = total[False]
anomalies = total[True]
anomalies_ratio = anomalies/(anomalies+normal)
print(f"Anomaly Ratio: {anomalies_ratio}")

""" Question # 09 """
print("\nQuestion # 09\n")
features = ["Transaction_Amount", "Average_Transaction_Amount", "Frequency_of_Transactions"]
X = df[features]
y = []
for i in range (0,len(df[['Is_Anomaly']])):
    if  df["Is_Anomaly"].iloc[i]:
        y.append(0)
    else:
        y.append(1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# Isolate Forest model for anomaly detection
model = IsolationForest(contamination=anomalies_ratio)  # Contamination parameter based on estimated
model.fit(X_train,y_test)
y_pred = model.predict(X_test)
y_pred[y_pred == -1] = 0
print("Confusion Matrix:")
print(confusion_matrix(y_pred, y_test))

""" Question # 10 """
print("\nQuestion # 10\n")
print("Classification Report:")
print(classification_report(y_pred, y_test))

""" Question # 11"""
print("\nQuestion # 11\n")
Transaction_Amount = int(input("Enter the value for 'Transaction_Amount':"))
Average_Transaction_Amount = int(input("Enter the value for 'Average_Transaction_Amount':"))
Frequency_of_Transactions = int(input("Enter the value for 'Frequency_of_Transactions':"))
X_sample = pd.DataFrame({
    "Transaction_Amount":[Transaction_Amount],
    "Average_Transaction_Amount":[Average_Transaction_Amount], 
    "Frequency_of_Transactions":[Frequency_of_Transactions]})
y_sample = model.predict(X_sample)
if y_sample==0:
   print('The transaction is Normal.')
else:
   print('Anomaly Detected: This transaction is flagged as an anomaly.')
