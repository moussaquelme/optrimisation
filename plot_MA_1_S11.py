# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:49:36 2023

@author: Moussa Sarr Ndiaye
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the CSV files and concatenate them into one dataframe
df1 = pd.read_csv('Z_RI_100um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])
df2 = pd.read_csv('Z_RI_90um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])
df3 = pd.read_csv('Z_RI_80um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])
df4 = pd.read_csv('Z_RI_70um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])
df5 = pd.read_csv('Z_RI_60um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])
df6 = pd.read_csv('Z_RI_50um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])
df7 = pd.read_csv('Z_RI_40um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])
df8 = pd.read_csv('Z_RI_30um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])
df9 = pd.read_csv('Z_RI_20um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])
df10 = pd.read_csv('Z_RI_10um.csv', header=None, names=['length', 'resonanz_freq', 'frequency', 'real', 'imag'])

# Create separate dataframes for the real part and frequency data for each CSV file
df1_real = df1[['frequency', 'real']]
df2_real = df2[['frequency', 'real']]
df3_real = df3[['frequency', 'real']]
df4_real = df4[['frequency', 'real']]
df5_real = df5[['frequency', 'real']]
df6_real = df6[['frequency', 'real']]
df7_real = df7[['frequency', 'real']]
df8_real = df8[['frequency', 'real']]
df9_real = df9[['frequency', 'real']]
df10_real = df10[['frequency', 'real']]



ymax = np.max(df9_real['real'])
xpos = np.where(df9_real['real'] == ymax)
xmax = np.array(df9_real['frequency'])[xpos[0]]
print('resonant frequency and Impendance max = ', xmax,ymax)

# Plot the data from each file separately
plt.plot(df1_real['frequency'], df1_real['real'], label='Inset_length: 100um')
plt.scatter(df1_real['frequency'], df1_real['real'])
plt.plot(df2_real['frequency'], df2_real['real'], label='Inset_length: 90um')
plt.scatter(df2_real['frequency'], df2_real['real'])
plt.plot(df3_real['frequency'], df3_real['real'], label='Inset_length: 80um')
plt.scatter(df3_real['frequency'], df3_real['real'])
plt.plot(df4_real['frequency'], df4_real['real'], label='Inset_length: 70um')
plt.scatter(df4_real['frequency'], df4_real['real'])
plt.plot(df5_real['frequency'], df5_real['real'], label='Inset_length: 60um')
plt.scatter(df5_real['frequency'], df5_real['real'])
plt.plot(df6_real['frequency'], df6_real['real'], label='Inset_length: 50um')
plt.scatter(df6_real['frequency'], df6_real['real'])
plt.plot(df7_real['frequency'], df7_real['real'], label='Inset_length: 40um')
plt.scatter(df7_real['frequency'], df7_real['real'])
plt.plot(df8_real['frequency'], df8_real['real'], label='Inset_length: 30um')
plt.scatter(df8_real['frequency'], df8_real['real'])
plt.plot(df9_real['frequency'], df9_real['real'], label='Inset_length: 20um')
plt.scatter(df9_real['frequency'], df9_real['real'])
plt.plot(df10_real['frequency'], df10_real['real'], label='Inset_length: 10um')
plt.scatter(df10_real['frequency'], df10_real['real'])

# Add a legend for each file
plt.legend()
plt.grid()

# Set x-axis limits
plt.xlim(280, 320)
#plt.ylim(0, 140)

# Set axis labels and title
plt.xlabel('Frequency (GHz)')
plt.ylabel('Impedance {R(Z} (Ω) ')
#plt.title('Impedance {R(Z} vs Frequency')

# Set figure size
plt.figure(figsize=(8, 6))

# Show the plot
#plt.grid()
#plt.show()



