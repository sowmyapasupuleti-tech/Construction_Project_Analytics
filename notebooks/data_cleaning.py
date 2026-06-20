import pandas as pd
import numpy as np
from datetime import datetime

print("\n" + "="*60)
print("CONSTRUCTION DATA CLEANING PROCESS")
print("="*60 + "\n")

# Load the raw data
print("📂 Loading raw data...")
df = pd.read_csv('data/raw_construction_data.csv')
print(f"✓ Loaded {len(df)} projects")

print("\n" + "="*60)
print("STEP 1: Initial Data Overview")
print("="*60)
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nMissing Values:\n{df.isnull().sum()}")

# Data Cleaning Steps
print("\n" + "="*60)
print("STEP 2: Data Cleaning & Processing")
print("="*60)

# Remove duplicates
df = df.drop_duplicates()
print(f"✓ Removed duplicates. Total records: {len(df)}")

# Convert date columns to datetime
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])
print("✓ Converted date columns to proper format")

# Create new calculated columns (THIS IS THE IMPORTANT PART!)
print("\n✓ Creating calculated metrics...")
df['budget_variance'] = ((df['actual_cost'] - df['contract_value']) / df['contract_value'] * 100).round(2)
df['timeline_variance'] = ((df['timeline_days_actual'] - df['timeline_days_planned']) / df['timeline_days_planned'] * 100).round(2)
df['labor_efficiency'] = (df['budgeted_labor_days'] / df['actual_labor_days'] * 100).round(2)
df['cost_per_day'] = (df['actual_cost'] / df['timeline_days_actual']).round(0)
df['safety_score'] = (100 - (df['safety_incidents'] * 10)).clip(0, 100)
df['quality_score'] = (100 - (df['quality_issues'] * 5)).clip(0, 100)
print(f"  - Budget Variance (%)")
print(f"  - Timeline Variance (%)")
print(f"  - Labor Efficiency (%)")
print(f"  - Cost Per Day")
print(f"  - Safety Score (0-100)")
print(f"  - Quality Score (0-100)")

# Fill missing values
df['project_status'] = df['project_status'].fillna('Unknown')
print("✓ Handled missing values")

# Data validation - remove invalid records
df = df[df['actual_cost'] > 0]
df = df[df['timeline_days_actual'] > 0]
print("✓ Validated data (removed invalid records)")

# Save cleaned data
df.to_csv('data/cleaned_construction_data.csv', index=False)
print("\n✓ CLEANED DATA SAVED: data/cleaned_construction_data.csv")

print("\n" + "="*60)
print("STEP 3: Summary Statistics")
print("="*60)
print(f"Total Projects: {len(df)}")
print(f"Total Contract Value: ₹{df['contract_value'].sum():,.0f}")
print(f"Total Actual Cost: ₹{df['actual_cost'].sum():,.0f}")
print(f"Average Budget Variance: {df['budget_variance'].mean():.2f}%")
print(f"Average Timeline Variance: {df['timeline_variance'].mean():.2f}%")
print(f"Average Quality Score: {df['quality_score'].mean():.2f}/100")
print(f"Average Safety Score: {df['safety_score'].mean():.2f}/100")

print("\n✓ DATA CLEANING COMPLETE!")
print("="*60)

# Show first few rows of cleaned data
print("\n📊 First 3 cleaned records:")
print(df[['project_name', 'contract_value', 'actual_cost', 'budget_variance', 'quality_score']].head(3))