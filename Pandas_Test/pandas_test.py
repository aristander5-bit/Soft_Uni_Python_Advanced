import os
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), 'Table.ods')
df = pd.read_excel(file_path, engine='odf')

print(f"{'PEOPLE':<12} {'AGE':<5}")
print("-" * 18)

for _, row in df.iterrows():
    print(f"{row['PEOPLE']:<12} {row['AGE']:<5}")

print("-" * 18)
total_years = df["AGE"].sum()
print(f"{'TOTAL':<12} {total_years:<5}")