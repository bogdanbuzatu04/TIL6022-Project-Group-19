#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 14:40:01 2025

@author: yanniskiesslich
"""
# Disruption Causes Pie Chart - Combined 2023 and 2024

import pandas as pd
import matplotlib.pyplot as plt
import os


# Load disruption data
df_disruptions_2023 = pd.read_csv('disruptions-2023.csv')
df_disruptions_2024 = pd.read_csv('disruptions-2024.csv')

print(f"2023 disruptions: {len(df_disruptions_2023):,}")
print(f"2024 disruptions: {len(df_disruptions_2024):,}")

# Combine 2023 & 2024
df_disruptions = pd.concat([df_disruptions_2023, df_disruptions_2024], ignore_index=True)
print(f"Total disruptions combined: {len(df_disruptions):,}")

# Count disruptions by cause_group
cause_counts = df_disruptions['cause_group'].value_counts()

print(f"\nOriginal disruption counts by cause_group:")
print(cause_counts)


# COMBINE "weather" and "unknown" into "Others"
labels = cause_counts.index.tolist()
values = cause_counts.values.tolist()

# Categories to combine into "Others"
combine_set = {'weather', 'unknown'}

# Build new dictionary combining specific categories
new_counts = {}
for lab, val in zip(labels, values):
    key_lower = lab.strip().lower()
    if key_lower in combine_set:
        new_counts['Others'] = new_counts.get('Others', 0) + val
    else:
        new_counts[lab] = new_counts.get(lab, 0) + val

# Sort by value (descending) and put "Others" at the end
from collections import OrderedDict
sorted_items = sorted(new_counts.items(), key=lambda x: x[1], reverse=True)
ordered = OrderedDict()

for k, v in sorted_items:
    if k != 'Others':
        ordered[k] = v

# Add "Others" at the end 
if 'Others' in new_counts:
    ordered['Others'] = new_counts['Others']

labels_final = list(ordered.keys())
sizes_final = list(ordered.values())

print(f"\nDisruption Causes (Percentages):")
for label, size in zip(labels_final, sizes_final):
    pct = (size / len(df_disruptions)) * 100
    print(f"  {label:20s}: {size:5,} ({pct:5.1f}%)")


# VISUALIZATION
fig, ax = plt.subplots(figsize=(12, 8))

# Define colors 
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2']
colors = colors + ['#C0C0C0'] * (len(labels_final) - len(colors))  # Add gray for additional categories

# Create pie chart 
wedges, texts, autotexts = ax.pie(
    sizes_final,
    labels=labels_final,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors[:len(labels_final)],
    labeldistance=1.20,    
    pctdistance=0.80,      
    textprops={'fontsize': 11}
)

# percentage text 
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

# label text
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('bold')

ax.set_title('Train Disruption Causes (2023–2024)', 
             fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('disruption_causes_pie_chart_combined.png', dpi=300, bbox_inches='tight')
plt.show()

