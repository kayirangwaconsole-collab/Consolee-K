import pandas as pd

# Step 1: Read the CSV file
input_file = "conflict_regions.csv"
data = pd.read_csv(input_file)

print("Original data:")
print(data)
print(f"\nTotal rows: {len(data)}")

# Step 2: Define the regions we want to keep
regions_to_keep = ["Sub-Saharan Africa", "Middle East", "South-East Asia"]

# Step 3: Filter the data - keep only rows where Region matches our list
filtered_data = data[data['Region'].isin(regions_to_keep)]

print("\nFiltered data:")
print(filtered_data)
print(f"Total rows after filtering: {len(filtered_data)}")

# Step 4: Save the filtered data to a new CSV file
output_file = "filtered_conflict_regions.csv"
filtered_data.to_csv(output_file, index=False)

print(f"\nSuccess! Results saved to '{output_file}'")
