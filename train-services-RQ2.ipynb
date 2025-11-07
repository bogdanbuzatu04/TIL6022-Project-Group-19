#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 15:22:59 2025

@author: yanniskiesslich
"""

# Dutch Train Services Analysis 

import pandas as pd
import matplotlib.pyplot as plt
import os



# Calculate average amount of train services per time of day (using median time for each train service)


# Load data
df_2023 = pd.read_csv('services-2023.csv.gz', compression='gzip')
df_2024 = pd.read_csv('services-2024.csv.gz.csv', compression='gzip')

# Combine datasets
df_services = pd.concat([df_2023, df_2024], ignore_index=True)
print(f"Total records loaded: {len(df_services):,}")

# Parse timestamps
df_services['Stop:Departure time'] = pd.to_datetime(
    df_services['Stop:Departure time'], 
    errors='coerce', 
    utc=True
)
df_services['Stop:Arrival time'] = pd.to_datetime(
    df_services['Stop:Arrival time'], 
    errors='coerce', 
    utc=True
)

# Drop rows where either departure or arrival is invalid
df_services = df_services.dropna(subset=['Stop:Departure time', 'Stop:Arrival time'])

# Create unique train ID
df_services['train_id'] = df_services['Service:RDT-ID']

# For each train: get first departure and last arrival
journey_times = (df_services
                 .groupby('train_id', as_index=False)
                 .agg({
                     'Stop:Departure time': 'min',  # First departure
                     'Stop:Arrival time': 'max'      # Last arrival
                 })
                 .rename(columns={
                     'Stop:Departure time': 'first_departure',
                     'Stop:Arrival time': 'last_arrival'
                 }))

print(f"Unique trains: {len(journey_times):,}")

# Calculate median time (midpoint between first departure and last arrival)
journey_times['median_time'] = (
    journey_times['first_departure'] + 
    (journey_times['last_arrival'] - journey_times['first_departure']) / 2
)

# Extract date and hour from median time
journey_times['date'] = journey_times['median_time'].dt.date
journey_times['hour'] = journey_times['median_time'].dt.hour

# Count unique days
unique_dates = journey_times['date'].nunique()
print(f"Unique calendar days: {unique_dates}")

# Count total departures per hour (based on median time)
total_per_hour = journey_times['hour'].value_counts().reindex(range(24), fill_value=0).sort_index()

# Calculate average per day
average_per_hour = total_per_hour / unique_dates

print(f"\nAverage train journeys per hour per day (using median journey time):")
print(average_per_hour.round(2))


# VISUALIZATION
hours = list(range(24))
counts_avg = average_per_hour.values

fig, ax = plt.subplots(figsize=(14, 7))
bars = ax.bar(hours, counts_avg, color='coral', edgecolor='black', alpha=0.8, width=0.8)

ax.set_xlabel('Hour of day', fontsize=12, fontweight='bold')
ax.set_ylabel('Average number of train journeys per day', fontsize=12, fontweight='bold')
ax.set_title('Average train journey distribution per hour per day (2023–2024)\nBased on median time between first departure and last arrival', 
             fontsize=14, fontweight='bold')
ax.set_xticks(hours)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels above each bar
for bar, val in zip(bars, counts_avg):
    ax.annotate(f'{val:.1f}', 
                xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                xytext=(0, 4), textcoords='offset points',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('services_per_hour_median_journey.png', dpi=300, bbox_inches='tight')
plt.show()


# SUMMARY
print("Summary:")
print("-" * 50)
print(f"Peak hour: {average_per_hour.idxmax()}:00 with {average_per_hour.max():.2f} journeys/day")
print(f"Lowest hour: {average_per_hour.idxmin()}:00 with {average_per_hour.min():.2f} journeys/day")
print(f"Average total journeys per day: {average_per_hour.sum():.0f}")
