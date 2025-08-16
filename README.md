# Reservoir Storage Dynamics and Water Value Analysis

## Project Overview
This project analyzes hydroelectric storage and water values for the Tekapo reservoir and other connected reservoirs (Hawea, Taupo, and Pukaki) in New Zealand.

The goal is to explore the seasonal relationships between reservoir storage levels and Tekapo water values and present them with clear visualizations.

## Key Features
Calculates Total Other Storage (sum of Hawea, Taupo, and Pukaki).

Converts Week number → Week Start Date dynamically.

Assigns season labels to each week’s data.

Computes seasonal max storage and percentage levels.

Categorizes storage into: Very Low, Low, Medium, High, Very High.

Generates seasonal scatter plots for Tekapo storage vs water value.

Exports the cleaned dataset for further analysis.

## Tech Stack
Python 3.x

pandas – data manipulation

numpy – numerical computations

matplotlib & seaborn – visualization

datetime – date handling

openpyxl / xlrd – Excel file support

## Outputs

Cleaned Dataset :Cleaned_Hydroelectric_Data.csv

### Seasonal Scatter Plots

Tekapo_WaterValue_vs_Storage_Summer.png

Tekapo_WaterValue_vs_Storage_Autum.png

Tekapo_WaterValue_vs_Storage_Winter.png

Tekapo_WaterValue_vs_Storage_Spring.png

# 🔎 Insights from the Graph

Inverse Relationship

As Tekapo Storage (GWh) increases, the Water Value ($/MWh) decreases.

This shows a clear negative correlation → more water available means electricity prices fall.

High Prices at Low Storage

When storage is very low (0–100 GWh), water values are extremely high (sometimes above $1000/MWh).

This suggests scarcity pricing: when water is scarce, the value of generating electricity spikes.

Stable Prices at High Storage

Beyond 400–800 GWh, water values stay consistently low (under $200/MWh).

This means when lakes are full, there’s less risk of shortage, so electricity generation cost/value drops.

Impact of Other Storage Levels (color categories)

Very Low / Low (red & brown dots): Prices are highest, showing tight supply conditions.

Medium (yellow dots): Prices still fluctuate but are generally moderate.

High & Very High (light blue & dark blue dots): Prices stabilize at low levels, even as Tekapo storage rises.

Seasonal Takeaway (Summer)

During summer, storage levels can vary widely.

System stress occurs when Tekapo AND other storages are low → prices surge.

If Tekapo storage is high and other storages are also high → prices remain very low, showing a healthy system.


