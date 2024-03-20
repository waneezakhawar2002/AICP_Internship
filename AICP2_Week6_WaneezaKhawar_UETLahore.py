import pandas as pd
import plotly.express as px

""" QUESTION # 1 """
print("\nQUESTION # 01\n")
df = pd.read_csv("births.csv")
df['decade'] = df['year']-(df['year']%10)
print(df.head(10))

""" QUESTION # 2 """
print("\nQUESTION # 02\n")
print("Descriptive Statistics:")
print(df.describe())

""" QUESTION # 3 """
print("\nQUESTION # 03\n")
print("Missing Values:")
print(df.isnull().sum())

""" QUESTION # 4 """
print("\nQUESTION # 04\n")
print("Trend of Male and Female births every decade:")
df_female = df[df['gender']=='F']
df_male = df[df['gender']=='M']
female_births = df_female["decade"].value_counts(sort=False)
male_births = df_male["decade"].value_counts(sort=False)
df_gender = pd.DataFrame({
    'Female Births' : female_births,
    'Male Births' : male_births
})
fig = px.line(df_gender, x=df_gender.index, y=['Female Births','Male Births'], title='Trend of Male and Female births every decade')
fig.update_xaxes(title_text="Decade")  
fig.update_yaxes(title_text="Births") 
fig.show()
print("Trend of Male and Female births every decade is almost the same.")

""" QUESTION # 5 """
print("\nQUESTION # 05\n")
print("Removing outliers:")
# Q.5: Remove outliers (using Interquartile Range - IQR method)
q1 = df["births"].quantile(0.25)
q3 = df["births"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
df_filtered = df.loc[(df["births"] >= lower_bound) & (df["births"] <= upper_bound)]
# Analyze the outliers if desired (optional)
outlier_count = len(df) - len(df_filtered)
print(f"Number of outliers removed: {outlier_count}")

""" QUESTION # 6 """
print("\nQUESTION # 06\n")
print("Plot births by weekday for several decades.:")
weekday_grouped = df.groupby(["decade", "day"])["births"].sum()
print(weekday_grouped)
print(weekday_grouped.index[0][0])
decades = []
days = []
births = []
for i in range (0,len(weekday_grouped)):
    decades.append(weekday_grouped.index[i][0])
    days.append(weekday_grouped.index[i][1])
    births.append(weekday_grouped.iloc[i])

df_grouped = pd.DataFrame({
    'Decade':decades,
    'Day':days,
    'Births':births
})

fig = px.bar(df_grouped, x='Day', y='Births', color='Decade', barmode='group', title="Births by Weekday for Different Decades")
fig.update_xaxes(title="Weekday")  # Add weekday labels
fig.update_yaxes(title="Total Births")  # Add y-axis label
fig.show()

""" QUESTION # 7 """
print("\nQUESTION # 07\n")
print("Grouping the data by month and day separately:\n")
weekday_grouped = df.groupby(["day"])["births"].sum()
month_grouped = df.groupby(["month"])["births"].sum()
print("Grouping the data by day:")
print(weekday_grouped)
print("Grouping the data by month:")
print(month_grouped)

""" QUESTION # 8 """
print("\nQUESTION # 08\n")
print("Time series plot:\n")
df = df.dropna()
df_new = pd.DataFrame({
    'Date':[],
    'Births':[]
})
months = ['Jan','Feb','March','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in range (0,len(months)):
    new_row = df[df['month']==i+1].groupby(["day"])["births"].mean()
    new_row = new_row.drop(99)
    for j in range (0, len(new_row)):
        date = f'{months[i]},{int(new_row.index[j])}'
        df_temp = pd.DataFrame({'Date':[date],'Births':[new_row.iloc[j]]})
        df_new = pd.concat([df_new,df_temp])
fig = px.line(df_new, x='Date', y="Births", title='Time-Series Data')
fig.show()


