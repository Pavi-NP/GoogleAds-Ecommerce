# Mock Google Ads Dataset for E-commerce
## Overview
This project involves creating a mock Google Ads dataset for an e-commerce business selling three products: 
Oppo, Samsung, and Apple. The dataset spans one year and includes key Google Ads KPIs such as clicks, impressions, CPC, and sales.

## Key Features
• One year of data for three products

• Key KPIs: clicks, impressions, CPC, conversions, conversion rate, etc.

• Data includes adjustments for seasonal trends and product popularity

## Dataset Creation

The dataset is generated using Python with pandas and numpy libraries. Here’s a step-by-step breakdown:

### 1. Creating Product-specific Data:
Three copies of the original data are created, each representing one product.

### 2. Random Engagement Values:
Random engagement values are generated for each product.

### 3. Adjusting Values:
Specific adjustments are made to simulate real-world scenarios:

   o Higher activity for Samsung in December.
   
   o Gradual increase in popularity for Apple.
   
   o Overall increases in KPIs for Oppo and Samsung.
   

### 4. Calculating Metrics:
Various metrics are calculated including:

     o Average CPC
   
     o Click-Through Rate (CTR)
   
     o Cost Per Mille (CPM)
   
     o Interaction Rate
   
     o Engagement Rate
   
     o Cost Per Conversion (CPC)
   
     o Cost Per Engagement (CPE)
   
     o Conversion Rate
   

 ## Analysis and Visualization

### Total Yearly Metrics
The total cost, impressions, clicks, average CPC, conversions, CTR, conversion rate, and cost per conversion are calculated for the whole year.

### Plots
Several plots are created to visualize the data:

#### • Conversions vs. Conversion Rate by Day for December:
A bar and line chart comparing conversions and conversion rate by day.

#### • Average Cost Per Conversion by Day:
Bar charts for different months showing the average cost per conversion by day.

#### • Average Cost Per Conversion by Product:
A bar chart showing the average cost per conversion for each product.

#### • Average Conversions and Conversion Rate by Product:
A bar and line chart comparing average conversions and conversion rate by product.

#### • Conversions Value by Day:
Bar charts for different months showing the conversions value by day.

### Summary Table
A table summarizing total conversions, mean conversion rate, cost per conversion, and average cost for each product in December.

## NOTE: 
I also utilized a sample AdWords dataset for my analysis. To analyze this dataset, I used Looker Studio, a freely available data visualization and analytics platform developed by Google.

Reference:
https://lookerstudio.google.com/navigation/reporting


## Output:
[AdWordsData_Looker Studio.pdf](https://github.com/Pavi-NP/GoogleAds-Ecommerce/files/15377440/AdWordsData_Looker.Studio.pdf)


