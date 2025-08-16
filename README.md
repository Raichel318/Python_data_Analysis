# Python_data_Analysis

Seasonal Analysis of Hydroelectric Reservoir Storage and Water Values

This project analyzes hydroelectric storage and water values for the Tekapo reservoir and other connected reservoirs (Hawea, Taupo, and Pukaki) in New Zealand. The goal is to understand seasonal relationships between reservoir storage levels and Tekapo water values and visualize these insights through plots.

The analysis helps to identify patterns such as:

How Tekapo water values fluctuate based on its own storage.

How combined storage from other reservoirs impacts water pricing.

Key Features

Calculates Total Other Storage (sum of Hawea, Taupo, Pukaki end-of-week storage).

Assigns season to each week’s data.

Calculates Total Other Storage as a percentage of seasonal maximum.

Classifies storage levels into: Very Low, Low, Medium, High, Very High.

Generates seasonal scatter plots of Tekapo storage vs water value colored by storage level.

Saves cleaned and processed dataset for further analysis.

Technologies & Libraries

Python 3.x

pandas – for data manipulation

numpy – for numeric calculations

matplotlib & seaborn – for visualization

datetime – for handling dates


hydroelectric-analysis/
│
├── Finalproject.py          # Main Python script
├── Hydroelectricdataset.xlsx # Raw dataset
├── Cleaned_Hydroelectric_Data.csv # Processed output
├── Tekapo_WaterValue_vs_Storage_*.png # Plots by season
└── README.md               # Project documentation
