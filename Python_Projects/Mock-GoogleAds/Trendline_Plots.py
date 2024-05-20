#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:46:04 2024

@author: paviprathiraja

Tendline plots plus table and donut charts to compare data

"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
#data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y')
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# # Filter the data to include only November and December
# filtered_data = data[(data['date'].dt.month >= 11) & (data['date'].dt.month <= 12)]

############  Conversions vs Conversion Rate by Day for December ################

# Filter the data to include only December
december_data = data[data['date'].dt.month == 12]


# Group the filtered data by 'date' and aggregate 'conversions'
grouped_data = december_data.groupby('date').agg({'conversions': 'sum', 'conversion_rate': 'mean'})

# # Group the filtered data by 'date' and aggregate 'conversions'
# grouped_data = december_data.groupby('date')['conversions'].sum()

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot conversions as a column chart
ax1.bar(grouped_data.index, grouped_data['conversions'], color='tab:blue', label='Conversions')
ax1.set_ylabel('Conversions')

# Create a secondary y-axis for conversion rate
ax2 = ax1.twinx()
ax2.plot(grouped_data.index, grouped_data['conversion_rate'], color='tab:red', label='Conversion Rate (%)')
ax2.set_ylabel('Conversion Rate (%)')

# Add title and legend
plt.title('Conversions vs Conversion Rate by Day for December')
fig.legend(loc='upper left')

plt.show()



######################   Average Cost Per Conversion by Day  ##########################

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 12]

# Group the December data by date and calculate the mean cost per conversion for each day
grouped_data = december_data.groupby(december_data['date'].dt.date)['cost_per_conversion'].mean()

