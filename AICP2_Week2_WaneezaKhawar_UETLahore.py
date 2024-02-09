import pandas as pd

""" Question 1 """
data1 = [1,4,9,6,7]
index1 = ['a','x','c','2','e']
q1 = pd.Series(data1, index=index1)
print("Question # 1")
print(q1)

""" Question 2 """
data2 = {'Bilal':42,'Ayesha':32,'Hadia':39}
q2 = pd.Series(data2)
print("\nQuestion # 2\n")
print(q2)

""" Question 3 """
data3 = {
    'day' : ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature' : [32,35,28,24,32,31],
    'windspeed' : [6,7,2,7,4,2],
    'event' : ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny'] 
}
q3 = pd.DataFrame(data3)
print("\nQuestion # 3\n")
print(q3)

""" Question 4 """
q4 = pd.DataFrame(data3, index=['a','b','c','d','e','f'])
print("\nQuestion # 4\n")
print(q4)

""" Question 5 """
mean = q3['temperature'].mean()
maximum = q3['temperature'].max()
minimum = q3['temperature'].min()
print("\nQuestion # 5\n")
print('Mean Temperature:',mean)
print('Maximum Temperature',maximum)
print('Minimum Temperature:',minimum)

""" Question 6 """
file6 = pd.read_csv('people.csv', index_col=["Sex", "Job Title"],
        usecols=["First Name", "Sex", "Email", "Phone", "Job Title"], 
        skiprows=[1,5])
file6.to_csv('NewPeople.csv')

""" Question 7 """
file7 = pd.read_excel('SampleWork.xlsx', sheet_name='Sheet1',
                      usecols=[0,3], skiprows=[2])
# Set row 2 as header
file7.columns = file7.iloc[1]
file7 = file7.drop(file7.index[1])
file7.to_excel('NewSheet.xlsx', index = False)

""" Question 8 """
AICP_Dict = {
    'Name':['Sonia','Bilal','Hifza','Kabir','jazim'],
    'Age':[27,24,22,32,23],
    'Address':['Lahore','Karachi','Sialkot','Peshawar','lhr'],
    'Qualification':['Msc','MA','MCA','Phd','bsc']
}

AICP_DF = pd.DataFrame(AICP_Dict)
print("\nQuestion # 8 - DataFrame:\n")
print(AICP_DF)

df1 = AICP_DF.loc[:,['Name','Qualification']]
print( "\nOnly Name and Qualification columns:\n")
print(df1)

AICP_DF['Height'] = [5.1, 6.2, 5.1, 5.2,5.1]
print( "\nAdded Height column to the dataframe:\n")
print(AICP_DF)

AICP_DF.set_index('Name' , inplace=True)
print("\nAfter Setting Index:\n")
print(AICP_DF)

Hifza = AICP_DF.loc['Hifza']
print( "\nData of Hifza:\n")
print(Hifza)

Index_3 = AICP_DF.iloc[3]
print( "\nThe data at Row number 3:\n")
print(Index_3)

AICP_DF.drop('Bilal',inplace=True)
print( "\nAfter Dropping Bilal from DataFrame:\n")
print(AICP_DF)

