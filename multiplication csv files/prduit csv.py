import pandas as pd

# Read the CSV files
df1 = pd.read_csv('multiplication csv files/file1.csv', header=None)
df2 = pd.read_csv('multiplication csv files/file2.csv', header=None)

# Perform element-wise multiplication
result = df1 * df2

# Save the result to a new CSV file
result.to_csv('multiplication csv files/result.csv', index=False, header=False)

# Calculate the total sum of all elements
total_sum = result.values.sum()

# Print the result DataFrame and the total sum
print("Result of element-wise multiplication:")
print(result)
print("\nTotal sum of all elements in the resulting matrix:")
print(total_sum)
