import pandas as pd
import glob

# 1. Read all CSV files from the data folder
files = glob.glob('./data/*.csv')
df_list = [pd.read_csv(f) for f in files]
df = pd.concat(df_list, ignore_index=True)

# 2. Filter for Pink Morsels only
df = df[df['product'].str.lower() == 'pink morsel']

# 3. Create 'sales' column (Price * Quantity)
# Use r'[\$,]' to avoid that SyntaxWarning
df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
df['sales'] = df['price'] * df['quantity']

# 4. Keep only the necessary columns
final_df = df[['sales', 'date', 'region']]

# 5. Save the result
final_df.to_csv('formatted_data.csv', index=False)
print("File 'formatted_data.csv' created successfully!")