# Plotting
plt.figure(figsize=(12, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color='tab:blue')

# Add labels and title
plt.title('Average Cost Per Conversion by Day for December')
plt.xlabel('Date')
plt.ylabel('Average Cost Per Conversion')
plt.grid(axis='y')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()
#-------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 4]

# Group the December data by date and calculate the mean cost per conversion for each day
grouped_data = december_data.groupby(december_data['date'].dt.date)['cost_per_conversion'].mean()

# Plotting
plt.figure(figsize=(12, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color='tab:green')

# Add labels and title
plt.title('Average Cost Per Conversion by Day for April')
plt.xlabel('Date')
plt.ylabel('Average Cost Per Conversion')
plt.grid(axis='y')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


#-------------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 6]

# Group the December data by date and calculate the mean cost per conversion for each day
grouped_data = december_data.groupby(december_data['date'].dt.date)['cost_per_conversion'].mean()

# Plotting
plt.figure(figsize=(12, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color='tab:brown')

# Add labels and title
plt.title('Average Cost Per Conversion by Day for June')
plt.xlabel('Date')
plt.ylabel('Average Cost Per Conversion')
plt.grid(axis='y')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()

#-------------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 7]

# Group the December data by date and calculate the mean cost per conversion for each day
grouped_data = december_data.groupby(december_data['date'].dt.date)['cost_per_conversion'].mean()

# Plotting
plt.figure(figsize=(12, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color='tab:orange')

# Add labels and title
plt.title('Average Cost Per Conversion by Day for July')
plt.xlabel('Date')
plt.ylabel('Average Cost Per Conversion')
plt.grid(axis='y')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


#################### Cost Per Conversion  #################


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 12]

# Group the December data by product and calculate the mean cost per conversion for each product
grouped_data = december_data.groupby('product')['cost_per_conversion'].mean()

# Plotting
plt.figure(figsize=(10, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color=['tab:blue', 'tab:orange', 'tab:green'])

# Add labels and title
plt.title('Average Cost Per Conversion by Product for December')
plt.xlabel('Product')
plt.ylabel('Average Cost Per Conversion')
plt.grid(axis='y')
plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()

#------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 7]

# Group the December data by product and calculate the mean cost per conversion for each product
grouped_data = december_data.groupby('product')['cost_per_conversion'].mean()

# Plotting
plt.figure(figsize=(10, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color=['tab:blue', 'tab:orange', 'tab:green'])

# Add labels and title
plt.title('Average Cost Per Conversion by Product for July')
plt.xlabel('Product')
plt.ylabel('Average Cost Per Conversion')
plt.grid(axis='y')
plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()



################  Average Conversions and Conversion Rate by Product  ##########

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 12]

# Group the filtered data by 'product' and calculate the mean conversions and conversion rate for each product
average_conversions = december_data.groupby('product')['conversions'].mean()
average_conversion_rate = december_data.groupby('product')['conversion_rate'].mean()
# # Round conversion_rate to two decimal places
# average_conversion_rate = average_conversion_rate.round(4)

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot average conversions by product as a bar chart
average_conversions.plot(kind='bar', ax=ax1, color='skyblue', label='Average Conversions')
ax1.set_xlabel('Product')
ax1.set_ylabel('Average Conversions')

# Create a secondary y-axis for conversion rate
ax2 = ax1.twinx()
average_conversion_rate.plot(kind='line', ax=ax2, color='orange', label='Conversion Rate')
ax2.set_ylabel('Conversion Rate (%)')

# Add legend
fig.legend(loc='upper left')

# Title
plt.title('Average Conversions and Conversion Rate by Product for December')

# Show plot
plt.show()

### ------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 7]

# Group the filtered data by 'product' and calculate the mean conversions and conversion rate for each product
average_conversions = december_data.groupby('product')['conversions'].mean()
average_conversion_rate = december_data.groupby('product')['conversion_rate'].mean()

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot average conversions by product as a bar chart
average_conversions.plot(kind='bar', ax=ax1, color='skyblue', label='Average Conversions')
ax1.set_xlabel('Product')
ax1.set_ylabel('Average Conversions')

# Create a secondary y-axis for conversion rate
ax2 = ax1.twinx()
average_conversion_rate.plot(kind='line', ax=ax2, color='orange', label='Average Conversion Rate')
ax2.set_ylabel('Average Conversion Rate (%)')

# Add legend
fig.legend(loc='upper left')

# Title
plt.title('Average Conversions and Conversion Rate by Product for July')

# Show plot
plt.show()

############ TABLE ##################

import pandas as pd

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 12]

# Group the filtered data by 'product' and calculate the sum of 'conversions', mean of 'conversion_rate', mean of 'cost_per_conversion', and mean of 'average_cost'
product_table = december_data.groupby('product').agg({'conversions': 'sum', 'conversion_rate': 'mean', 'cost_per_conversion': 'mean', 'average_cost': 'mean'}).reset_index()

# Display the product table
print(product_table)


########################  conversions_value #################

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 12]

# Group the December data by date and calculate the mean cost per conversion for each day
grouped_data = december_data.groupby(december_data['date'].dt.date)['conversions_value'].mean()

# Plotting
plt.figure(figsize=(12, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color='tab:blue')

# Add labels and title
plt.title(' Conversions Value by Day for December')
plt.xlabel('Date')
plt.ylabel('Conversions Value ')
plt.grid(axis='y')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()
#-------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 4]

# Group the December data by date and calculate the mean cost per conversion for each day
grouped_data = december_data.groupby(december_data['date'].dt.date)['conversions_value'].mean()

# Plotting
plt.figure(figsize=(12, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color='tab:green')

# Add labels and title
plt.title('Conversions Value by Day for April')
plt.xlabel('Date')
plt.ylabel('Conversions Value ')
plt.grid(axis='y')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


#-------------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 6]

# Group the December data by date and calculate the mean cost per conversion for each day
grouped_data = december_data.groupby(december_data['date'].dt.date)['conversions_value'].mean()

# Plotting
plt.figure(figsize=(12, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color='tab:brown')

# Add labels and title
plt.title('Conversions Value by Day for June')
plt.xlabel('Date')
plt.ylabel('Conversions Value')
plt.grid(axis='y')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()


#---------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("3Phone_Dataset_TEST.csv")

# Convert 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'], format='%Y/%m/%d')

# Filter the data to include only December
december_data = data[data['date'].dt.month == 7]

# Group the December data by date and calculate the mean cost per conversion for each day
grouped_data = december_data.groupby(december_data['date'].dt.date)['conversions_value'].mean()

# Plotting
plt.figure(figsize=(12, 6))

# Create a bar graph
grouped_data.plot(kind='bar', color='tab:orange')

# Add labels and title
plt.title('Conversions Value by Day for July')
plt.xlabel('Date')
plt.ylabel('Conversions Value')
plt.grid(axis='y')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()

#####################################






