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


# Create a horizontal bar chart to visualize the adjusted offensive efficiency (ADJOE) of NCAA champions
bars = champion_data['TEAM+YEAR'].values
data = champion_data['ADJOE'].values
y_pos = np.arange(len(data))

fig, ax =plt.subplots()
ax.barh(y_pos, data, align='center', color="pink")
#adding mean line for this one 
data_mean = np.mean(data)
plt.axvline(x=data_mean, color='r', linestyle='--', label=f'Mean: {data_mean:.2f}')
plt.legend()

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
#aftering adding a mean line for BARTHAG, I decided to add it to to others.
data_mean = np.mean(data)
plt.axhline(y=data_mean, color='r', linestyle='--', label=f'Mean: {data_mean:.2f}')
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
#added a horizontal line to show the mean of the BARTHAG values for champions
data_mean = np.mean(data)
plt.axhline(y=data_mean, color='r', linestyle='--', label=f'Mean: {data_mean:.2f}')
plt.legend()
plt.xticks(rotation=90)
plt.ylabel('Average BARTHAG')
plt.suptitle('Average BARTHAG of NCAA Champions Over the Years')
plt.show()

#maybe I could have done this as a for loop - but getting the means for all the different categories for champions, non-champions, and top 10 seeds

nonChampion_data = df[df['POSTSEASON'] != 'Champions']
top10seed_data = df[df['SEED'] <= 10]
champion_avg_ADJOE = champion_data['ADJOE'].mean().round(1)
nonChampion_avg_ADJOE = nonChampion_data['ADJOE'].mean().round(1)
top10seeed_avg_ADJOE = top10seed_data['ADJOE'].mean().round(1)
champion_avg_ADJDE = champion_data['ADJDE'].mean().round(1)
nonChampion_avg_ADJDE = nonChampion_data['ADJDE'].mean().round(1)
top10seed_avg_ADJDE = top10seed_data['ADJDE'].mean().round(1)
champion_avg_EFG0 = champion_data['EFG_O'].mean().round(1)
nonChampion_avg_EFG0 = nonChampion_data['EFG_O'].mean().round(1)
top10seed_avg_EFG0 = top10seed_data['EFG_O'].mean().round(1)
champion_avg_EFGD = champion_data['EFG_D'].mean().round(1)
nonChampion_avg_EFGD = nonChampion_data['EFG_D'].mean().round(1)
top10seed_avg_EFGD = top10seed_data['EFG_D'].mean().round(1)
champion_avg_tempo= champion_data['ADJ_T'].mean().round(1)
nonChampion_avg_tempo = nonChampion_data['ADJ_T'].mean().round(1)
top10seed_avg_tempo = top10seed_data['ADJ_T'].mean().round(1)


#Chart that compares the average values of ADJOE, ADJDE, EFG_O, EFG_D, and ADJ_T for champions, non-champions, and top 10 seeds
names = ['ADJOE', 'ADJDE', 'EFG_O', 'EFG_D', 'ADJ_T']
means = {  

    'Champions': [champion_avg_ADJOE, champion_avg_ADJDE, champion_avg_EFG0, champion_avg_EFGD, champion_avg_tempo],
    'Non-Champions': [nonChampion_avg_ADJOE, nonChampion_avg_ADJDE, nonChampion_avg_EFG0, nonChampion_avg_EFGD, nonChampion_avg_tempo],
    'Top 10 Seeds': [top10seeed_avg_ADJOE, top10seed_avg_ADJDE, top10seed_avg_EFG0, top10seed_avg_EFGD, top10seed_avg_tempo]
}
width = 0.5
group_gap = 0.5
group_width = width * len(means)
x = np.arange(len(names)) * (group_width + group_gap)
multiplier = 0

fig, ax = plt.subplots(layout='constrained')
for attribute,measurement in means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_xticks(x + group_width / 2 - width / 2, names)
ax.legend(loc='upper right', ncols=3)
ax.set_ylabel('Average Values')
ax.set_title('Average Metrics for Champions, Non-Champions, and Top 10 Seeds')
plt.show()
