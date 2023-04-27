# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:49:36 2023

@author: Moussa Sarr Ndiaye
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np

# Read in the CSV files and concatenate them into one dataframe
#df1 = pd.read_csv('S Parameter_15um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'S11'])
df1 = pd.read_csv('S Parameter_5um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'S11'])
df2 = pd.read_csv('S Parameter_15um.csv', header=None, names=['length', 'frequency', 'S11'])
df3 = pd.read_csv('S Parameter_35um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'S11'])
df4 = pd.read_csv('S Parameter_45um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'S11'])
df5 = pd.read_csv('S Parameter_60um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'S11'])
df6 = pd.read_csv('S Parameter_80um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'S11'])
df7 = pd.read_csv('S Parameter_100um.csv', header=None, names=['length', 'frequency', 'S11'])

# Create separate dataframes for the real part and frequency data for each CSV file
df1_real = df1[['frequency', 'S11']]
df2_real = df2[['frequency', 'S11']]
df3_real = df3[['frequency', 'S11']]
df4_real = df4[['frequency', 'S11']]
df5_real = df5[['frequency', 'S11']]
df6_real = df6[['frequency', 'S11']]
df7_real = df7[['frequency', 'S11']]
#print(df1['S11'])




ymax = np.max(df2_real['S11'])
xpos = np.where(df2_real['S11'] == ymax)
xmax = np.array(df2_real['frequency'])[xpos[0]]
print('resonant frequency and Impendance max = ', xmax,ymax)

# Plot the data from each file separately
plt.plot(df1_real['frequency'], df1_real['S11'], label='Inset_length: 5um')
plt.scatter(df1_real['frequency'], df1_real['S11'])

plt.plot(df2_real['frequency'], df2_real['S11'], label='Inset_length: 15um')
plt.scatter(df2_real['frequency'], df2_real['S11'])

plt.plot(df3_real['frequency'], df3_real['S11'], label='Inset_length: 35um')
plt.scatter(df3_real['frequency'], df3_real['S11'])

plt.plot(df4_real['frequency'], df4_real['S11'], label='Inset_length: 45um')
plt.scatter(df4_real['frequency'], df4_real['S11'])

#plt.plot(df5_real['frequency'], df5_real['S11'], label='Inset_length: 60um')
#plt.scatter(df5_real['frequency'], df5_real['S11'])

#plt.plot(df6_real['frequency'], df6_real['S11'], label='Inset_length: 80um')
#plt.scatter(df6_real['frequency'], df6_real['S11'])

#plt.plot(df7_real['frequency'], df7_real['S11'], label='Inset_length: 100um')
#plt.scatter(df7_real['frequency'], df7_real['S11'])

# Add a legend for each file
plt.legend()
plt.grid()

# Set x-axis limits
plt.xlim(290, 310)
#plt.ylim(0, 140)

# Set axis labels and title
plt.xlabel('Frequency (GHz)')
plt.ylabel('S_11 (dB) ')
#plt.title('Impedance {R(Z} vs Frequency')
plt.grid()
# Set figure size
plt.figure(figsize=(8, 6))

# Show the plot
#plt.grid()
#plt.show()



