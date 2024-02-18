import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

""" QUESTION 1 """
x = [1,2,3]
y = [2,4,1]
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample Graph')
plt.plot(x,y)
plt.show()


""" QUESTION 2 """
x = [10,20,30]
y1 = [20,40,10]
y2 = [40,10,30]
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two lines with different widths and colors with suitable legend')
plt.plot(x,y1,color='b',linewidth=3, label='line1-width-3')
plt.plot(x,y2,color='r',linewidth=5, label='line2-width-5')
plt.legend()
plt.show()


""" QUESTION 3 """
x = [1,4,5,6,7]
y = [2,6,3,6,3]
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Display Marker')
plt.plot(x,y,color='r',ls='-.',marker='o',mfc='b',mec='b',ms=10)
plt.show()


""" Question 4 """
languages = ['Java','Python','PHP','JS','C#','C++']
popularity = [22.2,17.6,8.8,8,7.7,6.7]
plt.barh(languages,popularity, color='g')
plt.ylabel('Languages')
plt.xlabel('Popularity')
plt.title('Popularity of Programming Languages\n Worldwide, Oct 2017 compared to a year ago')
plt.grid(True,color='r',which='major',alpha=0.5)
plt.grid(True,color='b',which='minor',linestyle=':',alpha=0.5)
plt.minorticks_on()
plt.show()


""" Question 5 """
x_labels = [2,4,6,8,10]
a = [4,2,4,2,2]
b = [8,3,7,6,4]
c = [5,4,4,4,3]
d = [7,2,7,8,3]
e = [6,6,8,6,2]
X_axis = np.arange(len(x_labels)) 
print(X_axis)
plt.bar(X_axis - 0.2, a, 0.1, label = 'a') 
plt.bar(X_axis - 0.1, b, 0.1, label = 'b')
plt.bar(X_axis - 0, c, 0.1, label = 'c') 
plt.bar(X_axis + 0.1, d, 0.1, label = 'd') 
plt.bar(X_axis + 0.2, e, 0.1, label = 'e')  
  
plt.xticks(X_axis, x_labels) 
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("Horizontal Bar Plot") 
plt.legend() 
plt.grid(True,color='g',which='major',alpha=0.5)
plt.grid(True,color='b',which='minor',linestyle=':',alpha=0.5)
plt.minorticks_on()
plt.show() 

""" Question 6 """
file = pd.read_csv('Country_data.csv')
country = file['Country']
medals = file['Medals']
myexplode = []

for i in range(0,len(country)):
    if (country[i] == 'United States'):
        myexplode.append(0.2)
    else:
        myexplode.append(0)

plt.pie(medals, labels = country, explode = myexplode, autopct='%1.1f%%', shadow = True, startangle=90)
plt.show() 

""" Question 7 """
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#Maths Mark
plt.scatter(marks_range, math_marks,color='r',label="Math Marks")
#Science Marks
plt.scatter(marks_range, science_marks,color='g',label="Science Marks")
plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")
plt.title("Scatter Plot")
plt.legend(loc='upper right')
plt.show()