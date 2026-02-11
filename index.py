# INF601 - Advanced Programming in Python

# Zach Slusser

# Mini Project 2 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df= pd.read_csv('data/cbb.csv')
champion_data=  df[df['POSTSEASON'] == 'Champions']
plottingData = champion_data

#print(champion_data)
print(champion_data)