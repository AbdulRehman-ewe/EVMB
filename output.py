import pandas as pd

# Create a dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Write the dataframe to an Excel file
df.to_excel('data.xlsx', index=False)
