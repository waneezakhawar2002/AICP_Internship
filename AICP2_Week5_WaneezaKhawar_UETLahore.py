
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from wordcloud import WordCloud
pio.templates.default = "plotly_white"

""" QUESTION # 1 """
print("\nQUESTION # 01\n")
df = pd.read_csv("instagram_data.csv", encoding="latin-1")
print("Column Names and Info:")
print(df.columns)
print(df.info)

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
print("Histogram")
fig = px.histogram(df, x="Impressions", title="Distribution of Impressions")
fig.show()

""" QUESTION # 5 """
print("\nQUESTION # 05\n")
print("Impressions over Time:\n")
fig = px.line(df, x=df.index, y="Impressions", title='Impressions over Time')
fig.show()

""" QUESTION # 6 """
print("\nQUESTION # 06\n")
print("Metrics over Time:\n")
fig = px.line(df, x=df.index, y=['Likes','Saves','Follows'], title='Metrics over Time')
fig.update_xaxes(title_text="Date")  
fig.update_yaxes(title_text="Count") 
fig.show()

""" QUESTION # 7 """
print("\nQUESTION # 07\n")
print("Reach from Different Sources Pie Plot")
df1 = df[['From Home','From Hashtags','From Explore','From Other']].copy()
fig = px.pie(df1, values=df1.sum(), names=df1.columns, title='Reach from Different Sources')
fig.show()

""" QUESTION # 8 """
print("\nQUESTION # 08\n")
print("Engagement Sources Pie Plot")
df2 = df[['Likes','Saves','Shares','Comments']].copy()
fig = px.pie(df2, values=df2.sum(), names=df2.columns, title='Engagement Sources')
fig.show()

""" QUESTION # 9 """
print("\nQUESTION # 09\n")
print("Profile Visits vs Follows Scatter Plot")
fig = px.scatter(df, x="Profile Visits", y="Follows", title="Profile Visits vs Follows", trendline="ols")
fig.show()

""" QUESTION # 10 """
print("\nQUESTION # 10\n")
print("Word Cloud")
df['Hashtags_List'] = df['Hashtags'].apply(lambda x: x.split(',')) 
all_hashtags = ' '.join([item for sublist in df['Hashtags_List'] for item in sublist])  # Join all hashtags
wordcloud = WordCloud(width=800, height=600).generate(all_hashtags)
fig = px.imshow(wordcloud, title="Hashtag Word Cloud")
fig.show()

""" QUESTION # 11 """
print("\nQUESTION # 11\n")
print("Correlation:")
df3 = df[['Impressions', 'From Home', 'From Hashtags', 'From Explore',
       'From Other', 'Saves', 'Comments', 'Shares', 'Likes', 'Profile Visits',
       'Follows']].copy()
correlation_matrix = df3.corr()
fig = px.imshow(correlation_matrix,  # Heatmap data
                x=correlation_matrix.columns,  # X-axis labels (feature names)
                y=correlation_matrix.columns,  # Y-axis labels (feature names)
                zmin=-1, zmax=1,  # Set color scale range for correlation coefficients
                color_continuous_scale='RdBu',  # Color scale for positive/negative correlations
                title="Correlation Matrix")
fig.update_xaxes(title_text="Features")  
fig.update_yaxes(title_text="Features") 
fig.update_traces(colorbar=dict(title="Correlation Coefficient"))  # Add colorbar label
fig.show()

""" QUESTION # 12 """
print("\nQUESTION # 12\n")
print("Distribution of Hashtags:")
arr = []
for i in range (len(df["Hashtags"])):
    temp = df["Hashtags"][i].split()
    arr.extend(temp)
hashtags = pd.Series(arr)
df4 = hashtags.value_counts()
fig = px.bar(df4, x=df4.index, y=df4, title="Distribution of Hashtags")
fig.update_xaxes(title_text="Hashtag")  
fig.update_yaxes(title_text="Count") 
fig.show()

""" QUESTION # 13 """
print("\nQUESTION # 13\n")
print("Likes Distribution for each Hashtags:")
df5 = pd.DataFrame({
    'Hashtags' : [],
    'Likes' : [],
    'Impressions' : []})
for i in range (len(df["Hashtags"])):
    temp = df["Hashtags"][i].split()
    for j in range (len(temp)):
        if temp[j] in df5['Hashtags']:
            index = df5[df5['Hashtags'] == temp[j]].index[0]
            df5.loc[index,'Likes'].iat[0] += int(df["Likes"][i])
            df5.loc[index,'Impressions'].iat[0] += int(df["Impressions"][i])
        else:
            df_new = pd.DataFrame({'Hashtags':[temp[j]], 'Likes':[int(df["Likes"][i])], 'Impressions':[int(df["Impressions"][i])]})
            df5 = pd.concat([df5,df_new])
fig = px.bar(df5, x="Hashtags", y='Likes', title="Likes Distribution for each Hashtags")
fig.update_xaxes(title_text="Hashtag")  
fig.update_yaxes(title_text='Likes') 
fig.show()

print("Impressions Distribution for each Hashtags:")
fig = px.bar(df5, x="Hashtags", y='Impressions', title="Impressions Distribution for each Hashtags")
fig.update_xaxes(title_text="Hashtag")  
fig.update_yaxes(title_text='Impressions') 
fig.show()

""" QUESTION # 14 """
print("\nQUESTION # 14\n")
print("Summary:")
print("* The distribution of impressions is skewed, with a few posts having very high impressions.")
print("* Likes, Saves, and Follows generally follow similar trends over time.")
print("* The wordcloud reveals the most prominent hashtags used.")
print("* There is a positive correlation between profile visits and follows.")
print("* Comments almost have negative correlation with every other metric.")

