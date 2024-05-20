#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:14:17 2024

@author: paviprathiraja

Calculate indicators

    Visibility (impressions and clicks)

    Efficiency (CPC CTR)

    Outcome (Conversions, Cost/Cov., Conv. Rate)

of dataset
"""

import pandas as pd

# Load the dataset (assuming 'data.csv' is the name of your CSV file)
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'])

# Calculate total cost for the whole year
total_cost = data['cost_micros'].sum()

# Calculate total impressions for the whole year
total_impressions = data['impressions'].sum()

# Calculate total clicks for the whole year
total_clicks = data['clicks'].sum()

# Calculate average CPC for the whole year
average_cpc = data['average_cpc'].mean()

# Calculate total conversions for the whole year
total_conversions = data['conversions'].sum()

# Calculate CTR (Click-Through Rate) for the whole year
total_ctr = (total_clicks / total_impressions) * 100

# Calculate conversion rate for the whole year
total_conversion_rate = (total_conversions / total_clicks) * 100

# Calculate cost per conversion for the whole year
cost_per_conversion = total_cost / total_conversions

# Print the results
print("Total Cost for the whole year:", total_cost)
print("Total Impressions for the whole year:", total_impressions)
print("Total Clicks for the whole year:", total_clicks)
print("Average CPC for the whole year:", average_cpc)
print("Total Conversions for the whole year:", total_conversions)
print("CTR (Click-Through Rate) for the whole year %:", total_ctr)
print("Conversion Rate for the whole year %:", total_conversion_rate)
print("Cost per Conversion for the whole year:", cost_per_conversion)
