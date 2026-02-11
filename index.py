# INF601 - Advanced Programming in Python

# Zach Slusser

# Mini Project 2 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df= pd.read_csv('data/cbb.csv')
df = df.sort_values(by='YEAR', ascending=False)
champion_data=  df[df['POSTSEASON'] == 'Champions']
champion_data['TEAM+YEAR'] = champion_data['TEAM'] + ' ' + champion_data['YEAR'].astype(str)
#print(champion_data)
print(champion_data)


# Create a horizontal bar chart to visualize the adjusted offensive efficiency (ADJOE) of NCAA champions
bars = champion_data['TEAM+YEAR'].values
data = champion_data['ADJOE'].values
y_pos = np.arange(len(data))

fig, ax =plt.subplots()
ax.barh(y_pos, data, align='center')

x_max_value = max(data) 
ax.set_xlim(right= x_max_value * 1.1)

plt.yticks(y_pos, bars)
plt.xlabel('Adjusted Offensive Efficiency (ADJOE)')
plt.suptitle('Adjusted Offensive Efficiency of NCAA Champions')
plt.show()

#Create vertical bar chart to visualize the adjusted defensive efficiency (ADJDE) of NCAA champions
bars = champion_data['TEAM+YEAR'].values
data = champion_data['ADJDE'].values
fig ,ax = plt.subplots()
line = ax.bar(bars, data, align='center')
x_max_value = max(data)
ax.set_ylim(top= x_max_value * 1.1)
plt.xticks(rotation=90)
plt.ylabel('Adjusted Defensive Efficiency (ADJDE)')
plt.suptitle('Adjusted Defensive Efficiency of NCAA Champions')
plt.show()

#Create a scatter chart to visualize the average BARTHAG (a measure of team strength) of NCAA champions over the years
champion_data['BARTHAG'] = champion_data['BARTHAG'].astype(float)
bars = champion_data['TEAM+YEAR'].values
data = champion_data['BARTHAG'].values

fig, ax = plt.subplots()
ax.scatter(bars, data)
plt.xticks(rotation=90)
plt.ylabel('Average BARTHAG')
plt.suptitle('Average BARTHAG of NCAA Champions Over the Years')
plt.show()
