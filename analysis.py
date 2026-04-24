import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Load and clean data ---
df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')
df = df.drop(columns=['Row ID'])
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Days to Ship'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# --- Style settings ---
sns.set_theme(style='whitegrid')
os.makedirs('outputs', exist_ok=True)

# --- CHART 1: Sales by Category ---
plt.figure(figsize=(8, 5))
category_sales = df.groupby('Category')['Sales'].sum().sort_values()
colors = ['#d9534f', '#f0ad4e', '#5cb85c']
category_sales.plot(kind='barh', color=colors)
plt.title('Total Sales by Category', fontsize=14, fontweight='bold')
plt.xlabel('Sales (USD)')
plt.tight_layout()
plt.savefig('outputs/chart1_sales_by_category.png', dpi=150)
plt.close()
print("Chart 1 saved")

# --- CHART 2: Profit by Category ---
plt.figure(figsize=(8, 5))
category_profit = df.groupby('Category')['Profit'].sum().sort_values()
colors2 = ['#d9534f', '#5cb85c', '#5bc0de']
category_profit.plot(kind='barh', color=colors2)
plt.title('Total Profit by Category', fontsize=14, fontweight='bold')
plt.xlabel('Profit (USD)')
plt.tight_layout()
plt.savefig('outputs/chart2_profit_by_category.png', dpi=150)
plt.close()
print("Chart 2 saved")

# --- CHART 3: Sales trend over time (by year) ---
plt.figure(figsize=(9, 5))
yearly_sales = df.groupby('Year')['Sales'].sum()
yearly_sales.plot(kind='line', marker='o', color='#337ab7', linewidth=2.5)
plt.title('Annual Sales Trend (2014-2017)', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Sales (USD)')
plt.tight_layout()
plt.savefig('outputs/chart3_sales_trend.png', dpi=150)
plt.close()
print("Chart 3 saved")

# --- CHART 4: Profit by Region ---
plt.figure(figsize=(8, 5))
region_profit = df.groupby('Region')['Profit'].sum().sort_values()
region_profit.plot(kind='barh', color='#5cb85c')
plt.title('Total Profit by Region', fontsize=14, fontweight='bold')
plt.xlabel('Profit (USD)')
plt.tight_layout()
plt.savefig('outputs/chart4_profit_by_region.png', dpi=150)
plt.close()
print("Chart 4 saved")

# --- CHART 5: Discount vs Profit (scatter) ---
plt.figure(figsize=(8, 5))
colors_cat = {'Furniture': '#d9534f',
              'Office Supplies': '#f0ad4e',
              'Technology': '#5cb85c'}
for category, group in df.groupby('Category'):
    plt.scatter(group['Discount'], group['Profit'],
                alpha=0.4, label=category,
                color=colors_cat[category], s=15)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.title('Discount vs Profit by Category', fontsize=14, fontweight='bold')
plt.xlabel('Discount Rate')
plt.ylabel('Profit (USD)')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/chart5_discount_vs_profit.png', dpi=150)
plt.close()
print("Chart 5 saved")

print("\nAll charts saved to outputs folder.")

# --- Export cleaned data for Tableau ---
df.to_csv('outputs/superstore_cleaned.csv', index=False)
print("Cleaned CSV exported for Tableau.")

# --- Print executive summary ---
print("\n=============================")
print("  EXECUTIVE SUMMARY")
print("=============================")
print(f"Orders analyzed: {len(df):,}")
print(f"Date range: 2014 - 2017")
print(f"Total Revenue: ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
print(f"Overall Profit Margin: {(df['Profit'].sum()/df['Sales'].sum()*100):.1f}%")
print(f"Average Discount: {df['Discount'].mean()*100:.1f}%")
print(f"\nMost Profitable Category: Technology (${df[df['Category']=='Technology']['Profit'].sum():,.2f})")
print(f"Least Profitable Category: Furniture (${df[df['Category']=='Furniture']['Profit'].sum():,.2f})")
print(f"\nMost Profitable Region: {df.groupby('Region')['Profit'].sum().idxmax()}")
print(f"Least Profitable Region: {df.groupby('Region')['Profit'].sum().idxmin()}")
print(f"\nAvg Days to Ship: {df['Days to Ship'].mean():.1f} days")
print("=============================")

# Re-export CSV with clean encoding for MySQL
df.to_csv('outputs/superstore_mysql.csv', 
          index=False, 
          encoding='ascii', 
          errors='ignore')

print("MySQL-safe CSV exported.")