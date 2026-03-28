#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:30:03 2026

@author: marianasaavedra
"""

#Imports 

import pandas as pd
import matplotlib.pyplot as plt

#Load data

df = pd.read_csv("superstore.csv",encoding ="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month

#Data check

print(df.isnull().sum())
print(df.duplicated().sum())

#Insights:
# No missing values or duplicates in the dataset. 

#Monthly Sales

monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales.plot(kind ="line", xticks = range(1,13), title = "Monthly Sales", ylabel = "Total Sales")

#Insights:
# Sales peak in November, likely driven by seasonal events and pre-holiday shopping(black friday, right before christmas)
# Lower sales in the first couple months of the year (right after the holidays)

#Sales by Category

plt.figure()
cat_sales = df.groupby("Category")["Sales"].sum()
cat_sales.plot(kind = "bar", title = "Sales by Category", ylabel = "Total Sales")

#Insights:
# Technology generates the highest sales, indicating a strong demand for tech products 

#Profit by category

plt.figure()
profit_cat = df.groupby("Category")["Profit"].sum()
profit_cat.plot(kind = "bar",title = "Profit by Category", ylabel = "Total Profit (USD)")

#Insights:
# Profit assumed to be in USD based on the dataset context (United States)
# Technology generates both the highest sales and the highest profit, 
# making it the most valuable category for the business. 
# Focusing on this category, especially during peak sales months,
# could help maximize business revenue and growth.


