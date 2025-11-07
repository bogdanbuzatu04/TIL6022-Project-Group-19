#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:17:33 2025

@author: yanniskiesslich
"""

# Average Delay per hour per day (using median time of train services)
import pandas as pd
import matplotlib.pyplot as plt
import os


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

# Ensure delay column exists and is numeric (fill NaNs with 0)
# Assuming column name is 'Stop:Arrival delay' or similar; adjust if different
if 'Stop:Arrival delay' in df_services.columns:
    df_services['delay'] = pd.to_numeric(df_services['Stop:Arrival delay'], errors='coerce').fillna(0)
elif 'Stop:Departure delay' in df_services.columns:
    df_services['delay'] = pd.to_numeric(df_services['Stop:Departure delay'], errors='coerce').fillna(0)
else:
    # If no delay column exists, create a dummy one
    print("WARNING: No delay column found. Creating dummy delays (all 0).")
    df_services['delay'] = 0

print("Delay column used")

# Drop rows where departure or arrival is invalid
df_services = df_services.dropna(subset=['Stop:Departure time', 'Stop:Arrival time'])

# Create unique train ID
df_services['train_id'] = df_services['Service:RDT-ID']

# For each train: get first departure, last arrival, and MAX delay (worst delay on that train)
journey_times = (df_services
                 .groupby('train_id', as_index=False)
                 .agg({
                     'Stop:Departure time': 'min',  
                     'Stop:Arrival time': 'max',    
                     'delay': 'max'                  
                 })
                 .rename(columns={
                     'Stop:Departure time': 'first_departure',
                     'Stop:Arrival time': 'last_arrival',
                     'delay': 'max_delay'
                 }))

print(f"Unique trains: {len(journey_times):,}")

# Calculate median time (midpoint between first departure and last arrival)
journey_times['median_time'] = (
    journey_times['first_departure'] + 
    (journey_times['last_arrival'] - journey_times['first_departure']) / 2
)

# Extract hour from median time
journey_times['hour'] = journey_times['median_time'].dt.hour

# Count unique days
unique_dates = journey_times['median_time'].dt.date.nunique()
print(f"Unique calendar days: {unique_dates}")

# Count delayed vs on-time trains
delayed_trains = len(journey_times[journey_times['max_delay'] > 0])
on_time_trains = len(journey_times[journey_times['max_delay'] <= 0])

print(f"\nTrains with delays (max_delay > 0): {delayed_trains:,}")
print(f"Trains on-time (max_delay <= 0): {on_time_trains:,}")
print(f"Percentage delayed: {100 * delayed_trains / len(journey_times):.1f}%")

# Calculate average delay per hour (all trains, including on-time ones with delay=0)
avg_delay_per_hour = journey_times.groupby('hour')['max_delay'].mean()
avg_delay_per_hour = avg_delay_per_hour.reindex(range(24), fill_value=0)

print(f"\nAverage max delay per hour (ALL trains, including on-time):")
print(avg_delay_per_hour.round(1))


# VISUALIZATION
hours = list(range(24))
delays = avg_delay_per_hour.values

fig, ax = plt.subplots(figsize=(14, 7))
bars = ax.bar(hours, delays, color='steelblue', edgecolor='black', alpha=0.8, width=0.8)

ax.set_xlabel('Hour of day', fontsize=12, fontweight='bold')
ax.set_ylabel('Average maximum delay (minutes)', fontsize=12, fontweight='bold')
ax.set_title('Average train delays per hour (2023–2024)\nAll trains included (on-time + delayed)', 
             fontsize=14, fontweight='bold')
ax.set_xticks(hours)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels above each bar
for bar, val in zip(bars, delays):
    ax.annotate(f'{val:.2f}', 
                xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                xytext=(0, 4), textcoords='offset points',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('average_delays_per_hour_all_trains.png', dpi=300, bbox_inches='tight')
plt.show()


# SUMMARY

print("\nSUMMARY ")
print("-" * 50)

peak_delay_hour = avg_delay_per_hour.idxmax()
print(f"Peak delay hour: {peak_delay_hour}:00 with avg {avg_delay_per_hour[peak_delay_hour]:.2f} min delay")

lowest_delay_hour = avg_delay_per_hour.idxmin()
print(f"Lowest delay hour: {lowest_delay_hour}:00 with avg {avg_delay_per_hour[lowest_delay_hour]:.2f} min delay")

print(f"Overall average delay across all hours and trains: {avg_delay_per_hour.mean():.2f} minutes")
print(f"Maximum single train delay in dataset: {journey_times['max_delay'].max():.0f} minutes")
