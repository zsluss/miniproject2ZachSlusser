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

#maybe I could have done this as a for loop - but getting the means for all the different categories for champions, non-champions, and top 10 seeds

nonChampion_data = df[df['POSTSEASON'] != 'Champions']
top10seed_data = df[df['SEED'] <= 10]
champion_avg_ADJOE = champion_data['ADJOE'].mean()
nonChampion_avg_ADJOE = nonChampion_data['ADJOE'].mean()
top10seeed_avg_ADJOE = top10seed_data['ADJOE'].mean()
champion_avg_ADJDE = champion_data['ADJDE'].mean()
nonChampion_avg_ADJDE = nonChampion_data['ADJDE'].mean()
top10seed_avg_ADJDE = top10seed_data['ADJDE'].mean()
champion_avg_EFG0 = champion_data['EFG_O'].mean()
nonChampion_avg_EFG0 = nonChampion_data['EFG_O'].mean()
top10seed_avg_EFG0 = top10seed_data['EFG_O'].mean()
champion_avg_EFGD = champion_data['EFG_D'].mean()
nonChampion_avg_EFGD = nonChampion_data['EFG_D'].mean()
top10seed_avg_EFGD = top10seed_data['EFG_D'].mean()
champion_avg_tempo= champion_data['ADJ_T'].mean()
nonChampion_avg_tempo = nonChampion_data['ADJ_T'].mean()
top10seed_avg_tempo = top10seed_data['ADJ_T'].mean()

names = ['ADJOE', 'ADJDE', 'EFG_O', 'EFG_D', 'ADJ_T']
means = {  
    'ADJOE': [champion_avg_ADJOE, nonChampion_avg_ADJOE, top10seeed_avg_ADJOE],
    'ADJDE': [champion_avg_ADJDE, nonChampion_avg_ADJDE, top10seed_avg_ADJDE],
    'EFG_O': [champion_avg_EFG0, nonChampion_avg_EFG0, top10seed_avg_EFG0],
    'EFG_D': [champion_avg_EFGD, nonChampion_avg_EFGD, top10seed_avg_EFGD],
    'ADJ_T': [champion_avg_tempo, nonChampion_avg_tempo, top10seed_avg_tempo]
}
x = np.arange(len(names))
width = 0.15
multiplier = 0

fig, ax = plt.subplots(layout='constrained')
for attribute, mean in means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, mean, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel('Average Values')
ax.set_title('Average Values of Different Attributes for Champions, Non-Champions, and Top 10 Seeds')
ax.set_xticks(x + width, names)
ax.legend(loc='upper left', ncols=2)
plt.show()
