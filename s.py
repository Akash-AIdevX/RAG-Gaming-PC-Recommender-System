import pandas as pd
df = pd.read_csv("C:/Users/charl/Downloads/SKU.csv") 
sku_list = df.iloc[:, 0].dropna().astype(str).tolist()
formatted = ', '.join(f'"{sku}"' for sku in sku_list)
print(f"skus = [\n    {formatted}\n]")
