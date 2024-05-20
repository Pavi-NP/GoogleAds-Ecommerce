#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:28:14 2024

@author: paviprathiraja

A mock Google Ads dataset for an e-commerce selling only three products. 
This dataset contains one year of data and all the most important Google Ads KPIs (for example, clicks, impressions, CPC, sales etc…). 

"""
import numpy as np
import pandas as pd

# Load the original dataset
original_data = pd.read_csv('df_ads_groupby_date.csv')  # Adjust the path to your dataset
original_data['date'] = pd.to_datetime(original_data['date'], format='%d/%m/%Y')

# Create three copies of the original data, one for each product
product1_data = original_data.copy()
product2_data = original_data.copy()
product3_data = original_data.copy()

# Update the product column for each dataset
product1_data['product'] = 'Oppo'
product2_data['product'] = 'Samsung'
product3_data['product'] = 'Apple'

# Generate random engagement values for the "Oppo" product
product1_data['engagements'] = np.random.randint(100, 10000, size=len(product1_data))

# Convert clicks, conversions, engagements, impressions, and interactions to whole numbers
product1_data['clicks'] = product1_data['clicks'].astype(int)
product1_data['conversions'] = product1_data['conversions'].astype(int)
product1_data['engagements'] = product1_data['engagements'].astype(int)
product1_data['impressions'] = product1_data['impressions'].astype(int)
product1_data['interactions'] = product1_data['interactions'].astype(int)

# Adjust values for Product B (hit on December) and Product C as gradually popular
# For Product B (December)
product2_data.loc[product2_data['date'] == 'December', 'clicks'] *= 28
product2_data.loc[product2_data['date'] == 'December', 'conversions'] *= 100

# For Product C (gradually popular)
product3_data['clicks'] *= [1 + 0.005 * i for i in range(len(product3_data))]
product3_data['conversions'] *= [1 + 0.005 * i for i in range(len(product3_data))]

# Convert clicks, conversions, engagements, impressions, and interactions to whole numbers
product2_data['clicks'] = product2_data['clicks'].astype(int)
product2_data['conversions'] = product2_data['conversions'].astype(int)
product2_data['engagements'] = product2_data['engagements'].astype(int)
product2_data['impressions'] = product2_data['impressions'].astype(int)
product2_data['interactions'] = product2_data['interactions'].astype(int)

product3_data['clicks'] = product3_data['clicks'].astype(int)
product3_data['conversions'] = product3_data['conversions'].astype(int)
product3_data['engagements'] = product3_data['engagements'].astype(int)
product3_data['impressions'] = product3_data['impressions'].astype(int)
product3_data['interactions'] = product3_data['interactions'].astype(int)

# Concatenate the three product datasets into one
final_data = pd.concat([product1_data, product2_data, product3_data])

# Define the factors by which we want to adjust the values for Product A and Product B
product_a_factor = 1.5  # Example: Increase all values for Product A by 50%
product_b_factor = 1.2  # Example: Increase all values for Product B by 20%

# Adjust the values for Product A and Product B
final_data.loc[final_data['product'] == 'Oppo', ['clicks', 'conversions', 'cost_micros']] *= product_a_factor
final_data.loc[final_data['product'] == 'Samsung', ['clicks', 'conversions', 'cost_micros']] *= product_b_factor

# Sort the dataset by date in ascending order and then by product sequence A, B, C
final_data = final_data.sort_values(by=['date', 'product'], ascending=[True, True])

# # Load the modified dataset
# final_data = pd.read_csv('3Phone_Dataset.csv')  # Adjust the path to your modified dataset

# Add a random number between 100 and 500 to the conversions_value column
final_data['conversions_value'] += np.random.randint(100, 500, size=len(final_data))

# Multiply the conversions_value column by 100
final_data['conversions_value'] *= 100

# Calculate the value_per_conversion
final_data['value_per_conversion'] = final_data['conversions_value'] / final_data['conversions']
# Round value_per_conversion to two decimal places
final_data['value_per_conversion'] = final_data['value_per_conversion'].round(2)

# Calculate average CPC
final_data['average_cpc'] = final_data['average_cost'] / (1000*final_data['clicks'])
# Round average_cpc to two decimal places
final_data['average_cpc'] = final_data['average_cpc'].round(2)

# Calculate Click-Through Rate (CTR)
final_data['ctr'] = (final_data['clicks'] / final_data['impressions']) * 100

# Calculate Cost Per Mille (CPM)
final_data['average_cpm'] = (final_data['average_cost'] / final_data['impressions']) * 1000
# Round average_cpm to two decimal places
final_data['average_cpm'] = final_data['average_cpm'].round(2)


# Calculate Interaction Rate
final_data['interaction_rate'] = final_data['interactions'] / final_data['impressions']
# Round interaction_rate to four decimal places
final_data['interaction_rate'] = final_data['interaction_rate'].round(4)

# Calculate Engagement Rate
final_data['engagement_rate'] = final_data['engagements'] / final_data['impressions']
# Round engagement_rate to four decimal places
final_data['engagement_rate'] = final_data['engagement_rate'].round(4)

# # Calculate Average Cost
# final_data['average_cost'] = final_data['average_cost'] / final_data['interactions']

# Calculate Cost Per Conversion
final_data['cost_per_conversion'] = final_data['average_cost'] / final_data['conversions']
# Round Cost Per Conversion to two decimal places
final_data['cost_per_conversion'] = final_data['cost_per_conversion'].round(2)

# Calculate Cost Per Engagement (CPE)
final_data['cost_per_engagement'] = final_data['average_cost'] / final_data['engagements']
# Round cost_per_engagement to two decimal places
final_data['cost_per_engagement'] = final_data['cost_per_engagement'].round(2)

# Calculate conversion rate
final_data['conversion_rate'] = (final_data['conversions'] / final_data['clicks']) * 100
# Round conversion_rate to two decimal places
final_data['conversion_rate'] = final_data['conversion_rate'].round(2)

# Save the modified dataset to a new CSV file
final_data.to_csv("3Phone_Dataset_TEST.csv", index=False)


